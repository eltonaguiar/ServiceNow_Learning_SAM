# SAM — Mandatory vs Critical vs Optional Fields

## Quick Reference

| Field | Type | Why It's Critical/Mandatory/Optional |
|-------|------|--------------------------------------|
| Asset Tag | Critical | Unique physical identifier; without it you can't find the asset in the real world |
| Category | Critical | Determines which fields appear on the form |
| State | Critical | Tells you where the asset is in its lifecycle |
| Number | Critical | System-generated unique identifier |
| Name | Mandatory | Human-readable identifier |
| Purchase Date | Mandatory | Needed for warranty, depreciation, replacement planning |
| Assigned To | Mandatory | Accountability — who has the asset |
| Vendor | Mandatory | Who to contact for support/warranty |
| Serial Number | Critical | Links to manufacturer warranty and support |
| Cost | Optional | Useful for budgeting, not required |
| Location | Optional | Physical whereabouts |
| Pool | Optional | Grouping similar assets together |
| MAC Address | Optional | Network identification |
| Contract Reference | Critical (if leased) | Links asset to support contract |

## Decision Tree: Is This Field Critical?

```
Is it auto-generated? → Yes → Critical (Number)
                    → No → Is it needed to physically identify the asset?
                             → Yes → Critical (Asset Tag, Serial Number)
                             → No → Is it needed for daily operations?
                                      → Yes → Mandatory (Name, Assigned To, Purchase Date)
                                      → No → Optional (Cost, Location, Pool)
```
