# Meridian - Showcase
Meridian - E-commerce Supply Chain & Client Operations. Public portfolio showcase using simulated data. Development in progress.

## Business Case

Read the [Meridian - Business Case](Business-Case.md) for the business problem, options assessment, proposed value, scope, success measures and delivery approach.

## Terminology

**SKU (Stock Keeping Unit):** A company's internal identifier for a specific product variant. Different sizes, colours or configurations receive separate SKUs. For example, a black 750 mL bottle might use `BTL-750-BLK`, while its white equivalent uses `BTL-750-WHT`.

A **barcode** is a machine-readable symbol that encodes an identifier. An SKU identifies a product variant within the business; a barcode provides a scannable representation of an identifier, which may be an SKU or another code such as a GTIN.

Meridian's demonstration includes **250 SKUs**, meaning 250 distinct product variants tracked across purchasing, production, inventory, freight and warehouse receipts. All demonstration data will be simulated.


## Development status

**Data foundation completed; first read-only operations interface implemented.** This is a simulated portfolio project, not client work or a live production system.

The reproducible baseline spans **1 October 2025 to 30 September 2026**, with 8 fictional brands, 250 SKUs, 20 manufacturers and 4 Australian warehouses. All monetary amounts use AUD cents.

| Generated records | Count |
|---|---:|
| Purchase orders | 2,473 |
| Shipments | 2,890 |
| Warehouse receipts | 2,498 |
| Daily demand records | 91,250 |
| Daily inventory snapshots | 91,250 |
| Operational exceptions | 2,072 |
| Assigned follow-ups | 2,072 |
| Unsent client update drafts | 416 |

Scenarios include production delays, split deliveries, freight delays, damaged or missing receipts, seasonal demand and stockouts. Eight local automated tests passed, covering quantity reconciliation, nonnegative stock, dates, historical client updates and reproducibility. These are simulated operating results, not demonstrated client savings.

The implementation, schema and full reproduction instructions reside in the private core repository. The public repository contains the portfolio presentation. The first operations interface supports combined brand and warehouse filters, demand and fulfilment trends, searchable/sortable records, pagination, detail panels and labelled CSV exports. All 12 local automated tests passed. Browser checks also verified combined filters, record details, shipment search, pagination and a filtered CSV download. The private first version is ready for owner review; full module workflows, persistent changes, live integrations, SOPs and final portfolio screenshots remain to be built.
