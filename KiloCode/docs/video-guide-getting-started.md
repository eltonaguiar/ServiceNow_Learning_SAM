# Video Guide: Getting Started with ServiceNow SAM

**Agent:** Kilo  
**Date:** 2026-11-04  
**Repository:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM  

---

## Purpose

This guide curates video-based learning resources for getting started with ServiceNow SAM (Software Asset Management). Videos are ideal for visual learners who want to see the UI, click paths, and configuration steps in action before trying them in their own instance.

---

## Recommended Video Learning Path

Follow these videos in order. Each builds on the previous one.

| Order | Video Title | Provider | Length | Best For |
|-------|-------------|----------|--------|----------|
| 1 | **ServiceNow Fundamentals – Getting Started** | ServiceNow Official | ~2 hours | Absolute beginners |
| 2 | **ServiceNow Administration Fundamentals** | ServiceNow University | ~3 days (ILT) | CSA preparation |
| 3 | **ServiceNow SAM Overview** | ServiceNow | ~30 min | Understanding SAM capabilities |
| 4 | **SAM: Hardware Asset Management Overview** | ServiceNow | ~20 min | HAM basics |
| 5 | **SAM: Software License Management Overview** | ServiceNow | ~20 min | License lifecycle |
| 6 | **SAM: Procurement & Contract Management** | ServiceNow | ~20 min | Purchasing & contracts |
| 7 | **ServiceNow CMDB Fundamentals** | ServiceNow | ~45 min | Foundation data basics |
| 8 | **SAM: Integration Hub & Discovery** | ServiceNow | ~30 min | Connecting external data |

---

## Step-by-Step Video Guide

### Step 1: ServiceNow Fundamentals (2 hours)

**Where to find:** ServiceNow University → Learning Paths → System Administrator → Welcome to ServiceNow

**What you'll learn:**
- Navigating the ServiceNow interface
- Understanding forms, lists, and modules
- Understanding users, groups, and roles
- Creating and editing records
- Introduction to the Service Catalog

**Action item:** Complete the quiz at the end of each module. Take notes on where each major menu item lives.

---

### Step 2: ServiceNow Administration Fundamentals (3 days)

**Where to find:** ServiceNow University → Instructor-Led Training → ServiceNow Administration Fundamentals

**What you'll learn:**
- Creating and managing users, groups, and roles
- Configuring tables and fields
- Creating Business Rules, Client Scripts, and UI Policies
- Working with Update Sets
- Administering the Service Catalog

**Action item:** Complete all hands-on labs in the course. Build one custom table and one Business Rule in your Personal Developer Instance (PDI).

---

### Step 3: ServiceNow SAM Overview (20 minutes)

**Where to find:** ServiceNow University → Learning Paths → IT Asset Management → SAM Path

**What you'll learn:**
- What ServiceNow SAM is and what problems it solves
- The difference between SAM, HAM, and ITAM
- Overview of the SAM application family
- How SAM integrates with CMDB and Procurement

**Action item:** Note which SAM modules your organization already has licensed.

---

### Step 4: Hardware Asset Management Overview (20 minutes)

**Where to find:** ServiceNow University → SAM Learning Path → Hardware Asset Management

**What you'll learn:**
- Creating hardware assets
- Asset lifecycle (request → procure → deploy → maintain → retire)
- CMDB integration
- Asset relationships and dependencies

**Action item:** Create one hardware asset in your PDI and walk through its full lifecycle.

---

### Step 5: Software License Management Overview (20 minutes)

**Where to find:** ServiceNow University → SAM Learning Path → Software Asset Management

**What you'll learn:**
- Software license models and entitlements
- Allocating licenses to devices/users
- Understanding compliance and over/under-licensing
- Software normalization basics

**Action item:** Create one software license and allocate it to a test device.

---

### Step 6: Procurement & Contract Management (20 minutes)

**Where to find:** ServiceNow University → SAM Learning Path → Procurement Management

**What you'll learn:**
- Creating purchase orders
- Adding line items
- Approval workflows
- Contract creation and renewal tracking

**Action item:** Create one purchase order with two line items and route it through approval.

---

### Step 7: ServiceNow CMDB Fundamentals (45 minutes)

**Where to find:** ServiceNow University → Configuration Management Database (CMDB) Fundamentals

**What you'll learn:**
- What the CMDB is and why it matters for SAM
- Configuration Items (CIs) and relationships
- Data quality and reconciliation basics
- How SAM uses CMDB data

**Action item:** Explore the `cmdb_ci` table and create one CI manually.

---

### Step 8: Integration Hub & Discovery for SAM (30 minutes)

**Where to find:** ServiceNow University → ITOM Learning Path → Discovery Fundamentals

**What you'll learn:**
- How Discovery finds hardware and software on your network
- How Integration Hub connects to external systems
- How discovered data flows into SAM
- The difference between Discovery and manual entry

**Action item:** Review the Discovery dashboard in your instance (if Discovery is enabled).

---

## Video Learning Schedule (2-Week Sprint)

| Day | Topic | Video | Time |
|-----|-------|-------|------|
| Day 1 | ServiceNow Fundamentals | Welcome to ServiceNow | 2 hours |
| Day 2 | ServiceNow Administration Fundamentals | Part 1: Users, Groups, Roles | 2 hours |
| Day 3 | ServiceNow Administration Fundamentals | Part 2: Tables, Forms, Business Rules | 2 hours |
| Day 4 | ServiceNow Administration Fundamentals | Part 3: UI Policies, Client Scripts, Update Sets | 2 hours |
| Day 5 | SAM Overview + Platform Overview | SAM Overview + CMDB Fundamentals | 1 hour |
| Day 6 | Hardware Asset Management | HAM Overview + Hands-on Lab | 2 hours |
| Day 7 | Software Asset Management | SAM Overview + License Management | 2 hours |
| Day 8 | Procurement & Contracts | Procurement Management + Contract Management | 1 hour |
| Day 9 | Discovery & Integration | Discovery Basics + Integration Hub | 1 hour |
| Day 10 | Review & Practice | Review all videos, complete labs | 2 hours |

**Total time: ~14 hours over 2 weeks**

---

## Recommended YouTube Channels & Channels

| Channel | What You'll Find | Best For |
|---------|-----------------|----------|
| **ServiceNow Official** | Official training content, product demos, release notes | Official, up-to-date content |
| **ServiceNow Community** | Community webinars, customer stories, partner sessions | Real-world use cases |
| **ServNowGuy** | Practical how-to videos, tips and tricks | Practical tips for admins |
| **ServiceNow Developer** | Developer-focused scripting and integration content | Developers and technical admins |
| **ServiceNow Guru** | Quick tips, shortcuts, and lesser-known features | Quick tips and tricks |

---

## How to Take Notes While Watching

Use this template for each video:

```
Video: ____________________________________
Date: _____________________________________
Duration: __________________________________

Key concepts learned:
1. ________________________________________
2. ________________________________________
3. ________________________________________

Key terms to remember:
- ___________________: ______________________
- ___________________: ______________________

Steps I need to try in my instance:
1. ________________________________________
2. ________________________________________

Questions I still have:
1. ________________________________________
2. ________________________________________

Next video to watch: ________________________
```

---

## Common Mistakes When Learning from Videos

| Mistake | Why It's a Problem | Fix |
|---------|-------------------|-----|
| Watching without doing | You won't retain the steps | Pause the video and try each step in your PDI |
| Skipping the basics | Advanced topics won't make sense | Start with Welcome to ServiceNow, even if it feels basic |
| Not taking notes | You'll forget where things are | Use the template above for every video |
| Watching too many at once | Information overload | Limit to 2 videos per day |
| Not practicing after watching | Skills decay quickly | Practice within 24 hours of watching |

---

## Recommended Next Steps After Videos

1. **Complete the ServiceNow Administration Fundamentals course** — this is the foundation for everything else
2. **Complete the SAM Professional Fundamentals course** — SAM-specific depth
3. **Build a lab environment** — Practice everything you learned in your PDI
4. **Schedule the CSA exam** — Once you're comfortable with the fundamentals
5. **Work toward CIS-SAM** — The ultimate SAM certification goal

---

*Generated by Kilo on 2026-11-04. Part of the ServiceNow_Learning_SAM repository at github.com/eltonaguiar/ServiceNow_Learning_SAM.*
