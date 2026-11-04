# ServiceNow SAM Module Learning Framework

**Agent:** Kilo  
**Date:** 2026-11-04  

---

## Purpose

This framework teaches you how to learn **any** ServiceNow SAM (Software Asset Management) module using the same repeatable process. ServiceNow SAM has many modules and applications, but they all follow the same underlying patterns. Learn the pattern once, apply it everywhere.

---

## The SAM Module Anatomy

Every SAM module has these common components:

| Component | What It Is | Where to Find It |
|-----------|------------|------------------|
| **Table** | The database table storing records | Table: `[table_name]` |
| **Form** | The UI for creating/editing records | Form designer on the table |
| **List** | The UI for viewing multiple records | List view on the table |
| **Business Rule** | Server-side logic that runs on save/delete | System Definition → Business Rules |
| **UI Policy** | Client-side logic that shows/hides fields | System UI → UI Policies |
| **Client Script** | JavaScript that runs in the browser | System UI → Client Scripts |
| **ACL** | Access control (who can see/edit) | System Security → ACLs |
| **Flow/Workflow** | Automated multi-step process | Flow Designer / Workflow |
| **Report** | Aggregated view of data | Reports → Create New |
| **Dashboard** | Visual collection of reports | Performance Analytics / Dashboards |

---

## SAM Module Learning Checklist

For any SAM module, answer these 10 questions:

1. What is the module's primary table name?
2. What is the required user role to access it?
3. What are the 5 most important fields on the main form?
4. What business rules fire on insert/update?
5. What UI policies control field visibility?
6. What ACLs protect the table?
7. What flows or workflows are associated?
8. What related tables does it connect to?
9. What reports/dashboards exist out of the box?
10. What integrations (inbound/outbound) does it support?

---

## SAM Module-Specific Quick Starts

### Software Asset Management (SAM)

**Core table:** `alm_software`, `alm_license`, `alm_software_installation`  
**Required role:** `sam_admin`, `sam_license_manager`, `sn_sam.admin`  
**Key fields:** `name`, `version`, `manufacturer`, `license_type`, `entitlement_count`, `allocated_count`  
**Common business rules:** License allocation, compliance calculation, software normalization  
**Lab:** Create a software record, create a license, allocate the license to a device/user, check compliance.

### Hardware Asset Management (HAM)

**Core table:** `alm_hardware`, `alm_asset`  
**Required role:** `sam_admin`, `sam_asset_manager`  
**Key fields:** `name`, `serial_number`, `asset_tag`, `status`, `asset_category`, `model`  
**Lab:** Create a hardware asset, assign it to a user, transfer it between locations, retire it.

### Procurement Management

**Core table:** `pm_purchase_order`, `pm_line_item`  
**Required role:** `sn_sam.admin`, `procurement_admin`  
**Key fields:** `number`, `state`, `vendor`, `total_cost`, `currency`  
**Lab:** Create a purchase order, add line items, submit for approval, receive against the PO.

### Contract Management

**Core table:** `pm_contract`  
**Required role:** `sn_sam.admin`, `contract_manager`  
**Key fields:** `number`, `state`, `vendor`, `start_date`, `end_date`, `contract_value`  
**Lab:** Create a contract, link assets/licenses to it, track expiration dates.

### Software License Management

**Core table:** `alm_license`, `alm_license_model`  
**Required role:** `sam_license_manager`, `sam_admin`  
**Key fields:** `name`, `license_model`, `entitlement_count`, `allocated_count`, `compliance_status`  
**Lab:** Create a license model, create a license, allocate entitlements, check compliance status.

---

## Success Packs

ServiceNow "Success Packs" are pre-built application packages for specific industries or use cases (e.g., Financial Services, Healthcare, Public Sector). They bundle:

- Pre-configured tables and fields
- Pre-built flows and workflows
- Pre-defined ACLs and roles
- Pre-designed dashboards and reports
- Sample data

### Pre-Requisites for Installing a Success Pack

| Prerequisite | Why It Matters | How to Verify |
|--------------|---------------|---------------|
| **Correct ServiceNow release** | Success Packs target specific releases (e.g., Vancouver, Washington) | System Properties → `glide.product.version` |
| **Required dependent applications** | Some packs need other apps installed first | Application Manager → check dependencies |
| **Administrator role** | You need `admin` to install | Your user record → Roles → `admin` |
| **Sufficient storage** | Packs add tables, records, and attachments | System Diagnostics → Storage |
| **Backup snapshot** | You can't uninstall a pack easily | Take a system snapshot before installing |

---

## Out-of-Box Components

Every ServiceNow SAM instance includes these out of the box:

### Workflows
- Asset Lifecycle workflow (Request → Receive → Deploy → Maintain → Retire)
- Software License Allocation workflow
- Purchase Order Approval workflow
- Contract Renewal workflow

### Integrations
- REST Message (outbound REST calls)
- Inbound REST API (Table API, Record API)
- MID Server (on-premise connectivity for discovery)
- Import Sets (data loading from CSV/Excel)

### Playbooks
- Asset Request fulfillment playbook
- License Compliance playbook
- Procurement Approval playbook

### Metrics & Dashboards
- License compliance rate
- Asset utilization rate
- Software spend by vendor
- Hardware lifecycle stage distribution
- Contract expiration alerts

---

*Generated by Kilo on 2026-11-04.*
