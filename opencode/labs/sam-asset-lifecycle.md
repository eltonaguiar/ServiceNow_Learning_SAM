# SAM Asset Lifecycle Lab

## Goal

Walk a laptop through its entire lifecycle in ServiceNow SAM:
1. Request the asset
2. Order it (procurement)
3. Receive it
4. Assign it to an employee
5. Put it in repair
6. Retire it

**Estimated time:** 60 minutes  
**Prerequisites:** ITIL or admin role, access to ServiceNow SAM

---

## Scenario

Your company needs a new laptop for a new employee, Sarah. You'll track this laptop from the moment someone requests it until it's eventually retired.

---

## Step 1: Create an Asset Request (10 min)

1. Navigate to **Asset Management > Assets > All**
2. Click **New**
3. Fill in:
   - **Name:** Laptop for Sarah - Dell XPS 13
   - **Category:** Hardware > Computer > Laptop
   - **Asset Tag:** Leave blank (will be auto-generated or set later)
   - **State:** In Stock
   - **Requested By:** Your name
   - **Requested For:** Sarah Jenkins
   - **Purchase Date:** Today's date
   - **Cost:** 1200.00
   - **Vendor:** Dell Technologies
4. Click **Submit**
5. Note the asset number (e.g., AST0010001)

> **ELI5:** You're creating the "birth certificate" for this laptop. It now exists in ServiceNow even though it hasn't arrived yet.

---

## Step 2: Procure the Asset (10 min)

1. Open the asset record you just created
2. Change **State** from "In Stock" to "Ordered"
3. Add a note in the comments: "PO #PO-2026-001 placed with Dell on [date]"
4. Add the expected delivery date
5. Click **Update**

---

## Step 3: Receive the Asset (10 min)

1. When the laptop arrives, open the asset record
2. Change **State** from "Ordered" to "In Stock"
3. Add the **Serial Number** (from the physical laptop)
4. Add the **Asset Tag** (put a physical sticker on the laptop, record the number here)
5. Add the **MAC Address** (if you have it)
6. Click **Update**

---

## Step 4: Assign to an Employee (10 min)

1. Open the asset record
2. Change **State** from "In Stock" to "Assigned"
3. Set **Assigned To:** Sarah Jenkins
4. Set **Assignment Date:** Today's date
5. Add a note: "Issued to Sarah for her new role"
6. Click **Update**

> **ELI5:** The laptop now has a home. Sarah is responsible for it, and ServiceNow knows exactly who has it.

---

## Step 5: Put in Repair (10 min)

1. Three months later, Sarah's laptop screen cracks
2. Open the asset record
3. Change **State** from "Assigned" to "In Repair"
4. Add a note: "Screen cracked, sent to repair vendor on [date]"
5. Set **Expected Return Date:** 2 weeks from now
6. Click **Update**

> While in repair, Sarah gets a loaner laptop (create a separate asset record for the loaner).

---

## Step 6: Retire the Asset (10 min)

1. After 3 years, the laptop is too slow
2. Open the asset record
3. Change **State** from "Assigned" to "Retired"
4. Add a note: "Replaced with new model AST0020001"
5. Set **Retirement Date:** Today's date
6. Set **Disposal Method:** Recycled / Donated / Returned to vendor
7. Click **Update**

> The laptop is now retired. Sarah gets a new asset record for her replacement laptop.

---

## Key Breadcrumbs (Where to Click)

| Step | Navigation Path |
|------|----------------|
| Create Asset | Asset Management > Assets > All > New |
| View Asset List | Asset Management > Assets > All |
| Change State | Open asset record > State dropdown |
| Assign to User | Open asset record > Assigned To field |
| Add Notes | Open asset record > Comments/Work Notes |

---

## Common Mistakes

| Mistake | Result | Fix |
|---------|--------|-----|
| Creating asset after buying it | No record of purchase decision | Create asset request BEFORE ordering |
| Not setting asset tag | Can't physically identify the asset | Put sticker on device, record number in SAM |
| Forgetting serial number | Can't claim warranty | Record serial when asset arrives |
| Not retiring old assets | Reports show assets you no longer own | Retire assets when replaced |
| Assigning to wrong person | Wrong person held responsible | Double-check Assigned To before saving |

---

## Mandatory vs Optional vs Critical Fields

| Field | Type | Why |
|-------|------|-----|
| Asset Tag | Critical | Unique ID; can't track without it |
| Category | Critical | Determines available fields |
| State | Critical | Tells you where asset is in lifecycle |
| Assigned To | Mandatory | Knows who's responsible |
| Serial Number | Critical | Links to warranty and support |
| Purchase Date | Mandatory | Needed for depreciation and replacement planning |
| Cost | Optional | Helpful for budgeting |
| Vendor | Mandatory | Knows who to contact for support |

---

## What You Learned

- How to create an asset record from scratch
- How to move an asset through its lifecycle states
- How to assign an asset to an employee
- How to retire an asset when it's no longer needed
- Which fields are critical vs optional

---

## Next Steps

- Add software licenses to track software assets
- Create contract records for maintenance agreements
- Set up automatic asset discovery (finds computers on your network)
- Create reports: "Assets by Category," "Assets Due for Retirement," "Software License Compliance"
