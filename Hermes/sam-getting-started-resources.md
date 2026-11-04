# ServiceNow SAM Getting-Started Resources

**Author:** Hermes Agent  
**Date:** 2026-11-04  
**Branch:** main  
**Repo:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM

---

## Overview

This document is a curated list of resources for getting started with **ServiceNow SAM (Service Asset Management)**. It includes official documentation paths, learning resources, and practical references organized by skill level.

---

## 1. Official ServiceNow Documentation (via ServiceNow Docs / Docs.servicenow.com)

| Resource | Description | Best For |
|----------|-------------|----------|
| **SAM Product Documentation** | Official ServiceNow SAM admin and user guide | Reference, configuration details |
| **SAM Guided Setup** | Step-by-step activation and configuration | Initial setup |
| **SAM Asset Lifecycle** | How assets move from request to retirement | Understanding lifecycle |
| **SAM Procurement** | Converting purchase orders to assets | Procurement integration |
| **SAM Contract Management** | Tracking warranties, support, leases | Contract tracking |
| **SAM Software License Management** | Tracking software entitlements and installations | Software asset tracking |
| **CMDB Basics** | Configuration Management Database foundation | Linking assets to services |
| **Discovery (MID Server)** | Automated device discovery | Finding existing hardware |

**How to access:** Log into your ServiceNow instance → Help (?) → Documentation, or visit docs.servicenow.com and search for "Service Asset Management."

---

## 2. ServiceNow Training & Certification

| Resource | Description | Best For |
|----------|-------------|----------|
| **ServiceNow Now Learning** | Official ServiceNow training platform | Structured learning paths |
| **SAM Fundamentals Course** | Intro to SAM concepts and navigation | Beginners |
| **SAM Administration Course** | Configuring and administering SAM | Admins |
| **Certified Implementation Specialist - SAM** | Certification exam for SAM implementation | Career validation |
| **ServiceNow Community (community.servicenow.com)** | Q&A, forums, user groups | Troubleshooting, peer advice |

---

## 3. In-Instance Navigation Reference

| Module | Navigation Path | Purpose |
|--------|-----------------|---------|
| Assets | `Asset Management > Assets > All` | View and manage all assets |
| New Asset | `Asset Management > Assets > All > New` | Create an asset record |
| Asset Categories | `Asset Management > Categories > All` | Define asset types |
| Vendors | `Asset Management > Vendors > All` | Manage suppliers |
| Asset Models | `Asset Management > Models > All` | Define product models |
| Contracts | `Asset Management > Contracts > All` | Track warranties and support |
| States | `Asset Management > States > All` | Define lifecycle states |
| Guided Setup | `System Definition > Guided Setup > SAM` | Initial SAM activation |
| Roles | `User Administration > Roles` | Assign ITIL, asset_manager, etc. |

---

## 4. Core SAM Tables (Database Reference)

| Table | Purpose | Key Fields |
|-------|---------|------------|
| `alm_asset` | Core asset record | number, category, state, assigned_to, asset_tag |
| `alm_asset_category` | Asset categories | name, parent, active |
| `alm_asset_state` | Lifecycle states | name, sequence, default |
| `alm_vendor` | Vendors/suppliers | name, contact, email |
| `alm_hardware` | Hardware-specific fields | serial_number, mac_address, warranty_expiration |
| `alm_software` | Software-specific fields | license_count, installation_count |
| `alm_contract` | Maintenance/support contracts | start_date, end_date, renewal_date |
| `alm_asset_model` | Asset models | name, manufacturer, category |
| `alm_asset_pool` | Asset pools/groups | name, description, members |

---

## 5. Field Classification (Critical / Mandatory / Optional)

### Critical — System Won't Work Without
- **Number** — Auto-generated unique identifier
- **Category** — Drives form layout
- **State** — Tracks lifecycle position
- **Asset Tag** — Physical identification

### Mandatory — Required for Daily Work
- **Name** — Identifies the asset
- **Purchase Date** — Warranty and depreciation
- **Assigned To** — Accountability
- **Vendor** — Support contact

### Optional — Nice to Have
- **Cost** — Budget tracking
- **Location** — Physical whereabouts
- **Pool** — Grouping assets
- **Serial Number** — Warranty and support linkage

---

## 6. Common Beginner Mistakes & How to Avoid Them

| Mistake | Symptom | Prevention | Fix |
|---------|---------|------------|-----|
| No asset tag | Can't identify physical asset | Tag on receipt | Add tag to record |
| Wrong category | Wrong fields on form | Choose category first | Change category (may lose data) |
| Missing purchase date | No warranty tracking | Make it required in workflow | Backfill dates |
| Expired contracts missed | Support lapses | Set expiration alerts | Renew or retire |
| Assets vanish after offboarding | Lost hardware | Add recovery to HR workflow | Create return task |
| Software licenses untracked | Over/under-licensing | Run reconciliation | Match installs to entitlements |

---

## 7. Hands-On Lab: Asset Lifecycle (30-45 minutes)

**Goal:** Create and manage an asset from request to retirement.

### Prerequisites
- Admin or ITIL role in ServiceNow
- Access to Asset Management module

### Steps

1. **Create a vendor** — `Asset Management > Vendors > New` (e.g., Dell Technologies)
2. **Create an asset model** — `Asset Management > Models > New` (e.g., Dell XPS 13)
3. **Create an asset category** — `Asset Management > Categories > New` (Hardware > Computer > Laptop)
4. **Create a new asset** — `Asset Management > Assets > New`
   - Name: "Laptop - Sarah Jenkins"
   - Category: Laptop
   - Asset Tag: AST-001234
   - Serial Number: FCH12345678
   - Vendor: Dell Technologies
   - Model: Dell XPS 13
   - Purchase Date: 2026-01-15
   - State: In Stock
5. **Assign the asset** — Open asset → Assigned To: Sarah Jenkins → State: Assigned
6. **Create a contract** — `Asset Management > Contracts > New` (Dell Support, 3-year)
7. **Link contract to asset** — Open asset → Contract Reference: Dell Support
8. **Retire the asset** — Open asset → State: Retired → Add retirement reason

### Validation Checklist
- [ ] Vendor record exists
- [ ] Asset model exists
- [ ] Asset record created with tag and serial
- [ ] Asset assigned to a user
- [ ] Contract linked to asset
- [ ] Asset can be retired and un-retired

---

## 8. Recommended Learning Order

1. Read ELI5 basics (`opencode/guides/sam-eli5-basics.md`)
2. Review field cheat sheet (`opencode/resources/sam-field-cheatsheet.md`)
3. Walk through Guided Setup (`opencode/guides/sam-guided-setup.md`)
4. Complete the hands-on lab (Section 7 above)
5. Explore common mistakes (Section 6 above)
6. Try the concept summarizer script (`opencode/scripts/sam_concept_summarizer.py`)
7. Diagram SAM architecture (`opencode/templates/sam-architecture.mmd`)

---

## 9. Quick Reference: Where to Click

| What You Need | Click Path |
|--------------|------------|
| All assets | `Asset Management > Assets > All` |
| New asset | `Asset Management > Assets > All > New` |
| Vendors | `Asset Management > Vendors > All` |
| Contracts | `Asset Management > Contracts > All` |
| Categories | `Asset Management > Categories > All` |
| Models | `Asset Management > Models > All` |
| States | `Asset Management > States > All` |
| Guided Setup | `System Definition > Guided Setup > SAM` |
| Roles | `User Administration > Roles` |

---

## 10. Related Resources in This Repo

| Folder | Contents |
|--------|----------|
| `opencode/guides/` | ELI5 basics, guided setup, concept summaries |
| `opencode/resources/` | Field cheat sheet, module framework, mandatory vs critical |
| `opencode/labs/` | Asset lifecycle hands-on lab |
| `opencode/scripts/` | SAM concept summarizer script |
| `opencode/templates/` | SAM architecture diagram template |
