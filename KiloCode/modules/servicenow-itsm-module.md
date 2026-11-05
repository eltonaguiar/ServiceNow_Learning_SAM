# ServiceNow IT Service Management (ITSM)

**Module:** IT Service Management (ITSM)  
**Category:** IT Service Management  
**Certification Path:** ServiceNow Certified Implementation Specialist – IT Service Management (CIS-ITSM)  
**Author:** Kilo AI Agent  
**Date:** 2026-11-05  
**Repository:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM  
**Branch:** kilo-2026-11-05-sam-modules

---

## 1. Overview

ServiceNow IT Service Management (ITSM) is the core IT service management platform that helps organizations manage IT services, incidents, problems, changes, and configurations. ITSM is the foundation of the ServiceNow platform and provides the core capabilities for IT service delivery.

### Core Value Proposition

- **Incident Management** - Restore normal service operation as quickly as possible
- **Problem Management** - Minimize the adverse impact of incidents and problems
- **Change Management** - Control the lifecycle of all changes
- **Configuration Management** - Maintain accurate information about configuration items
- **Service Level Management** - Ensure service levels are met
- **Knowledge Management** - Share knowledge across the organization
- **Service Catalog** - Provide a self-service catalog for users
- **Asset Management** - Manage IT assets throughout their lifecycle

---

## 2. Key Table Hierarchy

ITSM relies on the following core tables:

| Table Name | Table Name (sys_db_object) | Description | Key Fields |
|------------|---------------------------|-------------|------------|
| `incident` | `incident` | Incident records | `number`, `short_description`, `state`, `priority`, `assignment_group`, `assigned_to`, `category`, `subcategory`, `impact`, `urgency` |
| `problem` | `problem` | Problem records | `number`, `short_description`, `state`, `priority`, `assignment_group`, `assigned_to`, `category`, `root_cause` |
| `change_request` | `change_request` | Change requests | `number`, `short_description`, `state`, `priority`, `assignment_group`, `assigned_to`, `category`, `risk`, `implementation_date` |
| `cmdb_ci` | `cmdb_ci` | Configuration Items | `name`, `serial_number`, `model`, `location`, `status`, `asset_tag` |
| `cmdb_ci_server` | `cmdb_ci_server` | Server CIs | `name`, `ip_address`, `os`, `os_version`, `processor`, `memory` |
| `cmdb_ci_server` | `cmdb_ci_server` | Server CIs | `name`, `ip_address`, `os`, `os_version`, `processor`, `memory` |
| `task` | `task` | Base task table | `number`, `short_description`, `state`, `priority`, `assignment_group`, `assigned_to` |
| `cmn_location` | `cmn_location` | Locations | `name`, `street`, `city`, `state`, `zip`, `country` |
| `cmn_department` | `cmn_department` | Departments | `name`, `manager`, `location`, `cost_center` |
| `sys_user` | `sys_user` | Users | `user_name`, `first_name`, `last_name`, `email`, `department`, `location`, `company` |
| `cmn_location` | `cmn_location` | Locations | `name`, `street`, `city`, `state`, `zip`, `country` |

### Table Relationships

```
incident ──┬── problem (1:N)
           ├── cmdb_ci (1:N)
           └── task (1:1 inheritance)

problem ──┬── change_request (1:N)
          └── cmdb_ci (1:N)

change_request ──┬── cmdb_ci (1:N)
                 └── task (1:1 inheritance)

cmdb_ci ──┬── incident (1:N)
          └── problem (1:N)
          └── change_request (1:N)
          └── cmdb_ci_server (1:N)

cmn_location ──┬── cmdb_ci (1:N)
               └── cmn_department (1:N)

cmn_department ──┬── cmdb_ci (1:N)
                 └── sys_user (1:N)

sys_user ──┬── incident (1:N)
           └── problem (1:N)
           └── change_request (1:N)
           └── task (1:N)
```

---

## 3. Out-of-Box Features

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Incident Management** | Incident lifecycle management | Restore normal service operation quickly |
| **Problem Management** | Problem lifecycle management | Minimize impact of incidents and problems |
| **Change Management** | Change lifecycle management | Control changes to IT services |
| **Configuration Management** | Configuration Item management | Maintain accurate CMDB data |
| **Service Catalog** | Service catalog for end users | Self-service portal for users |
| **Knowledge Management** | Knowledge base for agents and users | Reduce incidents and improve self-service |
| **SLA Management** | Service Level Agreement management | Track and meet SLAs |
| **Reporting & Analytics** | ITSM reports and dashboards | Monitor ITSM performance |
| **Integration Hub** | Integration with external systems | Connect ITSM with other systems |
| **Mobile ITSM** | Mobile app for IT staff | Manage ITSM on-the-go |

---

## 4. Re-usable Code & Meta Data

### Script Includes

#### Incident Priority Calculator

```javascript
var ITSMPriorityCalculator = Class.create();
ITSMPriorityCalculator.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    calculatePriority: function(impact, urgency) {
        var priority = 5; // Default lowest priority
        
        var impactVal = parseInt(impact) || 3;
        var urgencyVal = parseInt(urgency) || 3;
        
        // Priority matrix
        if (impactVal === 1 && urgencyVal === 1) priority = 1; // Critical
        else if ((impactVal === 1 && urgencyVal === 2) || (impactVal === 2 && urgencyVal === 1)) priority = 2; // High
        else if ((impactVal === 1 && urgencyVal === 3) || (impactVal === 2 && urgencyVal === 2) || (impactVal === 3 && urgencyVal === 1)) priority = 3; // Medium
        else priority = 4; // Low
        
        return JSON.stringify({
            impact: impactVal,
            urgency: urgencyVal,
            priority: priority,
            priority_name: this.getPriorityName(priority)
        });
    },
    
    getPriorityName: function(priority) {
        var names = {
            1: 'Critical',
            2: 'High',
            3: 'Medium',
            4: 'Low',
            5: 'Lowest'
        };
        return names[priority] || 'Unknown';
    },
    
    type: 'ITSMPriorityCalculator'
});
```

#### Incident Auto-Assigner

```javascript
var ITSMAutoAssigner = Class.create();
ITSMAutoAssigner.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    autoAssignIncident: function(incidentSysId) {
        var inc = new GlideRecord('incident');
        if (!inc.get(incidentSysId)) {
            return JSON.stringify({error: 'Incident not found'});
        }
        
        var category = inc.getValue('category');
        var subcategory = inc.getValue('subcategory');
        var assignmentGroup = inc.getValue('assignment_group');
        
        // Find available technician in the assignment group with matching category
        var techGr = new GlideRecord('sys_user');
        techGr.addQuery('groups', assignmentGroup);
        techGr.addQuery('active', true);
        techGr.query();
        
        var availableTechs = [];
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
            
            if (hasCategorySkill) {
                availableTechs.push({
                    sys_id: techGr.getValue('sys_id'),
                    user_name: techGr.getValue('user_name'),
                    first_name: techGr.getValue('first_name'),
                    last_name: techGr.getValue('last_name')
                });
            }
        }
        
        if (availableTechs.length === 0) {
            return JSON.stringify({error: 'No available technicians in group'});
        }
        
        var selectedTech = availableTechs[Math.floor(Math.random() * availableTechs.length)];
        
        inc.assigned_to = selectedTech.sys_id;
        inc.state = '2'; // In Progress
        inc.update();
        
        return JSON.stringify({
            incident_number: inc.getValue('number'),
            assigned_to: selectedTech.user_name,
            assigned_to_sys_id: selectedTech.sys_id,
            assignment_group: inc.getValue('assignment_group')
        });
    },
    
    type: 'ITSMAutoAssigner'
});
```

### Business Rules

#### Incident Priority Auto-Assign

**Name:** ITSM Incident Priority Auto-Assign  
**Table:** incident  
**Type:** Before  
**Operations:** insert

```javascript
(function rule(current, previous) {
    var impact = parseInt(current.getValue('impact')) || 3;
    var urgency = parseInt(current.getValue('urgency')) || 3;
    
    var priority = 3; // Default medium
    
    if (impact === 1 && urgency === 1) priority = 1;
    else if ((impact === 1 && urgency === 2) || (impact === 2 && urgency === 1)) priority = 2;
    else if ((impact === 1 && urgency === 3) || (impact === 2 && urgency === 2) || (impact === 3 && urgency === 1)) priority = 3;
    else priority = 4;
    
    current.priority = priority;
})(current, previous);
```

---

## 5. Integrations

ITSM integrates with the following ServiceNow modules and external systems:

| Integration | Purpose | Method |
|-------------|---------|--------|
| **ServiceNow CMDB** | Configuration Item data for incidents and changes | Direct table joins |
| **ServiceNow Integration Hub** | Integration with monitoring, ticketing, and other systems | REST API, MID Server |
| **ServiceNow Flow Designer** | Automated ITSM workflows | Flow Designer actions |
| **ServiceNow Notifications** | Incident, problem, and change notifications | Email, SMS, Slack, Teams |
| **External Monitoring Systems** (Datadog, New Relic, Dynatrace, Splunk) | Incident creation from monitoring alerts | Integration Hub, REST API |
| **External Ticketing Systems** (Jira, Zendesk, ServiceNow) | Ticket synchronization | Integration Hub, REST API |
| **External Communication** (Email, Phone, Chat) | Incident communication and updates | Integration Hub, REST API |
| **External Monitoring Systems** (Prometheus, Grafana, Zabbix) | Metrics and alert integration | Integration Hub, REST API |
| **ServiceNow Mobile** | Mobile ITSM for technicians | Mobile app |
| **ServiceNow Data Management** | Data quality and deduplication | Data management policies |

### Integration Example: External Monitoring Integration

```javascript
// Example: Create incident from external monitoring alert via REST Message
var restMessage = new sn_ws.RESTMessageV2('Monitoring Integration', 'Create Incident');
restMessage.setStringParameter('title', 'Server CPU High');
restMessage.setStringParameter('description', 'CPU usage is above 90% on server1.example.com');
restMessage.setStringParameter('category', 'Hardware');
restMessage.setStringParameter('priority', '2');
var response = restMessage.execute();
var responseStatus = response.getStatusCode();

if (responseStatus === 201) {
    var incidentData = JSON.parse(response.getBody());
    var incidentNumber = responseData.number;
    var incidentSysId = responseData.sys_id;
    
    // Update incident with additional details
    var inc = new GlideRecord('incident');
    inc.get(incidentSysId);
    inc.description = 'Server CPU usage is above 90% on server1.example.com. Please investigate.';
    inc.category = 'Hardware';
    inc.priority = '2';
    inc.update();
}
```

---

## 5. Getting Started Steps

1. **Enable ServiceNow ITSM application** on your instance
2. **Configure CMDB** with accurate CI data
3. **Configure Integration Hub** for external monitoring and ticketing system integration
4. **Configure MID Server** for on-premise system connectivity
5. **Configure Incident Categories** with incident categories and subcategories
6. **Configure Problem Categories** with problem categories
7. **Configure Change Models** with change models and workflows
8. **Configure Performance Analytics** for ITSM dashboards
9. **Configure Flow Designer** for automated ITSM workflows
10. **Configure Dashboards** for ITSM performance monitoring
11. **Train IT staff** on ServiceNow ITSM usage

---

## 5. Related Resources

- [ServiceNow ITSM Documentation](https://docs.servicenow.com/bundle/orlando-it-service-management/)
- [ServiceNow Integration Hub Documentation](https://docs.servicenow.com/bundle/orlando-integration-hub/)
- [ServiceNow Flow Designer Documentation](https://docs.servicenow.com/bundle/orlando-flow-designer/)
- [ServiceNow Performance Analytics Documentation](https://docs.servicenow.com/bundle/orlando-performance-analytics/)

---

*Generated by Kilo on 2026-11-05. Part of the ServiceNow_Learning_SAM repository at github.com/eltonaguiar/ServiceNow_Learning_SAM.*
