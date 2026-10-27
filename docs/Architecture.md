# Meridian - Architecture

The application separates a reproducible baseline from each visitor's saved demo changes.

The Python generator produces an auditable SQLite operating history. `meridian.export_application` derives the application baseline without modifying that history. The server exposes this simulated baseline and the current signed-in visitor's workspace state. A shared domain layer materialises the current records and validates all supported actions.

The interface runs in the browser; the server routes run on the Sites-supported Vinext/Cloudflare Worker stack. D1 stores each workspace's JSON changes, revision and update timestamp. The tracked Drizzle migration owns the workspace table. Baseline data is not inserted through a migration.

## Saved operations

- Draft and approve purchase orders; revise readiness; record production completion.
- Book a simulated shipment; record departure; revise arrival estimate; propose consolidation.
- Reconcile one receipt or an atomic batch of sample CSV receipts.
- Create, assign, resolve and reopen follow-ups.
- Save client draft versions and record approvals.

Every successful operation appends a workspace activity entry. A revision check prevents stale tabs from overwriting later changes. Receipt processing checks the full batch before any state is saved. Monetary calculations use integer AUD cents.

## Access and boundaries

The current Site remains private. Hosted writes require the dispatch-provided ChatGPT user identity, same-origin JSON requests and server-side business validation. Workspace records use the site-specific user ID, not an email address. Anonymous visitors, if public viewing is enabled later, receive the baseline without write access. Development identity fallback is restricted to the development build and recognised local preview hosts.

This is not a production ERP. It has one demo actor per workspace, a fixed scenario date, one assigned warehouse per SKU, no external transactions, and no live WMS, carrier or e-commerce integrations. The JSON workspace is capped to keep the demonstration bounded. Real deployment would need role separation, more granular storage, monitoring, backup policy, retention and integration-specific validation.

The freight map uses approximate vector geography and labelled illustrative routes. It is an operations demonstration, not a navigation or carrier-tracking product.
