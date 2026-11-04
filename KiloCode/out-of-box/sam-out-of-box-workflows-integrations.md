# Out-of-Box Workflows, Integrations, Playbooks, Metrics & Dashboards — ServiceNow SAM

**Agent:** Kilo  
**Date:** 2026-11-04  

---

## Purpose

This document covers what ServiceNow SAM provides out of the box (OOB) — workflows, integrations, playbooks, metrics, and dashboards — so you know what you get for free and what you need to build yourself.

---

## Out-of-Box Workflows

ServiceNow SAM ships with pre-built workflows for common SAM processes.

### SAM Workflows

| Workflow | Triggers On | What It Does | Where to Find |
|----------|-------------|--------------|---------------|
| Asset Request Fulfillment | Asset request created | Routes request through approval, then provisions asset | Flow Designer → All |
| Software License Allocation | License allocated | Assigns license entitlement to device/user, updates compliance | Flow Designer → All |
| Purchase Order Approval | PO created | Routes PO through approval chain based on value | Workflow → All |
| Contract Renewal | Contract nearing expiry | Notifies owners, creates renewal tasks | Workflow → All |
| Asset Retirement | Asset marked retired | Decommissions asset, updates CMDB | Workflow → All |

### How to View Workflows

1. Go to **Workflow → All**
2. Search for the workflow name
3. Click the workflow name to view the diagram
4. Click **Edit** to see the activities

### What to Look For

- Which table the workflow runs on
- What activities are included (approvals, notifications, script actions)
- What conditions start the workflow
- What the end state is

---

## Out-of-Box Integrations

ServiceNow SAM connects to other systems out of the box.

### Outbound REST Messages

| Integration | What It Does | Where to Find |
|-------------|--------------|---------------|
| Outbound REST Message | Sends data from ServiceNow to another system (e.g., software vendor API) | System Web Services → Outbound REST Messages |

### Inbound REST APIs

| API | What It Does | Where to Find |
|-----|--------------|---------------|
| Table API | Create, read, update, delete records via REST | System Web Services → Table API |
| Record API | Create, read, update, delete specific records | System Web Services → Record API |

### Import Sets

| Import Type | What It Does | Where to Find |
|-------------|--------------|---------------|
| CSV Import | Import asset data from CSV files | System Import Sets → Load Data |
| Excel Import | Import data from Excel files | System Import Sets → Load Data |

### MID Server

| Component | What It Does | Where to Find |
|-----------|--------------|---------------|
| MID Server | Connects ServiceNow to on-premise systems for discovery | MID Server → Servers |

### How to Test Integrations

1. **Outbound REST Message:** Create a REST Message, set the endpoint to a public API (e.g., `https://jsonplaceholder.typicode.com/posts`), run it, check the response
2. **Inbound Table API:** Use a tool like Postman or curl to POST to `https://your-instance.service-now.com/api/now/table/alm_license`
3. **Import Set:** Upload a CSV file and watch it create asset records

---

## Out-of-Box Playbooks

ServiceNow SAM provides pre-built playbooks for common scenarios.

| Playbook | What It Does | Where to Find |
|----------|--------------|---------------|
| Asset Request Fulfillment | Guides requesters through requesting and receiving assets | Flow Designer → Playbooks |
| License Compliance | Guides administrators through license compliance remediation | Flow Designer → Playbooks |
| Procurement Approval | Guides purchase orders through approval | Workflow → Change Management |

---

## Out-of-Box Metrics & Indicators

ServiceNow SAM tracks these metrics out of the box:

### SAM Metrics

| Metric | What It Measures | Where to Find |
|--------|-----------------|---------------|
| License Compliance Rate | Percentage of licenses in compliance | Performance Analytics → Indicators |
| Asset Utilization Rate | Percentage of assets actively used | Performance Analytics → Indicators |
| Software Spend by Vendor | Total spend grouped by vendor | Performance Analytics → Indicators |
| Hardware Lifecycle Stage | Distribution of assets across lifecycle stages | Performance Analytics → Indicators |
| Contract Expiration | Contracts expiring in next 30/60/90 days | Performance Analytics → Indicators |

### CMDB Metrics

| Metric | What It Measures | Where to Find |
|--------|-----------------|---------------|
| CMDB Completeness | Percentage of CIs with complete data | Performance Analytics → Indicators |
| CI Count | Total number of CIs | Performance Analytics → Indicators |

---

## Out-of-Box Dashboards

ServiceNow SAM provides pre-built dashboards:

| Dashboard | What It Shows | Where to Find |
|-----------|---------------|---------------|
| License Overview | License count, compliance status, entitlement vs. allocation | Dashboards → License Overview |
| Asset Overview | Asset count, status, lifecycle stage | Dashboards → Asset Overview |
| Procurement Overview | PO count, spend by vendor, approval status | Dashboards → Procurement Overview |
| Contract Overview | Contract count, expiration alerts, vendor distribution | Dashboards → Contract Overview |
| CMDB Overview | CI count, classes, relationships | Dashboards → CMDB Overview |

### How to View Dashboards

1. Go to **Dashboards → All**
2. Click a dashboard name to open it
3. Click **Edit** to customize it
4. Click **Configure** to change filters or time ranges

---

## How to Explore Out-of-Box Content

### Step 1: List What's Available

1. Go to **System Definition → Tables**
2. Filter by the application you're interested in (e.g., `alm_`, `pm_`)
3. Note the table names

### Step 2: List Workflows

1. Go to **Workflow → All**
2. List all workflows
3. Read the description of each

### Step 3: List Reports & Dashboards

1. Go to **Reports → All**
2. List all reports
3. Go to **Dashboards → All**
4. List all dashboards

### Step 4: Test One

1. Pick one workflow, report, or dashboard
2. Run it
3. Understand what it does
4. Modify it slightly
5. Save your version

---

## What's NOT Out of the Box

Don't expect these to work immediately:

- **Custom integrations** with your specific vendors (e.g., Microsoft, Oracle, Adobe)
- **Custom workflows** for your unique procurement processes
- **Custom dashboards** for your specific KPIs
- **Custom reports** for your specific data needs
- **Custom SLAs** for your specific business hours

These require configuration or development.

---

*Generated by Kilo on 2026-11-04.*
