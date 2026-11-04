# SAM Field Cheat Sheet

## Core Asset Fields

| Field | Type | Example | Notes |
|-------|------|---------|-------|
| Number | Auto | AST0010001 | System-generated, unique |
| Name | String | Laptop - Sarah Jenkins | Descriptive name |
| Category | Choice | Hardware > Computer > Laptop | Determines other available fields |
| Asset Tag | String | AST-001234 | Physical sticker number |
| Serial Number | String | FCH12345678 | From hardware, for warranty |
| State | Choice | In Stock, Assigned, In Repair, Retired | Where in lifecycle |
| Assigned To | Reference | Sarah Jenkins | sys_user who has it |
| Assigned By | Reference | IT Manager | Who assigned it |
| Assignment Date | Date | 2026-11-04 | When assigned |
| Purchase Date | Date | 2026-01-15 | When bought |
| Cost | Currency | 1200.00 | Purchase price |
| Vendor | Reference | Dell Technologies | Who you bought from |
| Location | Reference | New York Office | Where physically located |
| Custodian | Reference | IT Department | Department responsible |
| Pool | Reference | Laptop Pool | Group of similar assets |

## Mandatory vs Optional vs Critical

### Critical (System Won't Work Without)
- **Number** — Auto-generated
- **Category** — Drives form layout
- **State** — Tracks lifecycle position
- **Asset Tag** — Physical identification

### Mandatory (Required for Daily Work)
- **Name** — Identifies the asset
- **Purchase Date** — Warranty and depreciation
- **Assigned To** — Accountability
- **Vendor** — Support contact

### Optional (Nice to Have)
- **Cost** — Budget tracking
- **Location** — Physical whereabouts
- **Pool** — Grouping assets
- **MAC Address** — Network identification

## Category Hierarchy Example

```
Hardware
  └── Computer
        └── Laptop
              └── Dell XPS 13 (Model)
Software
  └── Application
        └── Microsoft Office 365 (License)
Contract
  └── Maintenance
        └── Dell Support (3-year)
```

## Quick Actions

- **Create new asset:** Asset Management > Assets > All > New
- **Find an asset:** Search by asset tag, serial number, or name
- **Change state:** Open asset > Change State dropdown > Update
- **Reassign asset:** Open asset > Change Assigned To > Update
- **Retire asset:** Open asset > State = Retired > Add retirement reason
