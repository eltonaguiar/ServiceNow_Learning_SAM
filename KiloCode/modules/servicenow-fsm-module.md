# ServiceNow Field Service Management (FSM)

**Module:** Field Service Management (FSM)  
**Category:** Field Service Management  
**Certification Path:** ServiceNow Certified Implementation Specialist – Field Service Management (CIS-FSM)  
**Author:** Kilo AI Agent  
**Date:** 2026-11-05  
**Repository:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM  
**Branch:** kilo-2026-11-05-sam-modules

---

## 1. Overview

ServiceNow Field Service Management (FSM) is a comprehensive field service solution that helps organizations manage field service operations, including work order management, workforce scheduling, inventory management, and customer communication.

### Core Value Proposition

- **Work order management** from creation to completion
- **Workforce management** with intelligent scheduling and dispatch
- **Inventory management** with parts and inventory tracking
- **Mobile field service** with mobile app for field technicians
- **Customer communication** with automated notifications and updates
- **Performance analytics** with field service KPIs and dashboards

---

## 2. Key Table Hierarchy

FSM relies on the following core tables:

| Table Name | Table Name (sys_db_object) | Description | Key Fields |
|------------|---------------------------|-------------|------------|
| `fm_work_order` | `fm_work_order` | Field service work orders | `number`, `short_description`, `state`, `priority`, `assigned_to`, `assignment_group`, `location`, `start_time`, `end_time` |
| `fm_work_order_task` | `fm_work_order_task` | Work order tasks | `number`, `short_description`, `state`, `priority`, `assignment_group`, `assigned_to`, `parent` |
| `fm_work_order_template` | `fm_work_order_template` | Work order templates | `name`, `description`, `category`, `active` |
| `fm_service_contract` | `fm_service_contract` | Service contracts | `number`, `name`, `start_date`, `end_date`, `customer`, `status`, `value` |
| `fm_service_agreement` | `fm_service_agreement` | Service agreements | `name`, `customer`, `start_date`, `end_date`, `service_level`, `status` |
| `fm_asset` | `fm_asset` | Field service assets | `name`, `serial_number`, `asset_tag`, `model`, `location`, `status` |
| `fm_inventory_item` | `fm_inventory_item` | Inventory items | `name`, `quantity`, `location`, `status`, `reorder_point` |
| `fm_work_order_part` | `fm_work_order_part` | Work order parts | `work_order`, `item`, `quantity`, `status` |
| `cmdb_ci` | `cmdb_ci` | Configuration items | `name`, `serial_number`, `model`, `location`, `status` |
| `task` | `task` | Base task table | `number`, `short_description`, `state`, `priority`, `assignment_group`, `assigned_to` |
| `cmn_location` | `cmn_location` | Locations | `name`, `street`, `city`, `state`, `zip`, `country` |

### Table Relationships

```
fm_work_order ──┬── fm_work_order_task (1:N)
                ├── fm_work_order_part (1:N)
                └── task (1:1 inheritance)

fm_service_contract ──┬── fm_work_order (1:N)
                      └── fm_service_agreement (1:N)

cmdb_ci ──┬── fm_work_order (1:N)
          └── fm_work_order_part (1:N)

cmn_location ──┬── fm_work_order (1:N)
               └── fm_work_order_task (1:N)

cmn_location ──┬── fm_asset (1:N)
               └── fm_inventory_item (1:N)

fm_asset ──┬── fm_work_order (1:N)
           └── fm_work_order_part (1:N)
```

---

## 3. Out-of-Box Features

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Work Order Management** | Complete work order lifecycle management | Create, assign, track, and close work orders |
| **Workforce Management** | Technician scheduling and dispatch | Assign the right technician to the right job |
| **Inventory Management** | Parts and inventory management | Track parts inventory and usage |
| **Mobile Field Service** | Mobile app for field technicians | Field technicians can update work orders in the field |
| **Customer Communication** | Automated notifications and updates | Keep customers informed throughout service process |
| **Performance Analytics** | Field service KPIs and dashboards | Track field service performance |
| **Integration Hub** | Integration with external systems (ERP, CRM, etc.) | Connect FSM with other business systems |
| **Scheduling Assistant** | Intelligent scheduling assistant | Optimize technician schedules |
| **Map View** | Map-based view of field technicians and jobs | Visualize field service operations |
| **Time Tracking** | Time tracking for field technicians | Track time spent on work orders |

---

## 4. Re-usable Code & Meta Data

### Script Includes

#### FSM Work Order Manager

```javascript
var FSMWorkOrderManager = Class.create();
FSMWorkOrderManager.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    createWorkOrder: function(title, description, company, location, priority, category) {
        var wo = new GlideRecord('fm_work_order');
        wo.initialize();
        wo.short_description = title;
        wo.description = description;
        wo.company = company;
        wo.location = location;
        wo.priority = priority;
        wo.category = category;
        wo.state = '1'; // Draft
        var sysId = wo.insert();
        
        return JSON.stringify({
            number: wo.getValue('number'),
            sys_id: wo.getValue('sys_id'),
            title: wo.getValue('short_description'),
            state: wo.getValue('state')
        });
    },
    
    assignWorkOrder: function(workOrderSysId, technicianSysId) {
        var wo = new GlideRecord('fm_work_order');
        if (!wo.get(workOrderSysId)) {
            return JSON.stringify({error: 'Work order not found'});
        }
        
        wo.assigned_to = technicianSysId;
        wo.state = '2'; // Dispatched
        wo.update();
        
        return JSON.stringify({
            work_order_number: wo.getValue('number'),
            assigned_to: technicianSysId,
            state: wo.getValue('state')
        });
    },
    
    type: 'FSMWorkOrderManager'
});
```

#### FSM Scheduling Assistant

```javascript
var FSMSchedulingAssistant = Class.create();
FSMSchedulingAssistant.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    findAvailableTechnicians: function(workOrderSysId, date, duration) {
        var wo = new GlideRecord('fm_work_order');
        if (!wo.get(workOrderSysId)) {
            return JSON.stringify({error: 'Work order not found'});
        }
        
        var location = wo.getValue('location');
        var category = wo.getValue('category');
        
        // Find technicians with matching skills and availability
        var techGr = new GlideRecord('sys_user');
        techGr.addQuery('groups', 'field_technicians');
        techGr.addQuery('active', true);
        techGr.query();
        
        var availableTechs = [];
        while (techGr.next()) {
            var techId = techGr.getValue('sys_id');
            
            // Check if technician has required skills
            var skillsGr = new GlideRecord('sys_user_has_skill');
            skillsGr.addQuery('user', techId);
            skillsGr.query();
            var hasRequiredSkill = false;
            while (skillsGr.next()) {
                var skillGr = new GlideRecord('cmn_skill');
                if (skillGr.get(skillsGr.skill)) {
                    if (skillGr.name == category) {
                        hasRequiredSkill = true;
                        break;
                    }
                }
            }
            
            if (hasRequiredSkill) {
                availableTechs.push({
                    sys_id: techGr.getValue('sys_id'),
                    user_name: techGr.getValue('user_name'),
                    first_name: techGr.getValue('first_name'),
                    last_name: techGr.getValue('last_name')
                });
            }
        }
        
        return JSON.stringify({
            work_order_sys_id: workOrderSysId,
            available_technicians: availableTechs,
            total_available: availableTechs.length
        });
    },
    
    type: 'FSMSchedulingAssistant'
});
```

### Business Rules

#### Work Order Auto-Assign

**Name:** FSM Work Order Auto-Assign  
**Table:** fm_work_order  
**Type:** Before  
**Operations:** insert

```javascript
(function rule(current, previous) {
    var location = current.getValue('location');
    var category = current.getValue('category');
    
    if (!location || !category) return;
    
    // Find technicians in the same location with matching category
    var techGr = new GlideRecord('sys_user');
    techGr.addQuery('groups', 'field_technicians');
    techGr.addQuery('active', true);
    techGr.query();
    
    var bestMatch = null;
    var bestScore = 0;
    
    while (techGr.next()) {
        var techId = techGr.getValue('sys_id');
        
        // Check skills
        var skillsGr = new GlideRecord('sys_user_has_skill');
        skillsGr.addQuery('user', techId);
        skillsGr.query();
        var hasCategorySkill = false;
        while (skillsGr.next()) {
            var skillGr = new GlideRecord('cmn_skill');
            if (skillGr.get(skillsGr.skill)) {
                if (skillGr.name == category) {
                    hasCategorySkill = true;
                    break;
                }
            }
        }
        
        if (!hasCategorySkill) continue;
        
        var score = 1;
        
        // Bonus for same location
        if (techGr.getValue('location') == location) {
            score += 10;
        }
        
        if (score > bestScore) {
            bestScore = score;
            bestMatch = techGr.getValue('sys_id');
        }
    }
    
    if (bestMatch) {
        current.assigned_to = bestMatch;
        current.assignment_group = techGr.getValue('groups');
        current.state = '2'; // Dispatched
    }
})(current, previous);
```

---

## 5. Integrations

FSM integrates with the following ServiceNow modules and external systems:

| Integration | Purpose | Method |
|-------------|---------|--------|
| **ServiceNow CMDB** | Configuration Item data for field assets | Direct table joins |
| **ServiceNow Integration Hub** | Integration with ERP, CRM, and other systems | REST API, MID Server |
| **ServiceNow Field Service Mobile App** | Mobile app for field technicians | Mobile app |
| **ServiceNow Performance Analytics** | Field service performance analytics | Performance Analytics |
| **ServiceNow Flow Designer** | Automated field service workflows | Flow Designer actions |
| **ServiceNow Notifications** | Customer and technician notifications | Email, SMS, Slack, Teams |
| **External ERP Systems** (SAP, Oracle, Microsoft Dynamics) | ERP integration for parts and inventory | Integration Hub, REST API |
| **External CRM Systems** (Salesforce, Microsoft Dynamics) | Customer data synchronization | Integration Hub, REST API |
| **External GPS Systems** (Google Maps, Google Maps Platform) | Location and routing integration | Integration Hub, REST API |
| **External IoT Systems** (IoT sensors, devices) | IoT device integration | Integration Hub, REST API |

### Integration Example: External ERP Parts Integration

```javascript
// Example: Sync parts inventory from external ERP via REST Message
var restMessage = new sn_ws.RESTMessageV2('ERP Integration', 'Get Parts Inventory');
restMessage.setStringParameter('warehouse_id', warehouseSysId);
var response = restMessage.execute();
var responseStatus = response.getStatusCode();

if (responseStatus === 200) {
    var responseData = JSON.parse(response.getBody());
    // Process and update inventory items
    responseData.items.forEach(function(item) {
        var itemGr = new GlideRecord('fm_inventory_item');
        itemGr.addQuery('name', item.part_number);
        itemGr.query();
        if (itemGr.next()) {
            itemGr.quantity_on_hand = item.quantity;
            itemGr.update();
        } else {
            var newItem = new GlideRecord('fm_inventory_item');
            newItem.initialize();
            newItem.name = item.part_number;
            newItem.quantity_on_hand = item.quantity;
            newItem.location = item.warehouse_location;
            newItem.insert();
        }
    });
}
```

---

## 5. Getting Started Steps

1. **Enable ServiceNow FSM application** on your instance
2. **Configure CMDB** with accurate asset and configuration item data
3. **Configure Integration Hub** for external ERP and CRM system integration
4. **Configure MID Server** for on-premise system connectivity
5. **Configure Field Service Mobile App** for field technicians
6. **Configure Work Order Templates** with standard work order templates
7. **Configure Inventory Management** with parts and inventory data
8. **Configure Performance Analytics** for field service dashboards
9. **Configure Flow Designer** for automated field service workflows
10. **Configure Dashboards** for field service performance monitoring
11. **Train technicians and dispatchers** on ServiceNow FSM usage

---

## 5. Related Resources

- [ServiceNow FSM Documentation](https://docs.servicenow.com/bundle/orlando-field-service-management/)
- [ServiceNow ITSM Documentation](https://docs.servicenow.com/bundle/orlando-it-service-management/)
- [ServiceNow Integration Hub Documentation](https://docs.servicenow.com/bundle/orlando-integration-hub/)
- [ServiceNow Flow Designer Documentation](https://docs.servicenow.com/bundle/orlando-flow-designer/)
- [ServiceNow Performance Analytics Documentation](https://docs.servicenow.com/bundle/orlando-performance-analytics/)

---

*Generated by Kilo on 2026-11-05. Part of the ServiceNow_Learning_SAM repository at github.com/eltonaguiar/ServiceNow_Learning_SAM.*
