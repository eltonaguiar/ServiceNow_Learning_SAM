# Video Guide: Getting Started with ServiceNow SAM

**Format:** Screen-captured walkthrough + voiceover  
**Target audience:** ServiceNow Admins / Asset Managers  
**Estimated runtime:** 12–15 minutes  
**Methodology:** SNRLM (ServiceNow Rapid Learning Methodology) — Step 1: Decompose → Step 2: ELI5 → Step 3: Hands-on lab

---

## Part 1: Script & Storyboard

### Opening (0:00–0:30)
**Visual:** ServiceNow logo, then split screen: left side = SAM Workspace, right side = "What is SAM?"

**Voiceover:**
> "Software Asset Management in ServiceNow isn't just about tracking what you have. It's about building a licence position you can defend in an audit. If you're just tracking installs, you're doing asset management, not SAM. In this 12-minute video, we'll walk through the three hard gates that make SAM data trustworthy."

### The Three Hard Gates (0:30–2:30)
**Visual:** Animated diagram: Gate 1 (Schema), Gate 2 (CMDB), Gate 3 (Discovery Feed)

**Voiceover:**
> "SAM has three hard gates. If you miss any of these, every number you produce is fiction. First: SAM schema and entitlement. You need the SAM plugin and the right entitlement tables. Second: CMDB populated with identification rules. Duplicate CIs mean duplicate installs, which means inflated gaps. Third: A discovery or connector feed. Hand-typed installs are an asset register, not SAM."

### The Build Order (2:30–5:00)
**Visual:** Checklist animation: Plugin -> Guided Setup -> Roles -> Feed -> Normalisation -> Entitlements -> Metrics -> Reconciliation

**Voiceover:**
> "Do not reorder these steps. Each one assumes the previous checkpoint. Start by installing the plugin. Run Guided Setup — read every step before clicking. Set up a dedicated integration user. Then, connect one discovery feed. Once data flows, focus on normalisation. Only then do you load entitlements and define your licence metrics."

### Identification Rules: CMDB vs SAM (5:00–7:30)
**Visual:** Comparison table: CI Identification (IRE) vs SAM Normalisation

**Voiceover:**
> "The most common mistake? Confusing CI identification with SAM normalisation. CI identification rules are for the CMDB — they stop you from having three assets for one laptop. SAM normalisation is for software titles — it maps 'Microsoft Office 2021' and 'MS Office 21' to the same product. Fix your CMDB identification first, or you'll spend a week explaining a shortage that's really just a duplicate CI."

### Fields That Decide the Answer (7:30–10:00)
**Visual:** Highlighted form fields: Entitlement (Metric), Install (Normalised Product), Asset (Model)

**Voiceover:**
> "Which fields actually matter? For Entitlements, it's the Metric — per user, per device, or per core? That's a commercial decision, not a technical one. For Installs, it's the Normalised Product. If that's empty, your reconciliation report is empty. And for Assets, it's the Model. If your model is wrong, your licence metric won't apply correctly."

### Metrics That Lie (10:00–11:30)
**Visual:** Table: Metric vs Caution

**Voiceover:**
> "Be careful with metrics. 'Unlicensed installs' alone is just fear without context. 'Raw install count' as usage is a trap — installed does not mean used. Your best first KPI? 'Installs without a normalised product'. If that number is high, your SAM program is effectively offline."

### Closing (11:30–12:30)
**Visual:** Recap screen with next steps

**Voiceover:**
> "You've seen the gates, the build order, and the traps. Now, go to the lab. Build a real compliance number for three titles. Then break it by changing the metric and watch the answer flip. That's the moment SAM becomes a business conversation."

**On-screen next steps:**
- [ ] Run the SAM readiness probe (`scripts/sam_readiness.py`)
- [ ] Fix your CMDB identification rules
- [ ] Complete Lab 03 (SAM Baseline)
- [ ] Read the SAM methodology in the repo

---

## Part 2: Production Checklist

| Item | Status | Notes |
|------|--------|-------|
| Script written | ✅ | This document |
| Storyboard sketched | ⬜ | Map each script section to visuals |
| Instance ready | ⬜ | Use developer.servicenow.com |
| Screen recorder selected | ⬜ | OBS Studio, Loom, or Camtasia |
| Video recorded | ⬜ | 12–15 min target |
| Video edited | ⬜ | Add captions, callouts, zooms |
| Uploaded to platform | ⬜ | YouTube, Vimeo, or internal |
| Linked in README | ⬜ | Add link to repo README |
