# SAM Guided Setup — Checklist & Prerequisites

## What is Guided Setup?

Guided Setup is ServiceNow's built-in checklist. When you activate SAM, it tells you exactly what you need to configure before assets can be tracked properly. Think of it as a "to-do list" that ServiceNow generates for you.

## Prerequisites (Do These First)

Before starting SAM Guided Setup, make sure you have:

- [ ] **ITIL role** — Required to create and manage assets
- [ ] **Admin access** — Needed to configure categories and states
- [ ] **Asset categories defined** — At minimum: Hardware, Software
- [ ] **Procurement process** — Know how your company buys assets
- [ ] **Vendor records** — Companies you buy from (Dell, Microsoft, etc.)

## Guided Setup Checklist

| # | Setup Item | Type | Why It Matters | Done |
|---|-----------|------|----------------|------|
| 1 | Define asset categories | **CRITICAL** | Determines what fields appear on each asset | [ ] |
| 2 | Set up asset states | **CRITICAL** | In Stock, Assigned, In Repair, Retired | [ ] |
| 3 | Create vendor records | **Mandatory** | Who you buy assets from | [ ] |
| 4 | Configure asset procurement | **Mandatory** | How purchase requests become assets | [ ] |
| 5 | Set up asset lifecycle | **Mandatory** | Rules for moving assets between states | [ ] |
| 6 | Create asset models | **Optional** | Specific models (Dell XPS 13, iPhone 15) | [ ] |
| 7 | Configure software licenses | **Optional** | Track licensed software | [ ] |
| 8 | Set up contract management | **Optional** | Track maintenance and support contracts | [ ] |
| 9 | Integrate with discovery | **Critical** | Automatically find servers and computers | [ ] |
| 10| Configure asset retirement | **Optional** | Rules for disposing of old assets | [ ] |

## Mandatory vs Optional vs Critical

| Type | Meaning | Example in SAM |
|------|---------|----------------|
| **Critical** | Asset tracking won't work without it | Asset categories, Asset tag |
| **Mandatory** | Required for normal daily work | Procurement process, Assigned To |
| **Optional** | Nice to have, works without it | Software licenses, Contracts |

## Where to Find Guided Setup in ServiceNow

1. Navigate to **Asset Management > Administration > Guided Setup**
2. Or search "Guided Setup" in the navigation bar
3. Each item has a status: Not Started / In Progress / Complete
4. Click an item to go directly to its configuration page

## Common Setup Mistakes

| Mistake | Result | Fix |
|---------|--------|-----|
| Skipping asset categories | Can't create assets | Define categories first |
| Not setting asset states | Assets stuck in "In Stock" forever | Configure state transitions |
| Missing vendor records | Can't record who you bought from | Add vendors before receiving assets |
| No asset tag format | Duplicate or confusing tag numbers | Define a standard tag format (e.g., AST-#####) |
