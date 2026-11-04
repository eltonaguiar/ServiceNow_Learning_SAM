# Mandatory vs Critical vs Optional Fields — ServiceNow SAM

**Agent:** Kilo  
**Date:** 2026-11-04  

---

## Purpose

This document helps you understand the difference between mandatory, critical, and optional fields in ServiceNow SAM — and why knowing the difference matters when building forms, scripts, and integrations.

---

## Field Importance Levels

| Level | Definition | Example | Consequence of Missing |
|-------|-----------|---------|----------------------|
| **Mandatory** | The system won't let you save the record without it | `number` on `alm_license`, `name` on `alm_asset` | Record won't save. System throws an error. |
| **Critical** | The record saves, but the process breaks downstream | `assignment_group` on `alm_asset`, `state` on `pm_purchase_order` | Record saves but workflows break, SLAs don't start, notifications don't fire |
| **Optional** | Nice to have, but not required for core functionality | `comments`, `work_notes`, `asset_tag` | Record saves fine. Process continues. Data is just incomplete. |

---

## Mandatory Fields

**Definition:** Fields that must have a value before the record can be saved. ServiceNow enforces this at the database level.

### How to Identify Mandatory Fields

1. Look for a red asterisk (*) next to the field label on the form
2. Check the table definition: System Definition → Tables → [table] → Fields → look for `Mandatory = true`
3. Try saving without the value — the system will block you

### Examples

| Table | Mandatory Fields | Why |
|-------|-----------------|-----|
| `alm_license` | `number`, `name`, `license_type` | Every license needs a number, name, and type |
| `alm_asset` | `number`, `name` | Every asset needs a number and name |
| `pm_purchase_order` | `number`, `state`, `vendor` | Every PO needs a number, state, and vendor |
| `pm_contract` | `number`, `state`, `vendor` | Every contract needs a number, state, and vendor |

### Best Practice

Never try to bypass mandatory fields. If you need to create a record without a value for a mandatory field, you're likely approaching the problem wrong.

---

## Critical Fields

**Definition:** Fields that aren't enforced by the database but are required for business processes to work correctly. The record saves, but downstream processes fail.

### How to Identify Critical Fields

1. Look at business rules that reference the field
2. Look at workflows and flows that depend on the field
3. Look at notifications that use the field
4. Check SLAs that depend on the field
5. Ask the process owner

### Examples

| Table | Critical Field | Why It's Critical |
|-------|---------------|-------------------|
| `alm_asset` | `assigned_to` | Without it, no one knows who has the asset |
| `alm_license` | `entitlement_count` | Without it, compliance calculation is impossible |
| `pm_purchase_order` | `vendor` | Without it, no one knows who to pay |
| `pm_contract` | `end_date` | Without it, renewal tracking breaks |

### Downstream Impacts of Missing Critical Fields

| Missing Field | Downstream Impact |
|---------------|-------------------|
| `assigned_to` on `alm_asset` | No one knows who has the asset, it gets lost |
| `entitlement_count` on `alm_license` | Can't calculate compliance, over/under-licensing risk |
| `vendor` on `pm_purchase_order` | Procurement doesn't know who to order from |
| `end_date` on `pm_contract` | Can't track renewals, contracts lapse unnoticed |

---

## Optional Fields

**Definition:** Fields that are nice to have but not required for core functionality.

### Examples

| Table | Optional Field | Why It's Optional |
|-------|---------------|-------------------|
| `alm_asset` | `comments` | Helpful for context, but not required to track the asset |
| `alm_license` | `comments` | Helpful for context, but not required for compliance |
| `pm_purchase_order` | `justification` | Helpful for auditors, but PO can proceed without it |
| `pm_contract` | `notes` | Helpful for context, but not required for contract management |

### Best Practice

Fill optional fields when you have the information, but don't block process flow waiting for them.

---

## Field Decision Matrix

Use this table to decide how to treat each field:

| Field Characteristic | Mandatory | Critical | Optional |
|---------------------|-----------|----------|----------|
| Database prevents save without value | Yes | No | No |
| Business process breaks without it | Yes | Yes | No |
| Workflows depend on it | Yes | Yes | No |
| Notifications use it | Often | Yes | Rarely |
| SLAs depend on it | Often | Yes | Rarely |
| User can proceed without it | No | Yes | Yes |

---

## Practical Exercise

Pick any SAM table (e.g., `alm_license`) and answer:

1. What are the 3 most important mandatory fields?
2. What are the 3 most important critical fields?
3. What are 3 optional fields you often see filled in?
4. What happens if you create a license without `entitlement_count`?
5. What happens if you create an asset without `assigned_to`?

---

## Related Lists

**Note:** Related Lists are different from fields. They show related records (e.g., all allocations related to a license, all line items related to a PO).

| Related List Type | Mandatory? | Critical? | Notes |
|-------------------|-----------|-----------|-------|
| Child records (e.g., line items on a PO) | No | Often | Important for workflows |
| Related records (e.g., license on an asset) | No | Critical | Links records together |
| Approval records | Sometimes | Often | Needed for PO approval |

---

*Generated by Kilo on 2026-11-04.*
