# Meridian - Business Case

E-commerce Supply Chain & Client Operations  
27 October 2026 · Revised project brief

*Meridian is an independent portfolio project based on a hypothetical business serving e-commerce brands. All operating data is simulated. The starting brief came from the coordination responsibilities described in a public logistics vacancy; this document does not describe an engagement with that employer.*

## Why I chose this problem

A supply-chain coordinator can spend much of the day answering a question that sounds straightforward: where is this order, and what happens next?

The answer may require checking a manufacturer's latest message, a purchasing spreadsheet, a freight update and a warehouse receipt. Each record describes part of the journey. The coordinator still has to work out whether those records agree and what the client needs to know.

I chose this problem because the coordination effort is easy to underestimate. Tracking more orders is only part of the workload. Each additional brand brings its own products, commitments, questions and unresolved issues. A process that works for a few accounts can become difficult to maintain as the business grows.

For Meridian, I am working with the assumption that this information is spread across separate files and communication channels. That assumption would need to be checked with a real team. The project explores whether connecting those records can make daily coordination more reliable and less time-consuming.

## What Meridian should change

My proposal is to give the coordinator a consistent view of an order from purchasing through warehouse receipt, with inventory and follow-ups attached to that same operating picture.

The useful part is the context. A shipment that is five days late may not need urgent intervention if the brand has enough stock. A smaller delay on a fast-moving product could require an immediate decision. The coordinator should be able to see that difference without rebuilding the analysis from several files.

Meridian is organised around six areas: production and purchasing, inventory planning, freight coordination, warehouse receipts, client communication, and action tracking. Together, these should let a user follow an order, investigate a problem and prepare an update from consistent records.

For example, consider a fictional brand waiting for a shipment of bottles. The manufacturer misses its promised readiness date. The coordinator needs to establish the revised date, check how much saleable stock remains and determine whether the client needs to approve a change in freight or purchasing.

When the shipment arrives, the warehouse may report fewer usable units than expected. Meridian should preserve the difference between what was ordered, what was shipped and what was accepted. Damaged and missing units need a follow-up; they must not silently become available stock.

The coordinator owns that follow-up. The operations lead sets escalation rules, while the client or another authorised person approves decisions involving additional spending. Suppliers, forwarders and warehouse contacts provide the underlying confirmations. Software can make those responsibilities visible, but the people involved still have to act.

## Why build a dedicated tool?

Better spreadsheets are a credible alternative. Standard templates, consistent naming and clear operating procedures may solve much of the problem for a small team. They would also require less development and ongoing support.

An established ERP or warehouse management system is another option, particularly where a business needs broader transaction processing. Its suitability would depend on the actual requirements, configuration effort and total cost.

I am developing Meridian to test a more focused approach: connecting the records and decisions that a coordination team handles every day. The case for it becomes stronger when repeated reconciliation, account reporting and missed follow-ups consume enough effort to justify maintaining an application.

That is something to demonstrate, not assume. If a well-run spreadsheet process achieves the same result at lower cost, custom software would need another clear advantage.

The initial scope therefore stays close to coordination. It does not include accounting, payroll or autonomous purchasing. Client messages and spending decisions require human review. Shopify and Canary7 workflows will begin with sample imports or exports; live connections depend on verified specifications and authorised access.

## How I would judge its value

The first benefit I would investigate is time spent preparing and checking account updates. A coordinator should be able to spend more time resolving an issue and less time finding out what happened.

I would also examine how quickly important exceptions are acknowledged, whether follow-ups have clear owners, and whether stock records remain consistent after partial or damaged deliveries.

For a pilot, I would measure the existing process before setting a final improvement target. The comparison should use similar accounts and transaction complexity, with the same incoming information available to both workflows. Comparing a simple demonstration with a busy operating team would not provide a fair result.

There are a few acceptance conditions I would treat as essential:

- Closing stock must reconcile to opening stock, accepted receipts and fulfilled sales.
- Each receipt must explain its expected, accepted, damaged and missing quantities.
- Every exception must have an assigned owner and a due date.
- A client update must agree with the records available on its preparation date.

These checks establish whether the information can be trusted. Usability and commercial value need separate evidence.

There is no supported return-on-investment figure at this stage. A financial assessment would include development, hosting, maintenance, integration work and training. Any value assigned to time saved should use observed hours and an agreed labour cost. Released staff capacity should only be called a cash saving if it actually reduces expenditure.

Likewise, displaying a stockout does not show that Meridian prevented one. A claim about fewer stockouts would require a controlled comparison or a pilot that can distinguish the effect of the tool from changes in demand or supplier performance.

## Practical concerns

The main dependency is the quality of the incoming information. A connected application will still be wrong if a supplier date is stale or a warehouse receipt is incomplete. The finished workflow needs to make the source and age of important updates visible, and show where confirmation is still outstanding.

Alert volume also needs attention. If every delay appears equally urgent, the coordinator gains another list to clear. I want priorities to reflect stock exposure, time sensitivity and the decision required. The first version provides a starting view of these issues; its thresholds still need to be tested through realistic scenarios.

There is also an adoption question. Someone must own each record and know when to update it. Before a real implementation, I would agree those responsibilities, approval limits and working-time expectations with the team.

Real client use would additionally require account access controls, an audit trail, backup arrangements and agreed support responsibilities. Those requirements are part of assessing readiness for a pilot, not capabilities I am claiming for the current demonstration.

## Where the project stands

The simulated foundation covers eight brands, 250 SKUs, 20 manufacturers and four Australian warehouses over twelve months. It includes purchase orders, shipments, receipts, inventory movements, exceptions and sample client update drafts.

The six-module demonstration is now implemented with a persistent personal workspace. It supports draft purchase orders and approvals, inventory planning, an illustrative air/sea route map, freight updates, warehouse receipt reconciliation, client update drafts and owned follow-ups. Twenty-six automated tests passed across the data foundation, overview and operational rules; TypeScript validation and a production build also passed. Browser checks covered saved PO approval across reloads, receipt validation and discrepancy follow-ups, client draft approvals, CSV upload rejection, filtering, details, pagination and exports.

Demo changes are saved on the server and remain separate from the reproducible historical baseline. No external orders or messages are submitted. Live integrations and production approval controls remain outside this demonstration.

The demonstration now lets a reviewer follow an order through the process, understand an exception, identify the responsible person and prepare an account update from the same records. The next decision is whether to release public demo access after owner review.

A commercial pilot would be a separate decision. It would need real stakeholder discovery, a measured baseline, an implementation budget and agreement on what improvement would justify continuing.
