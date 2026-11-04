# Asset Lifecycle — SAM Concept Summary

*Generated: 2026-11-04T23:29:38.016852+00:00*
*Table: alm_asset*

## ELI5 (Explain Like I'm 5)

An asset lifecycle is like the life of a laptop: someone asks for it, you buy it, it arrives, you give it to an employee, you fix it when it breaks, and eventually you replace it and recycle the old one.

## Technical Detail

The asset lifecycle is tracked through the 'state' field on the alm_asset table. States typically include: In Stock, Ordered, Assigned, In Repair, Retired, and Disposed. Transitions between states can be controlled by business rules.

## Where to Find It in ServiceNow

Asset Management > Assets > All > State field

## Key Terminology

| Term | Definition |
|------|------------|
| Asset Lifecycle | The journey from request to retirement |
| State | Current position in the lifecycle |
| Asset Tag | Unique physical identifier |

## Suggested Next Steps

1. Create an asset and move it through all states
2. Set up state transition rules
3. Create a report showing assets by state

---
