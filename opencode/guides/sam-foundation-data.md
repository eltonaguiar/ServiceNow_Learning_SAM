# SAM Foundation Data — Beginner Guide

## What is Foundation Data? (ELI5)

Foundation data is the **basic information** that ServiceNow SAM needs to work before you can track any assets. Think of it like setting up a new office:

- You need desks (locations)
- You need employees (users/departments)
- You need suppliers (vendors/companies)
- You need to know what kinds of things you buy (categories)
- You need to know what condition things can be in (states)

Without foundation data, you can't create assets properly — the forms will be missing dropdown options, and reports won't make sense.

## Why Foundation Data Comes First

| Step | What | Why It Matters |
|------|------|----------------|
| 1 | Companies & Vendors | You can't record who you bought assets from |
| 2 | Locations | You can't say where an asset is |
| 3 | Departments & Cost Centers | You can't track who pays for what |
| 4 | Asset Categories | You can't create assets (form won't load right) |
| 5 | Asset States | You can't track where an asset is in its lifecycle |
| 6 | Asset Models | You can't specify exact make/model of hardware |

**Rule:** Foundation data first, assets second.

---

## Core Foundation Data Tables

| Table | Purpose | Example Records |
|-------|---------|-----------------|
| `cmn_company` | Companies you do business with | Dell Technologies, Microsoft, CDW |
| `cmn_location` | Offices, warehouses, data centers | New York HQ, London Office, Chicago Warehouse |
| `cmn_department` | Internal departments | IT, Finance, HR, Marketing |
| `cmn_cost_center` | Budget centers | IT-Operations, Finance-Systems |
| `alm_asset_category` | Types of assets | Laptop, Server, Software License, Monitor |
| `alm_asset_state` | Lifecycle stages | In Stock, Ordered, Assigned, In Repair, Retired |
| `alm_asset_model` | Specific makes/models | Dell XPS 13, MacBook Pro 14", iPhone 15 |
| `sys_user` | People who use assets | Sarah Jenkins, Mike Chen |

---

## Where to Find Foundation Data in ServiceNow

| Data Type | Navigation Path |
|-----------|----------------|
| Companies | Company Administration > Companies |
| Vendors | Company Administration > Vendors |
| Locations | Company Administration > Locations |
| Departments | Organization > Departments |
| Cost Centers | Organization > Cost Centers |
| Asset Categories | Asset Management > Administration > Categories |
| Asset States | Asset Management > Administration > States |
| Asset Models | Asset Management > Administration > Models |
| Users | Organization > Users |

---

## Mandatory vs Optional Foundation Data

| Data | Type | Why |
|------|------|-----|
| Company | Critical | Every asset needs a vendor/company |
| Location | Mandatory | You need to know where assets are |
| Department | Mandatory | Cost accountability |
| Asset Category | Critical | Determines which fields appear on asset form |
| Asset State | Critical | Tracks lifecycle position |
| Cost Center | Optional | Useful for budgeting, not required |
| Asset Model | Optional | Nice for specific make/model tracking |

---

## Setup Checklist

```
[ ] Companies created (Dell, Microsoft, Apple, etc.)
[ ] Vendors created (suppliers you buy from)
[ ] Locations created (all offices/warehouses)
[ ] Departments created (IT, Finance, HR, etc.)
[ ] Cost centers created (budget centers)
[ ] Asset categories defined (Laptop, Server, Software, etc.)
[ ] Asset states defined (In Stock, Ordered, Assigned, etc.)
[ ] Asset models created (Dell XPS 13, etc.)
[ ] Users created (employees who will receive assets)
```

---

## Common Foundation Data Mistakes

| Mistake | Result | Fix |
|---------|--------|-----|
| Creating assets before categories | Asset form breaks or shows wrong fields | Define categories first |
| Using "Miscellaneous" for everything | Reports are meaningless | Create specific categories |
| No location on assets | Can't find where assets are | Require location on all asset records |
| Duplicate vendors | Confusion about who to contact | Deduplicate vendor records |
| No asset states | Assets stuck in one state forever | Define full lifecycle states |

---

## Quick Reference: Foundation Data Dependencies

```
Company/Vendor
    ↓
Location
    ↓
Department → Cost Center
    ↓
Asset Category → Asset State → Asset Model
    ↓
   Asset Record (created last)
```

> **Remember:** You cannot create a meaningful asset record until the foundation data above it exists.
