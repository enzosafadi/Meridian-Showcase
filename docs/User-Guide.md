# Meridian - User Guide

Meridian is a portfolio demonstration of e-commerce supply-chain coordination. It uses fictional brands, suppliers and warehouses. Its six modules now support saved demo workflows, alongside the operations overview.

The scenario date is **30 September 2026**. Historical demand covers the previous twelve months. Actual completion, dispatch and receipt dates cannot go beyond that date; future planned dates are allowed. The activity log records the real time a demo change was saved.

## Your workspace

Sign in to use your own saved workspace. Demo changes are stored on the server under your site-specific user identity and survive browser refreshes. Other users do not share those changes. The baseline remains unchanged.

The application does not send messages, place supplier orders, commit real freight bookings or connect to Shopify or Canary7. A demo approval records a decision in the workspace; it is not a production purchasing authorisation or separation of duties.

## Operations Overview

Use the brand and warehouse filters to narrow the account scope. The indicators show stock risks, overdue production, in-transit shipments and overdue follow-ups. The demand chart remains historical: recording a receipt changes current stock, not past demand.

The attention list numbers records continuously across pages. Search or status filtering starts a new numbered list at 1. Inventory risks intentionally excludes healthy stock; Inventory planning includes all three stock conditions.

## Production & Purchasing

Create a draft PO from the module or from a product's inventory recommendation. Quantity must meet its minimum order quantity and use full cartons. The application validates these rules again on the server.

A draft does not increase incoming inventory. Review and approve it to add its quantity to the pipeline. Record supplier-confirmed production completion before dispatching a linked shipment. Original commitments remain visible when a readiness date is revised; add an operating note to explain the change.

No supplier receives these orders. Order value is quantity multiplied by the simulated unit cost in AUD, excluding tax, duty and currency conversion.

## Inventory Planning

Review all 250 product variants, their assigned warehouses, saleable stock, incoming quantities and recent requested demand. Product details include MOQ, carton size, lead times, unit cost, retail price and suggested replenishment.

Stock cover uses average requested demand over the final 30 calendar days. This avoids understating demand when a stockout limited actual sales. The recommendation is a simple target-stock policy: nominal lead time plus 30 days, less on-hand and approved incoming quantities, rounded to cartons and MOQ. It is a baseline planning method rather than a fitted forecasting model.

Only accepted receipt units become saleable. Damaged and missing units remain visible as discrepancies.

## Freight Coordination & Route Map

The map distinguishes air and sea routes. Filter the mode, brand or warehouse, then select an incoming shipment to focus its lane. The map covers four origin countries and four Australian destination warehouses.

**The lanes and gateway assignments are illustrative.** The geography is simplified, routes are not carrier tracks, and estimated packing weights and volumes are demonstration assumptions. No live vessel or aircraft positions are available.

Shipment detail includes its purchase order, SKU, origin, destination, mode, units, cartons, estimated weight and volume, freight cost, planned and observed dates, and current status. Download a labelled sample packing list when needed.

Book shipments only against approved orders with unallocated quantities. Record departure after production completion, or revise the ETA with a confirmation note. The consolidation view identifies planned sea shipments with the same origin country, receiving warehouse and departure week. Saving a proposal groups them for review; it does not confirm a carrier booking or claim a freight saving.

## Warehouse Receipts

Choose an in-transit shipment and record accepted, damaged and missing units. Those quantities must sum to the expected shipment quantity. Receipt date cannot precede departure or exceed the scenario date. Duplicate receipts are rejected.

Saving a receipt increases saleable stock by accepted units and removes the full shipment quantity from incoming stock. A discrepancy creates an assigned follow-up. Partial delivery is represented by separately receivable split shipments; a single shipment receives one final reconciled receipt.

For uploads, download the sample CSV template. Required columns are `shipment_id`, `accepted_units`, `damaged_units` and `missing_units`; `date` and `note` are optional. Uploads are limited to 50 lines and 100 KB. Review validation results before saving. The server checks every line; an invalid line rejects the whole batch. This is Meridian's sample format, not a certified Canary7 file.

## Client Communications

Select a client account and prepare an update. The generated text reflects the selected warehouse scope and current operational records. Review and edit it before saving an unsent draft version.

Approve a saved version with a review note. Approved text remains preserved; prepare a new version to make changes. Read or export draft text at any time. Historical weekly sample updates are also available. Nothing is emailed or sent through WeChat.

## Actions & Escalations

Review open, overdue and closed follow-ups. Search by reference, owner, account or SKU. Create a manual action, change its owner and deadline, resolve it with a note, or reopen it when further work is required.

Closing an action records that the follow-up was completed. It does not erase an inventory shortage, receipt discrepancy or late shipment. Review those linked records separately.

## Activity and exports

The activity log records saved demo operations, references, notes and timestamps. Export the log or the current module's filtered records. CSVs label the data as simulated and identify AUD cents in monetary fields. Packing weights and volumes are estimates.

When concurrent tabs make changes, a stale revision is rejected rather than silently overwriting newer work. Refresh before retrying. Network or validation failures display an error and do not claim a successful save.
