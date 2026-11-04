"""Repeatable repository checks. Exit nonzero for any failed configured gate."""
import argparse, ast, hashlib, json, os, re, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATTERNS={
 'private-key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
 'github-token':r'\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b',
 'aws-access-key':r'\bAKIA[A-Z0-9]{16}\b',
 'openai-secret':r'\bsk-(?:proj-)?[A-Za-z0-9_-]{35,}\b',
}

def verify(visibility, run_tests=True):
 config=json.loads((ROOT/'verification-config.json').read_text())
 errors=[]; counts={'syntax':0,'pdfs':0,'test_commands':0}
 if config['visibility']!=visibility: errors.append('Configured and actual repository visibility disagree.')
 if visibility=='public' and (ROOT/'Project Documents').exists(): errors.append('Public repository contains Project Documents.')
 for p in ROOT.rglob('*'):
  if not p.is_file() or any(x in p.parts for x in ('.git','node_modules','.venv','archive','Retired','.pytest_cache','__pycache__','evidence')):continue
  if p.suffix not in ('.py','.js','.mjs','.cjs','.json','.md','.html','.ts','.tsx','.sol','.txt','.yml','.yaml','.ipynb'):continue
  text=p.read_text(errors='replace')
  for name, pattern in PATTERNS.items():
   if re.search(pattern,text):errors.append(f'{name}: {p.relative_to(ROOT)}')
  if p.suffix=='.ipynb':
   notebook=json.loads(text)
   for cell in notebook.get('cells',[]):
    source=''.join(cell.get('source',[]))
    for match in re.finditer(r'''(CLIENT_SECRET|API_KEY|ACCESS_TOKEN)\s*=\s*(['"])([^'"]{20,})\2''',source,re.I):
     if not any(word in match[3].upper() for word in ('YOUR_','REDACTED','PLACEHOLDER')):
      errors.append(f'Hard-coded notebook credential: {p.relative_to(ROOT)} ({match[1]})')
  if p.suffix=='.py':
   try:ast.parse(text);counts['syntax']+=1
   except SyntaxError as e:errors.append(f'{p.relative_to(ROOT)}: {e}')
  if p.suffix in ('.js','.mjs','.cjs') and p.name!='three.min.js':
   r=subprocess.run(['node','--check',str(p)],capture_output=True,text=True)
   if r.returncode:errors.append(f'JavaScript syntax: {p.relative_to(ROOT)}\n{r.stderr}')
   else:counts['syntax']+=1
 if visibility=='private':
  from pypdf import PdfReader
  manifest=json.loads((ROOT/'Project Documents/CURRENT-v2.1.json').read_text())
  if len(manifest['documents'])!=6:errors.append('Exactly six current lifecycle documents are required.')
  for d in manifest['documents']:
   p=ROOT/d['path']
   if not p.is_file():errors.append(f'Missing current PDF: {d["path"]}');continue
   if hashlib.sha256(p.read_bytes()).hexdigest()!=d['sha256']:errors.append(f'PDF checksum changed: {d["path"]}')
   reader=PdfReader(p,strict=True)
   text='\n'.join(page.extract_text() for page in reader.pages)
   if not reader.pages or 'v2.1' not in text or '2026-11-03' not in text:errors.append(f'Invalid PDF metadata/content: {d["path"]}')
   counts['pdfs']+=1
 if run_tests:
  env=dict(os.environ,PYTHONPATH=str(ROOT/'src')+os.pathsep+str(ROOT))
  for command in config['test_commands']:
   command=[sys.executable if x=='{python}' else x for x in command]
   r=subprocess.run(command,cwd=ROOT,env=env,timeout=240)
   counts['test_commands']+=1
   if r.returncode:errors.append('Test command failed: '+' '.join(command))
 print(json.dumps({'visibility':visibility,'checks':counts,'errors':errors},indent=2))
 return 1 if errors else 0

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--visibility',choices=['public','private'],required=True);parser.add_argument('--skip-tests',action='store_true');args=parser.parse_args()
 raise SystemExit(verify(args.visibility,not args.skip_tests))
