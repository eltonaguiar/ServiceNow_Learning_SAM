# SAM Foundation Data Audit

*Generated: 2026-11-04T23:45:56.405624+00:00*

## Summary

- Total foundation data areas: 9
- Critical (must have): 7

## Audit Checklist

| Item | Table | Critical | Description | Status |
|------|-------|----------|-------------|--------|
| Asset Categories | alm_asset_category | **CRITICAL** | Types of assets (determines form fields) | unknown |
| Asset States | alm_asset_state | **CRITICAL** | Lifecycle stages an asset can be in | unknown |
| Companies | cmn_company | **CRITICAL** | Companies you buy from or work with | unknown |
| Departments | cmn_department | **CRITICAL** | Internal departments that own assets | unknown |
| Locations | cmn_location | **CRITICAL** | Offices, warehouses, data centers where assets live | unknown |
| Users | sys_user | **CRITICAL** | Employees who are assigned assets | unknown |
| Vendors | cmn_vendor_company | **CRITICAL** | Approved vendors for purchasing assets | unknown |
| Asset Models | alm_asset_model | Optional | Specific make and model of hardware assets | unknown |
| Cost Centers | cmn_cost_center | Optional | Budget centers for cost accountability | unknown |

## Examples by Category

- **Asset Categories**: Laptop, Server, Software License, Monitor
- **Asset States**: In Stock, Ordered, Assigned, In Repair, Retired
- **Companies**: Dell Technologies, Microsoft, CDW, SHI
- **Departments**: IT, Finance, HR, Marketing
- **Locations**: New York HQ, London Office, Chicago Warehouse
- **Users**: Sarah Jenkins, Mike Chen
- **Vendors**: Dell Technologies, Insight Global, CDW
- **Asset Models**: Dell XPS 13, MacBook Pro 14", iPhone 15
- **Cost Centers**: IT-Operations, Finance-Systems

## Next Steps

1. Log into your ServiceNow instance
2. Navigate to each table listed above
3. Create any missing foundation data
4. Only then create asset records