# ServiceNow Hardware Asset Management (HAM)

**Module:** Hardware Asset Management (HAM)  
**Category:** Asset Management  
**Certification Path:** ServiceNow Certified Implementation Specialist – Hardware Asset Management (CIS-HAM)  
**Author:** Kilo AI Agent  
**Date:** 2026-11-05  
**Repository:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM  
**Branch:** kilo-2026-11-05-sam-modules

---

## 1. Overview

ServiceNow Hardware Asset Management (HAM) is a comprehensive solution for managing hardware assets throughout their lifecycle - from procurement to disposal. HAM helps organizations track, manage, and optimize their hardware assets while reducing costs and ensuring compliance.

### Core Value Proposition

- **Asset Lifecycle Management** - Track assets from procurement to disposal
- **Asset Inventory** - Maintain accurate inventory of all hardware assets
- **Cost Management** - Track hardware costs and optimize spending
- **Compliance Management** - Ensure compliance with software and hardware licenses
- **Procurement Management** - Streamline hardware procurement processes
- **Disposal Management** - Manage asset disposal and decommissioning

---

## 2. Key Table Hierarchy

HAM relies on the following core tables:

| Table Name | Table Name (sys_db_object) | Description | Key Fields |
|------------|---------------------------|-------------|------------|
| `alm_asset` | `alm_asset` | All assets | `name`, `asset_tag`, `serial_number`, `model`, `location`, `status`, `assigned_to`, `purchase_date`, `cost` |
| `alm_hardware` | `alm_hardware` | Hardware assets | `name`, `serial_number`, `asset_tag`, `model`, `location`, `status`, `assigned_to`, `ip_address`, `mac_address` |
| `alm_software` | `alm_software` | Software assets | `name`, `version`, `manufacturer`, `license_type`, `license_count`, `installed_count` |
| `alm_license` | `alm_license` | Software licenses | `name`, `license_type`, `entitlement_count`, `allocated_count`, `compliance_status` |
| `cmdb_ci` | `cmdb_ci` | Configuration items | `name`, `serial_number`, `model`, `location`, `status` |
| `cmdb_ci_computer` | `cmdb_ci_computer` | Computer CIs | `name`, `serial_number`, `asset_tag`, `os`, `os_version`, `processor`, `memory`, `disk_space` |
| `cmdb_ci_server` | `cmdb_ci_server` | Server CIs | `name`, `ip_address`, `os`, `os_version`, `processor_count`, `memory_gb`, `disk_gb` |
| `pm_purchase_order` | `pm_purchase_order` | Purchase orders | `number`, `title`, `company`, `location`, `state`, `total_cost`, `currency` |
| `pm_purchase_order_line` | `pm_purchase_order_line` | Purchase order line items | `number`, `position`, `item`, `quantity`, `unit_cost`, `total_cost` |
| `cmn_location` | `cmn_location` | Locations | `name`, `street`, `city`, `state`, `zip`, `country` |
| `cmn_department` | `cmn_department` | Departments | `name`, `manager`, `location`, `cost_center` |
| `cmn_location` | `cmn_location` | Locations | `name`, `street`, `city`, `state`, `zip`, `country` |

### Table Relationships

```
alm_asset ──┬── alm_hardware (1:1)
            └── alm_software (1:N)

alm_asset ──┬── cmdb_ci (1:N)
            └── pm_purchase_order_line (1:N)

cmdb_ci ──┬── cmdb_ci_computer (1:N)
          └── cmdb_ci_server (1:N)

cmdb_ci_computer ──┬── fm_work_order (1:N)
                   └── fm_work_order_part (1:N)

cmn_location ──┬── alm_asset (1:N)
               └── cmdb_ci (1:N)
               └── cmn_department (1:N)

cmn_department ──┬── alm_asset (1:N)
                  └── cmdb_ci (1:N)

pm_purchase_order ──┬── pm_purchase_order_line (1:N)
                    └── alm_asset (1:N)
```

---

## 3. Out-of-Box Features

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Asset Lifecycle Management** | Track assets from procurement to disposal | Manage the full asset lifecycle |
| **Asset Discovery** | Automatic discovery of hardware assets | Automatically discover hardware on the network |
| **Asset Reconciliation** | Reconcile physical assets with records | Ensure accuracy of asset data |
| **License Management** | Track software licenses and entitlements | Ensure compliance with software licenses |
| **Procurement Management** | Manage hardware procurement process | Streamline hardware purchasing |
| **Disposal Management** | Manage asset disposal and decommissioning | Properly dispose of retired assets |
| **Cost Management** | Track hardware costs and optimize spending | Monitor and reduce hardware costs |
| **Reporting & Analytics** | Asset reports and dashboards | Monitor asset performance and trends |
| **Integration Hub** | Integration with external systems | Connect HAM with other business systems |
| **Mobile Asset Management** | Mobile app for field technicians | Manage assets in the field |

---

## 4. Re-usable Code & Meta Data

### Script Includes

#### Asset Lifecycle Manager

```javascript
var SAMAssetLifecycle = Class.create();
SAMAssetLifecycle.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    transitionAssetState: function(assetSysId, newState) {
        var asset = new GlideRecord('alm_asset');
        if (!asset.get(assetSysId)) {
            return JSON.stringify({error: 'Asset not found'});
        }
        
        var oldState = asset.getValue('state');
        asset.state = newState;
        asset.update();
        
        // Create workflow record if needed
        if (newState == 'retired') {
            var retirementGr = new GlideRecord('fm_retirement');
            retirementGr.initialize();
            retirementGr.asset = assetSysId;
            retirementGr.reason = 'End of life';
            retirementGr.date = new Date().toISOString();
            retirementGr.insert();
        }
        
        return JSON.stringify({
            asset_sys_id: assetSysId,
            asset_name: asset.getValue('name'),
            old_state: oldState,
            new_state: newState,
            asset_number: asset.getValue('asset_tag')
        });
    },
    
    type: 'SAMAssetLifecycle'
});
```

#### Asset Compliance Checker

```javascript
var SAMComplianceChecker = Class.create();
SAMComplianceChecker.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    checkAssetCompliance: function(assetSysId) {
        var asset = new GlideRecord('alm_asset');
        if (!asset.get(assetSysId)) {
            return JSON.stringify({error: 'Asset not found'});
        }
        
        var complianceIssues = [];
        var complianceScore = 100;
        
        // Check if asset has required fields
        if (!asset.getValue('asset_tag')) {
            complianceIssues.push('Missing asset tag');
            complianceScore -= 20;
        }
        
        if (!asset.getValue('serial_number')) {
            complianceIssues.push('Missing serial number');
            complianceScore -= 20;
        }
        
        if (!asset.getValue('location')) {
            complianceIssues.push('Missing location');
            complianceScore -= 20;
        }
        
        if (!asset.getValue('assigned_to')) {
            complianceIssues.push('Missing assigned user');
            complianceScore -= 20;
        }
        
        if (!asset.getValue('purchase_date')) {
            complianceIssues.push('Missing purchase date');
            complianceScore -= 10;
        }
        
        if (complianceScore < 0) complianceScore = 0;
        
        var complianceStatus = 'compliant';
        if (complianceScore < 50) complianceStatus = 'non_compliant';
        else if (complianceScore < 80) complianceStatus = 'at_risk';
        
        return JSON.stringify({
            asset_sys_id: assetSysId,
            asset_name: asset.getValue('name'),
            compliance_score: complianceScore,
            compliance_status: complianceStatus,
            issues: complianceIssues
        });
    },
    
    type: 'SAMComplianceChecker'
});
```

### Business Rules

#### Asset State Change

**Name:** SAM Asset State Change  
**Table:** alm_asset  
**Type:** Before  
**Operations:** update

```javascript
(function rule(current, previous) {
    var oldState = previous.getValue('state');
    var newState = current.getValue('state');
    
    if (oldState !== newState) {
        current.comments = (current.comments || '') + '\n[SAM] Asset state changed from ' + oldState + ' to ' + newState + ' at ' + new Date().toISOString();
        
        // Auto-create retirement record when asset is retired
        if (newState == 'retired') {
            var retirementGr = new GlideRecord('fm_retirement');
            retirementGr.initialize();
            retirementGr.asset = current.getValue('sys_id');
            retirementGr.reason = 'End of life';
            retirementGr.date = new Date().toISOString();
            retirementGr.insert();
        }
        
        // Notify asset manager if asset is retired
        if (newState == 'retired') {
            var assignedTo = current.getValue('assigned_to');
            if (assignedTo) {
                var userGr = new GlideRecord('sys_user');
                if (userGr.get(assignedTo)) {
                    var notif = new GlideRecord('sys_notification');
                    notif.initialize();
                    notif.user = assignedTo;
                    notif.subject = 'Asset Retired: ' + current.getValue('name');
                    notif.message = 'Asset ' + current.getValue('name') + ' (' + current.getValue('asset_tag') + ') has been retired.';
                    notif.insert();
                }
            }
        }
    }
})(current, previous);
```

---

## 5. Integrations

HAM integrates with the following ServiceNow modules and external systems:

| Integration | Purpose | Method |
|-------------|---------|--------|
| **ServiceNow CMDB** | Configuration Item data for assets | Direct table joins |
| **ServiceNow Integration Hub** | Integration with ERP, procurement, and asset systems | REST API, MID Server |
| **ServiceNow Procurement** | Procurement workflow integration | Direct table joins |
| **ServiceNow Contract Management** | Contract and warranty management | Direct table joins |
| **ServiceNow Discovery** | Automatic discovery of hardware assets | MID Server, API |
| **ServiceNow Performance Analytics** | Asset performance and cost analytics | Performance Analytics |
| **ServiceNow Flow Designer** | Automated asset lifecycle workflows | Flow Designer actions |
| **ServiceNow Notifications** | Asset notifications and alerts | Email, SMS, Slack, Teams |
| **External ERP Systems** (SAP, Oracle, Microsoft Dynamics) | ERP integration for procurement and finance | Integration Hub, REST API |
| **External Asset Management Systems** (IBM Maximo, IBM Tivoli) | External asset management system integration | Integration Hub, REST API |
| **External Barcode/RFID Systems** | Barcode and RFID scanning for asset tracking | Integration Hub, REST API |

### Integration Example: External ERP Integration

```javascript
// Example: Sync asset data from external ERP via REST Message
var restMessage = new sn_ws.RESTMessageV2('ERP Integration', 'Get Assets');
restMessage.setStringParameter('warehouse_id', warehouseSysId);
var response = restMessage.execute();
var responseStatus = response.getStatusCode();

if (responseStatus === 200) {
    var responseData = JSON.parse(response.getBody());
    responseData.assets.forEach(function(asset) {
        var assetGr = new GlideRecord('alm_asset');
        assetGr.addQuery('serial_number', asset.serial_number);
        assetGr.query();
        if (assetGr.next()) {
            // Update existing asset
            assetGr.name = asset.name;
            assetGr.status = asset.status;
            assetGr.location = asset.location;
            assetGr.update();
        } else {
            // Create new asset
            var newAsset = new GlideRecord('alm_asset');
            newAsset.initialize();
            newAsset.name = asset.name;
            newAsset.serial_number = asset.serial_number;
            newAsset.asset_tag = asset.asset_tag;
            newAsset.location = asset.location;
            newAsset.status = asset.status;
            newAsset.insert();
        }
    });
}
```

---

## 5. Getting Started Steps

1. **Enable ServiceNow HAM application** on your instance
2. **Configure CMDB** with accurate hardware asset data
3. **Configure Integration Hub** for external ERP and procurement system integration
4. **Configure MID Server** for on-premise system connectivity
5. **Configure Asset Categories** with asset categories and models
6. **Configure Asset Locations** with asset locations
7. **Configure Asset Vendors** with vendor information
8. **Configure Performance Analytics** for asset performance dashboards
9. **Configure Flow Designer** for automated asset lifecycle workflows
10. **Configure Dashboards** for asset performance monitoring
11. **Train asset managers and administrators** on ServiceNow HAM usage

---

## 5. Related Resources

- [ServiceNow HAM Documentation](https://docs.servicenow.com/bundle/orlando-hardware-asset-management/)
- [ServiceNow ITSM Documentation](https://docs.servicenow.com/bundle/orlando-it-service-management/)
- [ServiceNow Integration Hub Documentation](https://docs.servicenow.com/bundle/orlando-integration-hub/)
- [ServiceNow Flow Designer Documentation](https://docs.servicenow.com/bundle/orlando-flow-designer/)
- [ServiceNow Performance Analytics Documentation](https://docs.servicenow.com/bundle/orlando-performance-analytics/)

---

*Generated by Kilo on 2026-11-05. Part of the ServiceNow_Learning_SAM repository at github.com/eltonaguiar/ServiceNow_Learning_SAM.*
