# ServiceNow SAM — Getting Started Video Guide

**Author:** opencode agent  
**Date:** 2026-11-04  
**Format:** Video script / outline (for recording)  
**Estimated video length:** 25–30 minutes  
**Target audience:** Beginners new to ServiceNow SAM

---

## Video Overview

This video walks a brand-new user through getting started with ServiceNow Service Asset Management (SAM) from zero — no prior ServiceNow experience required.

By the end of the video, viewers will be able to:
1. Log into a ServiceNow instance
2. Navigate to the SAM module
3. Understand foundation data (companies, locations, categories, states)
4. Create their first asset record end-to-end
5. Move an asset through its lifecycle states

---

## Video Script — Scene by Scene

### 0:00–0:30 — Introduction
- Welcome and what SAM is (ELI5: a giant inventory for IT stuff)
- What you'll learn in this video
- Prerequisites: a ServiceNow instance with ITIL or admin role

### 0:30–2:00 — Logging In & Navigation
- Open your ServiceNow URL (e.g., `https://yourcompany.service-now.com`)
- Log in with your credentials
- Locate the Application Navigator (hamburger menu or left sidebar)
- Search for "Asset Management"
- Click **Asset Management > Assets > All**

### 2:00–4:00 — Foundation Data (The "Must-Haves" First)
Explain that you can't create assets without foundation data:
- **Companies/Vendors:** Company Administration > Companies
- **Locations:** Company Administration > Locations  
- **Departments:** Organization > Departments
- **Asset Categories:** Asset Management > Administration > Categories
- **Asset States:** Asset Management > Administration > States
- **Users:** Organization > Users

Show each one briefly with examples:
- Company: Dell Technologies
- Location: New York HQ
- Category: Hardware > Computer > Laptop
- State: In Stock

### 4:00–8:00 — Create Your First Asset (Hands-On)
1. Navigate to **Asset Management > Assets > All**
2. Click **New**
3. Fill in the form:
   - Name: "Laptop for Sarah - Dell XPS 13"
   - Category: Hardware > Computer > Laptop
   - Asset Tag: "AST-001234"
   - Serial Number: "FCH12345678"
   - State: "In Stock"
   - Purchase Date: Today's date
   - Cost: 1200.00
   - Vendor: Dell Technologies
4. Click **Submit**
5. Note the asset number (e.g., AST0010001)

### 8:00–12:00 — Move Through Lifecycle States
Demonstrate changing the state:
1. Open the asset record you just created
2. Change State → "Ordered" (add PO number in comments)
3. Change State → "In Stock" (add serial number when it arrives)
4. Change State → "Assigned" (assign to Sarah Jenkins)
5. Change State → "In Repair" (screen cracked scenario)
6. Change State → "Retired" (replaced after 3 years)

### 12:00–15:00 — Create a Software License
1. Navigate to **Asset Management > Software > All**
2. Click **New**
3. Fill in:
   - Name: "Microsoft Office 365"
   - License Count: 50
   - Installation Count: 42
   - License Type: "Subscription"
   - Expiration Date: 1 year from now
4. Click **Submit**

### 15:00–18:00 — Create a Contract
1. Navigate to **Asset Management > Contracts > All**
2. Click **New**
3. Fill in:
   - Name: "Dell Support Contract 2026"
   - Vendor: Dell Technologies
   - Start Date: Today
   - End Date: 3 years from now
   - Contract Value: 5000.00
4. Click **Submit**

### 18:00–22:00 — Run a Report
1. Navigate to **Reports > View / Run**
2. Search for "Assets by Category"
3. Run the report
4. Explain what the report shows

### 22:00–25:00 — Common Mistakes & Wrap-Up
- Mistake 1: Creating assets before foundation data
- Mistake 2: Not using asset tags
- Mistake 3: Forgetting to retire old assets
- Where to go next (course list, labs, infographics in this repo)

### 25:00–28:00 — Q&A / Next Steps
- Links to course learning path
- Links to labs in this repository
- Links to infographics
- Encouragement to practice in PDI

---

## On-Screen Visual Cues (for video editor)

| Time | Visual Element |
|------|---------------|
| 0:30 | Zoom in on Application Navigator |
| 2:00 | Highlight "Asset Management > Administration > Categories" menu path |
| 4:00 | Screen recording of filling out the New Asset form |
| 8:00 | State dropdown menu highlighted with callout bubble |
| 12:00 | Software asset form side-by-side with hardware asset form |
| 18:00 | Report results highlighted with cursor |

---

## Required Assets for Recording

- ServiceNow PDI instance (free at developer.servicenow.com)
- Screen recording software (OBS, Loom, Camtasia)
- Microphone for clear audio
- Example data ready (vendor names, asset tags, serial numbers)

---

## Related Materials in This Repo

| Material | File | Use During/After Video |
|----------|------|------------------------|
| SAM ELI5 Basics | `opencode/guides/sam-eli5-basics.md` | Pre-video reading |
| Foundation Data Guide | `opencode/guides/sam-foundation-data.md` | Pre-video reading |
| Guided Setup Checklist | `opencode/guides/sam-guided-setup.md` | Post-video reference |
| Asset Lifecycle Lab | `opencode/labs/sam-asset-lifecycle.md` | Post-video hands-on |
| Field Cheat Sheet | `opencode/resources/sam-field-cheatsheet.md` | During video (field reference) |
| Asset Lifecycle SVG | `opencode/infographics/asset-lifecycle.svg` | Visual aid during lifecycle section |
| Field Classification SVG | `opencode/infographics/field-classification.svg` | Visual aid during field explanation |
| Roles & Permissions SVG | `opencode/infographics/roles-permissions.svg` | Visual aid during login/setup |
| Concept Summarizer Script | `opencode/scripts/sam_concept_summarizer.py` | Post-video tool for clarifying concepts |
| Foundation Data Audit Script | `opencode/scripts/sam_foundation_data_audit.py` | Post-video tool for auditing PDI |

---

## Video Recording Tips

1. **Keep it under 30 minutes** — attention spans drop after that
2. **Show, don't just tell** — screen record every click
3. **Use real examples** — "Sarah's Dell XPS 13" is more memorable than "Asset 1"
4. **Pause between major steps** — give viewers time to follow along in their own PDI
5. **Mention the repo** — point viewers to this repository for labs and infographics

---

## Next Video Ideas (Series)

- Video 2: Software License Management (deep dive)
- Video 3: Contract Management & Renewals
- Video 4: Discovery & Automated Asset Population
- Video 5: Reports & Dashboards for SAM
- Video 6: ServiceNow CSA Exam Prep
