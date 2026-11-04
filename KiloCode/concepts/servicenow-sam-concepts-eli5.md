# ServiceNow SAM Concepts — ELI5 Glossary

**Agent:** Kilo  
**Date:** 2026-11-04  

---

## Purpose

This glossary explains ServiceNow SAM (Software Asset Management) concepts in plain English — the kind of explanation you could give to a 10-year-old. If you're new to SAM, start here. If you're stuck on a term, look it up here.

---

## Table of Contents

- [Platform Basics](#platform-basics)
- [SAM Data & Records](#sam-data--records)
- [SAM Logic & Automation](#sam-logic--automation)
- [Interface & Access](#interface--access)
- [SAM Integrations](#sam-integrations)
- [Reporting & Analytics](#reporting--analytics)
- [Security & Administration](#security--administration)

---

## Platform Basics

### Instance
**ELI5:** It's like your own private copy of ServiceNow that lives on the internet. You log in with a username and password, and everything you do stays in your copy.

**Real term:** ServiceNow Instance  
**Where to find it:** Your login URL (e.g., `https://mycompany.service-now.com`)

### Application
**ELI5:** It's like an app on your phone — but inside ServiceNow. Each app does one thing (like tracking assets, managing software licenses, or processing purchase orders).

**Real term:** ServiceNow Application  
**Where to find it:** Application Navigator (left sidebar) → All

### Module
**ELI5:** It's like a page inside an app. If the app is a notebook, the module is one page in that notebook.

**Real term:** ServiceNow Module  
**Where to find it:** Application Navigator → expand an app → click a module

---

## SAM Data & Records

### Table
**ELI5:** It's like a spreadsheet. Each row is one record, each column is one field. ServiceNow stores almost everything in tables.

**Real term:** Table (e.g., `alm_asset`, `alm_license`, `pm_purchase_order`, `pm_contract`)  
**Where to find it:** System Definition → Tables

### Record
**ELI5:** One row in the table. One software license, one hardware asset, one purchase order, one contract.

**Real term:** Record  
**Where to find it:** Open any list view → click a row

### Field
**ELI5:** One column in the spreadsheet. One piece of information about a record (like "Serial Number" or "License Count").

**Real term:** Field (or column)  
**Where to find it:** On a form, each input box is a field

### sys_id
**ELI5:** A unique ID code for every record. No two records have the same sys_id, even if they have the same name.

**Real term:** sys_id  
**Where to find it:** Right-click a record → Copy sys_id

### Form
**ELI5:** The screen you fill out to create or edit a record. Like a digital form.

**Real term:** Form  
**Where to find it:** Click New on any list, or click an existing record

### List
**ELI5:** A table view showing many records at once. Like a spreadsheet filtered to show only certain rows.

**Real term:** List  
**Where to find it:** Click a module name (not New)

---

## SAM Logic & Automation

### Business Rule
**ELI5:** A behind-the-scenes rule that runs automatically when you save or delete a record. Like "If license count exceeds entitlement, send alert to SAM manager."

**Real term:** Business Rule  
**Where to find it:** System Definition → Business Rules

### UI Policy
**ELI5:** A rule that changes what you see on the form while you're filling it out. Like "If Asset Category = Hardware, show Serial Number field; if Software, hide it."

**Real term:** UI Policy  
**Where to find it:** System UI → UI Policies

### Client Script
**ELI5:** JavaScript that runs in your browser when you interact with a form. Like "When I select a vendor, automatically populate the currency field."

**Real term:** Client Script  
**Where to find it:** System UI → Client Scripts

### Flow Designer
**ELI5:** A visual drag-and-drop tool for building multi-step processes. Like building with LEGO blocks — drag actions, connect them, and ServiceNow runs them in order.

**Real term:** Flow Designer  
**Where to find it:** Flow Designer (in the app menu)

### Scheduled Job
**ELI5:** A task that runs automatically on a schedule. Like "Every night at 2 AM, run software license compliance check."

**Real term:** Scheduled Job  
**Where to find it:** System Definition → Scheduled Jobs

---

## Interface & Access

### Application Navigator
**ELI5:** The left sidebar menu. It's how you find every module, app, and tool in ServiceNow.

**Real term:** Application Navigator  
**Where to find it:** Left side of every page

### Application Menu
**ELI5:** A category in the Application Navigator that groups related modules together.

**Real term:** Application Menu  
**Where to find it:** Top-level items in the left sidebar

### Role
**ELI5:** A permission badge. Your user account wears badges that say what you're allowed to do. No badge = no access.

**Real term:** Role (e.g., `sam_admin`, `sam_asset_manager`, `sam_license_manager`, `sn_sam.admin`)  
**Where to find it:** System Security → Users → your user → Roles

### ACL (Access Control List)
**ELI5:** A security rule that says who can see or change a record or field. Like a bouncer at a club.

**Real term:** ACL  
**Where to find it:** System Security → ACLs

### Update Set
**ELI5:** A package of changes you've made. Like saving your work in a folder so you can move it to another instance (like from Test to Production).

**Real term:** Update Set  
**Where to find it:** System Update Sets → Local Update Sets

---

## SAM Integrations

### REST Message
**ELI5:** A way for ServiceNow to send a message to another website or application over the internet. Like sending a request to a software vendor's API to check license entitlements.

**Real term:** Outbound REST Message  
**Where to find it:** System Web Services → Outbound REST Messages  
**Lab:** `labs/rest-message-integration/`

### Inbound REST API
**ELI5:** A way for another website or application to send data TO ServiceNow. Like your procurement system sending purchase order data into ServiceNow.

**Real term:** Table API / Record API  
**Where to find it:** System Web Services → Table API / Record API

### MID Server
**ELI5:** A small program installed on your own computer (inside your office) that talks to ServiceNow. Used when ServiceNow needs to discover hardware/software on your internal network that isn't on the public internet.

**Real term:** MID Server  
**Where to find it:** MID Server → Servers

### Import Set
**ELI5:** A way to bring data from outside (like an Excel spreadsheet of assets) into ServiceNow. ServiceNow reads the file, then you map the columns to ServiceNow fields.

**Real term:** Import Set  
**Where to find it:** System Import Sets → Load Data

### Remote Table
**ELI5:** A table that looks like a ServiceNow table but actually lives somewhere else. ServiceNow shows you the data without copying it. Like looking through a window at another building.

**Real term:** Remote Table  
**Where to find it:** System Definition → Remote Tables  
**Lab:** `labs/remote-table/`

---

## Reporting & Analytics

### Report
**ELI5:** A chart, graph, or list that summarizes data. Like "How many software licenses are out of compliance?"

**Real term:** Report  
**Where to find it:** Reports → Create New

### Dashboard
**ELI5:** A wall of reports. Multiple charts and lists on one screen so you can see everything at once.

**Real term:** Dashboard  
**Where to find it:** Dashboards → All

### Performance Analytics
**ELI5:** ServiceNow's built-in tool for tracking KPIs (Key Performance Indicators) over time. Like a scoreboard for your SAM program.

**Real term:** Performance Analytics  
**Where to find it:** Performance Analytics (in the app menu)

### Indicator
**ELI5:** One specific number being tracked. Like "Number of out-of-compliance licenses" or "Total hardware asset value."

**Real term:** Indicator  
**Where to find it:** Performance Analytics → Indicators

---

## Security & Administration

### Update Set
**ELI5:** (See above) A package of changes you can move between instances.

### Clone
**ELI5:** Making an exact copy of one ServiceNow instance to another. Like photocopying your entire setup.

**Real term:** Clone  
**Where to find it:** System Clone → Clone Instances

### System Property
**ELI5:** A setting that changes how ServiceNow behaves. Like a light switch or a dial.

**Real term:** System Property  
**Where to find it:** System Properties → All

---

## Quick Reference: When to Use What

| Want to... | Use this... |
|------------|-------------|
| Send data to another system (e.g., sync licenses to vendor) | Outbound REST Message |
| Receive data from another system (e.g., purchase data from ERP) | Inbound REST API / Table API |
| Bring data from outside (like an Excel file of assets) | Import Set |
| See external data without copying | Remote Table |
| Automatically do something when saving | Business Rule |
| Change what's visible on a form | UI Policy |
| Run JavaScript on a form | Client Script |
| Build a multi-step process (e.g., asset request workflow) | Flow Designer |
| Control who can see a record | ACL |
| See how many licenses are out of compliance | Report |
| See a wall of charts | Dashboard |
| Track a number over time | Indicator |

---

## SAM-Specific Terms

| Term | What It Means |
|------|---------------|
| **Entitlement** | The right to use a software license. One entitlement = one installation allowed. |
| **Allocation** | Assigning a license entitlement to a specific device or user. |
| **Compliance** | When your actual usage doesn't exceed your entitlements. |
| **Over-licensed** | You have more entitlements than you need (wasting money). |
| **Under-licensed** | You have more usage than entitlements (compliance risk). |
| **Asset Lifecycle** | The journey of an asset from request → procure → deploy → maintain → retire. |
| **Procurement** | The process of buying hardware or software assets. |
| **Contract** | A legal agreement with a vendor for software or services, often covering multiple licenses. |

---

*Generated by Kilo on 2026-11-04.*
