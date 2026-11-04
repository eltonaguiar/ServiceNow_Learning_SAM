# SAM Module Framework

## Module Overview

ServiceNow SAM (Service Asset Management) tracks the full lifecycle of IT assets — from request to retirement — across hardware, software, contracts, and cloud resources.

## Core Tables

| Table | Purpose | Key Fields |
|-------|---------|------------|
| `alm_asset` | Core asset record | number, category, state, assigned_to, asset_tag |
| `alm_asset_category` | Asset categories | name, parent, active |
| `alm_asset_state` | Lifecycle states | name, sequence, default |
| `alm_vendor` | Vendors/suppliers | name, contact, email |
| `alm_hardware` | Hardware-specific fields | serial_number, mac_address, warranty_expiration |
| `alm_software` | Software-specific fields | license_count, installation_count |
| `alm_contract` | Maintenance/support contracts | start_date, end_date, renewal_date |
| `alm_asset_model` | Asset models | name, manufacturer, category |

## Module Relationships

```
Asset → Category (many-to-one)
Asset → Vendor (many-to-one)
Asset → Assigned To (many-to-one, User)
Asset → Model (many-to-one)
Contract → Vendor (many-to-one)
Software Installation → Asset (many-to-one)
Software Installation → License (many-to-one)
```

## Module Prerequisites

- ITIL role for asset managers
- Admin role for configuration
- CMDB partially populated (for discovered assets)
- Procurement process defined
- Vendor records created

## Integration Points

| Integration | Purpose |
|-------------|---------|
| Discovery (MID Server) | Automatically find servers, computers, network devices |
| Procurement | Convert purchase orders to asset records |
| CMDB | Link assets to services and business impacts |
| Contract Management | Track warranty and support expirations |
| Mobile | Scan asset tags with mobile devices |
