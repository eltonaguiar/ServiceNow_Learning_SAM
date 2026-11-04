# ServiceNow Certification Path — ServiceNow SAM (Software Asset Management)

**Agent:** Kilo  
**Date:** 2026-11-04  
**Repository:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM  
**Branch:** kilo-2026-11-04-sam-learning-materials  

---

## Purpose

This document maps out the recommended ServiceNow certification and training path for someone learning **ServiceNow Software Asset Management (SAM)**. It covers the full journey from beginner to certified implementation specialist, including prerequisites, recommended training courses, exam details, and estimated time investment.

---

## ServiceNow Certification Ecosystem

ServiceNow certifications are tiered into three levels:

| Level | Certification | Purpose |
|-------|---------------|---------|
| **Foundational** | Certified System Administrator (CSA) | Core platform skills — required foundation for nearly all other certifications |
| **Developer** | Certified Application Developer (CAD) | Application development on the ServiceNow platform |
| **Specialist** | Certified Implementation Specialist (CIS) | Role-specific implementation expertise (e.g., CIS-SAM, CIS-DF, CIS-ITSM) |
| **Expert** | Certified Technical Architect (CTA) | Advanced architecture and design expertise |
| **Master** | Certified Master Architect | Highest-level architectural authority |

ServiceNow certifications are tied to specific platform releases. When a new release launches, certified professionals must complete **delta exams** and pay the **Certification Maintenance Program (CMP)** fee to keep certifications current.

---

## Recommended Learning Path

The following sequence is the recommended order for someone pursuing ServiceNow SAM expertise:

| Order | Certification / Course | Type | Est. Time | Prerequisite |
|-------|------------------------|------|-----------|--------------|
| 1 | **Welcome to ServiceNow** | Free on-demand course | 1–2 hours | None |
| 2 | **Certified System Administrator (CSA)** | Certification + training | 2–4 weeks | None (recommended: 6+ months hands-on experience) |
| 3 | **ServiceNow Platform Implementation** | Training course | 3 days (ILT) | CSA recommended |
| 4 | **Certified Implementation Specialist – Data Foundations (CIS-DF)** | Certification | 2–4 weeks | CSA recommended |
| 5 | **Software Asset Management (SAM) Professional Fundamentals** | Training course | 3 days (ILT) | CIS-DF recommended |
| 6 | **Certified Implementation Specialist – Software Asset Management (CIS-SAM)** | Certification | 2–4 weeks | CIS-DF required |

**Total estimated time:** 6–12 weeks of part-time study and hands-on practice.

---

## Step 1: Welcome to ServiceNow (Free On-Demand)

**Purpose:** Introduce the ServiceNow platform, navigation, and basic concepts before committing to paid training.

| Attribute | Detail |
|-----------|--------|
| **Provider** | ServiceNow University |
| **Cost** | Free |
| **Format** | On-demand |
| **Prerequisite** | None |
| **Next step** | ServiceNow Administration Fundamentals |

**Why start here:** This is the absolute entry point. It covers navigation, forms and lists, users and groups, access control, the Service Catalog, flows, and data imports. It gives you enough context to decide if ServiceNow is right for you before investing in paid training.

---

## Step 2: Certified System Administrator (CSA)

**Purpose:** Establish foundational ServiceNow administration skills. CSA is the **gateway certification** — nearly every other ServiceNow certification builds on it.

| Attribute | Detail |
|-----------|--------|
| **Certification code** | CSA |
| **Provider** | ServiceNow University |
| **Cost** | ~$300 USD (exam voucher) |
| **Format** | Proctored online exam, 60 questions, 90 minutes |
| **Prerequisite** | None required, but **6+ months hands-on experience** with ServiceNow is strongly recommended |
| **Required training** | Welcome to ServiceNow + ServiceNow Administration Fundamentals |
| **Exam topics** | Navigation, forms and lists, users and groups, access control, Service Catalog, flows, data imports, core platform administration |

**Recommended training path:**
1. Welcome to ServiceNow (free, on-demand)
2. ServiceNow Administration Fundamentals (on-demand or instructor-led, 3 days)

**Why CSA first:** Almost every CIS (Certified Implementation Specialist) exam assumes CSA-level knowledge. Without it, you will struggle with more advanced certifications.

---

## Step 3: ServiceNow Platform Implementation (Optional but Recommended)

**Purpose:** Learn how to implement ServiceNow across an organization — planning, design, deployment, and governance.

| Attribute | Detail |
|-----------|--------|
| **Provider** | ServiceNow University |
| **Format** | Instructor-led training (ILT), 3 days |
| **Prerequisite** | CSA recommended |
| **Next step** | CIS-DF or CIS-SAM |

**Why take it:** If you plan to implement ServiceNow for an organization (not just use it), this course covers the end-to-end implementation methodology. It is a recommended prerequisite for CIS-SAM.

---

## Step 4: Certified Implementation Specialist – Data Foundations (CIS-DF)

**Purpose:** Validate your knowledge of the Configuration Management Database (CMDB) and Common Service Data Model (CSDM) — the foundation of all ServiceNow implementation work.

| Attribute | Detail |
|-----------|--------|
| **Certification code** | CIS-DF |
| **Provider** | ServiceNow University |
| **Cost** | ~$300 USD (exam voucher) |
| **Format** | Proctored online exam, ~60 questions, 90 minutes |
| **Prerequisite** | CSA recommended |
| **Required training** | Welcome to ServiceNow + ServiceNow Administration Fundamentals + ServiceNow Platform Implementation |

**Why CIS-DF before CIS-SAM:** ServiceNow requires CIS-DF as a **prerequisite** for CIS-SAM. You cannot register for the CIS-SAM exam without first passing CIS-DF. CMDB and CSDM are the foundation of SAM — you cannot manage software assets or hardware assets accurately without accurate configuration item (CI) data.

---

## Step 5: Software Asset Management (SAM) Professional Fundamentals

**Purpose:** Learn the core concepts of ServiceNow SAM — software license management, hardware asset management, procurement, contract management, and reconciliation.

| Attribute | Detail |
|-----------|--------|
| **Provider** | ServiceNow University |
| **Format** | On-demand or instructor-led (3 days) |
| **Prerequisite** | CIS-DF recommended |
| **Next step** | CIS-SAM exam |

**What you learn:**
- Software asset lifecycle management
- Software license models and entitlements
- Software discovery and normalization
- Software reconciliation
- Software compliance reporting
- Integration with CMDB

---

## Step 6: Certified Implementation Specialist – Software Asset Management (CIS-SAM)

**Purpose:** Validate that you can design, implement, and maintain ServiceNow SAM solutions at an implementation level.

| Attribute | Detail |
|-----------|--------|
| **Certification code** | CIS-SAM |
| **Provider** | ServiceNow University |
| **Cost** | ~$450 USD (exam voucher) |
| **Format** | Proctored online exam, 60 questions, 90 minutes |
| **Prerequisite** | **CIS-DF is required** |
| **Required training** | Welcome to ServiceNow + ServiceNow Administration Fundamentals + ServiceNow Platform Implementation + SAM Professional Fundamentals |
| **Recommended experience** | 6 months of field experience in ServiceNow deployment projects, participation in at least 2 ServiceNow deployment projects |
| **Exam topics** | Software Asset Core Overview & Fundamentals (14%), Data Integrity & CMDB (28%), Software License Management & Compliance (30%), Operational Integration (13%), Perpetual SAM (15%) |

**Exam domains:**
1. **Software Asset Core Overview & Fundamentals** (14%) — SAM basics, process architecture, application introduction
2. **Data Integrity** (28%) — Data importing, discovery and normalization, content services
3. **Software License Management** (30%) — License metrics, entitlements and allocations, software reconciliation
4. **Operational Integration** (13%) — Contract and change management, service catalog, software remediation
5. **Perpetual SAM** (15%) — Software model lifecycle, reporting, implementation and maintenance

---

## Alternative Paths

### If you want to focus on Hardware Asset Management (HAM) instead of SAM:

1. CSA → CIS-DF → CIS-HAM (Certified Implementation Specialist – Hardware Asset Management)
2. Training: Hardware Asset Management (HAM) Fundamentals

### If you want to focus on IT Service Management (ITSM):

1. CSA → CIS-DF → CIS-ITSM (Certified Implementation Specialist – IT Service Management)
2. Training: ITSM Fundamentals, Incident Management, Problem Management, Change Management

---

## Cost Summary

| Item | Estimated Cost (USD) |
|------|---------------------|
| Welcome to ServiceNow | Free |
| ServiceNow Administration Fundamentals | ~$2,700 (3-day ILT) or free on-demand |
| ServiceNow Platform Implementation | ~$2,700 (3-day ILT) |
| CSA exam | $300 |
| CIS-DF exam | $300 |
| SAM Professional Fundamentals | ~$2,700 (3-day ILT) |
| CIS-SAM exam | $450 |
| **Total estimated** | **~$4,000–$6,000** |

*Costs vary by region, training format (on-demand vs. instructor-led), and whether you use learning credits.*

---

## Study Tips

1. **Use a Personal Developer Instance (PDI):** Get a free ServiceNow developer instance to practice hands-on. Theory alone is not enough.
2. **Use official training materials only:** ServiceNow explicitly states that study materials posted elsewhere online are not official and should not be used to prepare for certification exams.
3. **Schedule your exam within 90 days:** Once you register and pay, you have 90 days to schedule and complete the exam.
4. **Plan for delta exams:** ServiceNow certifications are release-specific. When a new platform release launches, you must complete delta exams to keep your certification current.
5. **Budget for the Certification Maintenance Program (CMP):** Annual fee to maintain certifications.

---

## Recommended Learning Path Summary

```
Step 1: Welcome to ServiceNow (Free, On-Demand)
         ↓
Step 2: ServiceNow Administration Fundamentals → CSA Exam
         ↓
Step 3: ServiceNow Platform Implementation (Optional but recommended)
         ↓
Step 4: Certified Implementation Specialist – Data Foundations (CIS-DF)
         ↓
Step 5: Software Asset Management (SAM) Professional Fundamentals
         ↓
Step 6: Certified Implementation Specialist – Software Asset Management (CIS-SAM)
```

---

## Useful Links

- [ServiceNow Careers & Certifications](https://www.servicenow.com/careers/certifications.html)
- [ServiceNow University](https://learning.servicenow.com)
- [CIS-SAM Exam Blueprint](https://nowlearning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011570)
- [ServiceNow Learning Paths PDF](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/infographic/learning-paths.pdf)

---

*Generated by Kilo on 2026-11-04. Part of the ServiceNow_Learning_SAM repository at github.com/eltonaguiar/ServiceNow_Learning_SAM.*
