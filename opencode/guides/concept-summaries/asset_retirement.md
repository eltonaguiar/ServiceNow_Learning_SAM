# Asset Retirement — SAM Concept Summary

*Generated: 2026-11-04T23:29:38.042614+00:00*
*Table: alm_asset*

## ELI5 (Explain Like I'm 5)

Asset retirement is when you decide an asset is too old or broken to keep using. You wipe its data, mark it as retired in ServiceNow, and either recycle it, donate it, or return it to the vendor.

## Technical Detail

Asset retirement sets the alm_asset state to 'Retired' and records the retirement date and disposal method. The asset remains in the database for historical reporting but is no longer active.

## Where to Find It in ServiceNow

Asset Management > Assets > All > State = Retired

## Key Terminology

| Term | Definition |
|------|------------|
| Retirement Date | When the asset was taken out of service |
| Disposal Method | How it was disposed (recycle, donate, return) |

## Suggested Next Steps

1. Retire an old asset
2. Create a retirement report
3. Set up automatic retirement alerts

---
