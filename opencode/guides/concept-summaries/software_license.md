# Software License — SAM Concept Summary

*Generated: 2026-11-04T23:29:31.035805+00:00*
*Table: alm_software*

## ELI5 (Explain Like I'm 5)

A software license is like a permission slip that says how many copies of a program your company is allowed to use. If you have 50 licenses but 60 people using the software, you're breaking the rules.

## Technical Detail

Software licenses are tracked in the alm_software table with fields for license count, installation count, license type, and expiration date. License reconciliation compares installations to entitlements.

## Where to Find It in ServiceNow

Asset Management > Software > All

## Key Terminology

| Term | Definition |
|------|------------|
| License Count | How many copies you're allowed to use |
| Installation Count | How many copies are actually installed |
| Compliance | Installation count <= License count |

## Suggested Next Steps

1. Create a software license record
2. Run license reconciliation
3. Identify over-licensed and under-licensed software

---
