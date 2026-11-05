# ServiceNow Learning Courses — Recommended Order

**Author:** opencode agent  
**Date:** 2026-11-04  
**Repo:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM

## Purpose

This document lists the top ServiceNow learning courses to take, in the order you should take them, for someone learning ServiceNow **Service Asset Management (SAM)** and general platform administration.

## Learning Philosophy

| Principle | Explanation |
|-----------|-------------|
| **Platform first, module second** | Learn how ServiceNow works (tables, forms, roles, workflows) before diving into SAM specifics |
| **Official + free first** | Start with ServiceNow's own free resources, then paid certification courses |
| **Hands-on before theory** | Use a personal developer instance (PDI) to practice as you learn |
| **SAM-specific last** | Foundation platform skills make SAM courses much easier |

---

## Recommended Course Order

### Phase 1: Platform Foundations (Weeks 1–3)

These courses teach you how ServiceNow works — tables, forms, roles, lists, and basic administration. **Do not skip these.**

| # | Course | Provider | Cost | Duration | Why First |
|---|--------|----------|------|----------|-----------|
| 1 | **ServiceNow Fundamentals** | ServiceNow (Now Learning) | Free* | 16–20 hours | Teaches platform basics: navigation, tables, forms, roles, lists, dashboards. Required context for everything else. |
| 2 | **ServiceNow Platform Administration** | ServiceNow (Now Learning) | Free* | 20–25 hours | Covers users, groups, roles, data policies, UI policies, business rules. You need this to administer SAM. |
| 3 | **ServiceNow UI Building & Service Portal** | ServiceNow (Now Learning) | Free* | 10–15 hours | How to build forms and portals users actually interact with. |
| 4 | **ServiceNow Flow Designer** | ServiceNow (Now Learning) | Free* | 8–12 hours | Low-code automation. SAM uses flows for asset lifecycle automation. |

\*Free with a ServiceNow Now Learning account (create one at https://nowlearning.servicenow.com)

**Personal Developer Instance (PDI):** Sign up for a free PDI at https://developer.servicenow.com — this is your sandbox for practice.

---

### Phase 2: IT Asset Management (SAM) (Weeks 4–6)

Once you understand the platform, learn SAM-specific concepts.

| # | Course | Provider | Cost | Duration | Why This Order |
|---|--------|----------|------|----------|----------------|
| 5 | **ServiceNow IT Asset Management (SAM) Fundamentals** | ServiceNow (Now Learning) | Free* | 12–16 hours | Covers asset lifecycle, procurement, receipt, assignment, retirement. Builds directly on Phase 1 platform skills. |
| 6 | **ServiceNow Software Asset Management** | ServiceNow (Now Learning) | Free* | 10–14 hours | License management, compliance, installations. Hard to understand without knowing assets first (course 5). |
| 7 | **ServiceNow Contract Management** | ServiceNow (Now Learning) | Free* | 6–10 hours | Contracts tie to assets and vendors. Learn after assets and software. |

---

### Phase 3: Advanced Administration & Integration (Weeks 7–10)

| # | Course | Provider | Cost | Duration | Why |
|---|--------|----------|------|----------|-----|
| 8 | **ServiceNow Integrations (REST, SOAP, MID Server)** | ServiceNow (Now Learning) | Free* | 12–16 hours | SAM often needs to pull data from discovery tools (SCCM, Jamf, etc.). |
| 9 | **ServiceNow Discovery** | ServiceNow (Now Learning) | Free* | 12–16 hours | Automated asset discovery — populates CMDB without manual entry. |
| 10 | **ServiceNow Service Mapping** | ServiceNow (Now Learning) | Free* | 8–12 hours | Maps service dependencies. Advanced, requires CMDB foundation. |

---

### Phase 4: Certification (Optional, Weeks 11+)

| Certification | Provider | Cost | Prerequisites | When to Take |
|---------------|----------|------|---------------|--------------|
| **Certified System Administrator (CSA)** | ServiceNow | ~$250 | Phase 1–2 knowledge | After Phase 1–2 |
| **Certified Application Developer (CAD)** | ServiceNow | ~$250 | CSA recommended | After Phase 1–3 |
| **IT Asset Management Specialist** | ServiceNow | ~$250 | CSA + SAM experience | After Phase 2–3 |

---

## Free / Alternative Learning Resources

If you don't have access to ServiceNow Now Learning:

| Resource | Provider | Cost | Best For |
|----------|----------|------|----------|
| **ServiceNow Developer Portal** | ServiceNow | Free | Documentation, PDI instance, API reference |
| **ServiceNow Community** | ServiceNow | Free | Q&A, best practices, real-world scenarios |
| **ServiceNow Docs (docs.servicenow.com)** | ServiceNow | Free | Official product documentation |
| **ServiceNow on YouTube** | ServiceNow | Free | Product demos, release webinars |
| **LinkedIn Learning** | LinkedIn | Subscription (~$30/mo) | ServiceNow admin and SAM courses |
| **Udemy** | Various | $15–$20 per course | Budget-friendly SAM admin courses |
| **Coursera** | Various | Subscription | ServiceNow specialization paths |

---

## Suggested Study Schedule

| Week | Focus | Courses | Practice (PDI) |
|------|-------|---------|----------------|
| 1 | Platform navigation | Course 1 (Fundamentals) | Create users, groups, roles |
| 2 | Platform administration | Course 2 (Platform Admin) | Build UI policies, business rules |
| 3 | Forms & automation | Courses 3–4 (UI, Flow Designer) | Build a simple flow for asset requests |
| 4 | SAM basics | Course 5 (SAM Fundamentals) | Create asset categories, states |
| 5 | Software assets | Course 6 (SAM Software) | Track software licenses |
| 6 | Contracts | Course 7 (Contract Management) | Create vendor contracts |
| 7–8 | Integration | Courses 8–9 (REST, Discovery) | Connect PDI to a test API |
| 9–10 | Advanced | Course 10 (Service Mapping) | Map a simple service dependency |
| 11+ | Certification | CSA exam prep | Practice exams, review weak areas |

---

## How to Use This With the Repository

This repository contains hands-on materials that complement the courses:

| Repository Resource | Corresponds To | Use When |
|---------------------|---------------|----------|
| `opencode/guides/sam-foundation-data.md` | Course 5 (SAM Fundamentals) | Week 4 |
| `opencode/guides/sam-guided-setup.md` | Course 5 (SAM Fundamentals) | Week 4 |
| `opencode/labs/sam-asset-lifecycle.md` | Course 5–6 | Week 4–5 |
| `opencode/infographics/asset-lifecycle.svg` | Course 5 | Week 4 (visual reference) |
| `opencode/infographics/field-classification.svg` | Course 5–6 | Week 4–5 |
| `opencode/scripts/sam_concept_summarizer.py` | Any course | When you need concept clarification |
| `opencode/scripts/sam_foundation_data_audit.py` | Course 5 | Week 4 (audit your PDI) |

---

## Common Mistakes to Avoid

| Mistake | Why It Hurts | Fix |
|---------|-------------|-----|
| Skipping platform fundamentals | SAM courses assume you know tables, roles, forms | Take Courses 1–4 first |
| No PDI practice | You can't learn ServiceNow by reading only | Sign up for PDI immediately |
| Taking SAM before platform admin | You won't understand roles, data policies, UI policies | Follow the order above |
| Ignoring certification | CSA validates your skills to employers | Consider after Phase 1–2 |

---

## Quick Reference: Course Order Summary

```
Phase 1 (Platform):     Fundamentals → Platform Admin → UI Building → Flow Designer
Phase 2 (SAM):          SAM Fundamentals → SAM Software → Contract Management
Phase 3 (Advanced):     Integrations → Discovery → Service Mapping
Phase 4 (Cert):         CSA → CAD → ITAM Specialist
```

**Total estimated time:** 10–14 weeks at 5–8 hours/week

---

## Links

- ServiceNow Now Learning: https://nowlearning.servicenow.com
- ServiceNow Developer Program: https://developer.servicenow.com
- ServiceNow Documentation: https://docs.servicenow.com
- ServiceNow Community: https://community.servicenow.com
- ServiceNow Certification: https://www.servicenow.com/certification
