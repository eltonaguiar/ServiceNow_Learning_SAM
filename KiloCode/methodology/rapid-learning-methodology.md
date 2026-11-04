# Rapid Learning Methodology — ServiceNow SAM

**Agent:** Kilo  
**Date:** 2026-11-04  

---

## Overview

This is the core learning loop used throughout this repository. It is designed to take you from **zero knowledge** of a ServiceNow SAM module or concept to **working, demonstrable proficiency** in under 2 hours.

The loop has 5 steps. Do them in order. Do not skip steps.

---

## Step 1: Orient (10 minutes)

**Goal:** Know where the SAM module lives in the UI and what it does.

### Actions

1. **Find the module.** Go to the Application Navigator (left sidebar) → search for the SAM module name (e.g., "Software Asset Management", "Asset Management", "Procurement", "Contract Management").
2. **Identify the scope.** Is it a core platform module (Incident, Problem) or a SAM-specific app (Software Asset Management, Hardware Asset Management, Software License Management, Procurement, Contract Management)?
3. **Identify the primary table.** Every module is built on one or more tables. Find the table name (e.g., `alm_asset`, `alm_hardware`, `alm_software`, `alm_license`, `pm_purchase_order`, `pm_contract`).
4. **Identify the user role.** What role do you need to see it? (e.g., `sam_admin`, `sam_asset_manager`, `sam_license_manager`, `sn_sam.admin`, `itil`)
5. **Read the one-line description.** If you can't explain what the module does in one sentence, you're not ready to configure it.

### Output

A one-sentence summary: *"ServiceNow [Module Name] is used for [purpose]. It lives at [navigation path]. Its primary table is [table_name]. You need the [role_name] role to access it."*

---

## Step 2: Configure (15 minutes)

**Goal:** Turn the SAM module on and verify you can access it.

### Actions

1. **Activate the SAM plugin/application.** Go to System Applications → All Applications → search for the module (e.g., "Software Asset Management") → click Activate (if not already active).
2. **Grant yourself the role.** Go to System Security → Users → your user record → Related Lists → Roles → Edit → add the required role (e.g., `sam_admin`, `sam_asset_manager`, `sn_sam.admin`) → Save. Log out and log back in.
3. **Verify access.** Navigate to the module. If you see a list view or a form, you have access. If you see "No privileges," you missed a role.
4. **Create one test record.** Click New → fill in required fields → Submit. Note the sys_id of the record.

### Output

A live ServiceNow instance with the SAM module active, your user having the correct role, and at least one test record created.

---

## Step 3: Build (45 minutes)

**Goal:** Create a working artifact using the SAM module.

### Choose your lab based on what you're learning:

| If learning... | Build this... | See lab |
|----------------|---------------|---------|
| Software Asset Management | Create a software license, allocate it to a device/user | `labs/rest-message-integration/` |
| Hardware Asset Management | Create a hardware asset, track its lifecycle | `labs/remote-table/` |
| Procurement | Create a purchase order, receive against it | `labs/rest-message-integration/` |
| Contract Management | Create a software/hardware contract, link assets | `labs/remote-table/` |
| License Management | Create a license model, allocate entitlements | `labs/rest-message-integration/` |

### Actions

Follow the lab README and lab-steps.md for your chosen topic. Do not skip steps. Take screenshots at each major milestone.

### Output

A working artifact: a software license, a hardware asset record, a purchase order, a contract record, etc.

---

## Step 4: Verify (15 minutes)

**Goal:** Prove the artifact works end-to-end.

### Verification Checklist

- [ ] The record was created successfully (check the list view)
- [ ] Required fields are populated (mandatory fields filled)
- [ ] The integration returned data (check the response body or error log)
- [ ] The flow triggered correctly (check Flow Designer execution log)
- [ ] Access controls work (test with a user who should NOT have access)
- [ ] Related lists are populated (check related records on the form, e.g., allocations on a license)

---

## Step 5: Teach Back (15 minutes)

**Goal:** Prove you can explain it simply.

### Actions

Use `scripts/concept-summary-template.md` to write a summary covering:

1. **What is it?** (One sentence)
2. **What problem does it solve?** (One sentence)
3. **How do I use it?** (3 steps max)
4. **What broke and how did you fix it?** (Honest mistakes count)
5. **What's the next thing to learn?** (One thing)

If you can't explain it in under 2 minutes, go back to Step 3.

### Output

A written summary saved to your notes or shared with a teammate.

---

## Time Budget (per module)

| Step | Time | Cumulative |
|------|------|------------|
| Orient | 10 min | 10 min |
| Configure | 15 min | 25 min |
| Build | 45 min | 70 min |
| Verify | 15 min | 85 min |
| Teach Back | 15 min | 100 min |

**Target: Under 2 hours per module.**

---

## When You Get Stuck

1. **Check `docs/common-mistakes/sam-mistakes-to-avoid.md`** — 90% of issues are covered there.
2. **Re-read Step 1.** Did you miss a role or table name?
3. **Check the System Log** (`System Logs → All`) for errors.
4. **Ask:** "What changed since it last worked?" Revert that change.
5. **Start over.** Sometimes deleting and recreating is faster than debugging.

---

*Generated by Kilo on 2026-11-04.*
