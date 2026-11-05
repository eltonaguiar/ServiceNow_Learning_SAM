# ServiceNow Customer Service Management (CSM)

**Module:** Customer Service Management (CSM)  
**Category:** Customer Service Management  
**Certification Path:** ServiceNow Certified Implementation Specialist – Customer Service Management (CIS-CSM)  
**Author:** Kilo AI Agent  
**Date:** 2026-11-05  
**Repository:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM  
**Branch:** kilo-2026-11-05-sam-modules

---

## 1. Overview

ServiceNow Customer Service Management (CSM) is a comprehensive customer service solution that helps organizations deliver exceptional customer service across all channels. CSM connects customer service with other departments (operations, finance, legal, HR) to resolve customer issues faster and more efficiently.

### Core Value Proposition

- **Omnichannel support** across email, phone, chat, chatbot, social media, and self-service
- **Case management** with intelligent routing and automation
- **Knowledge management** for self-service and agent assistance
- **Customer 360 view** with complete customer context and history
- **Proactive service** with predictive insights and automated workflows
- **Omnichannel routing** with skills-based routing and workload balancing

---

## 2. Key Table Hierarchy

CSM relies on the following core tables:

| Table Name | Table Name (sys_db_object) | Description | Key Fields |
|------------|---------------------------|-------------|------------|
| `sn_customerservice_case` | `sn_customerservice_case` | Customer service cases | `number`, `short_description`, `state`, `priority`, `category`, `subcategory`, `contact`, `company`, `assigned_to`, `assignment_group` |
| `sn_customerservice_case_task` | `sn_customerservice_case_task` | Case tasks for multi-step resolution | `number`, `short_description`, `state`, `priority`, `assignment_group`, `assigned_to`, `parent` |
| `sn_customerservice_case_workflow` | `sn_customerservice_case_workflow` | Case workflow definitions | `name`, `case_table`, `workflow`, `active` |
| `sn_customerservice_case_routing` | `sn_customerservice_case_routing` | Case routing rules | `name`, `condition`, `assignment_group`, `assigned_to` |
| `sn_customerservice_customer` | `sn_customerservice_customer` | Customer records | `first_name`, `last_name`, `email`, `phone`, `company`, `account` |
| `sn_customerservice_account` | `sn_customerservice_account` | Customer accounts | `name`, `account_number`, `industry`, `size`, `region`, `status` |
| `sn_customerservice_knowledge` | `sn_customerservice_knowledge` | Customer service knowledge articles | `short_description`, `knowledge_base`, `category`, `workflow_state`, `view_count` |
| `sn_customerservice_contract` | `sn_customerservice_contract` | Customer contracts | `number`, `name`, `start_date`, `end_date`, `customer`, `status`, `value` |
| `sn_customerservice_entitlement` | `sn_customerservice_entitlement` | Service entitlements | `name`, `customer`, `start_date`, `end_date`, `entitlement_type`, `response_time`, `resolution_time` |
| `sn_customerservice_survey` | `sn_customerservice_survey` | Customer satisfaction surveys | `case`, `score`, `comment`, `response_date` |
| `cmdb_ci_service` | `cmdb_ci_service` | Service CI records | `name`, `category`, `owned_by`, `supported_by` |
| `task` | `task` | Base task table (parent of incident, change, problem, case) | `number`, `short_description`, `state`, `priority`, `assignment_group`, `assigned_to` |

### Table Relationships

```
sn_customerservice_case ──┬── sn_customerservice_case_task (1:N)
                          ├── sn_customerservice_contract (1:1)
                          ├── sn_customerservice_entitlement (1:N)
                          ├── sn_customerservice_survey (1:N)
                          └── task (1:1 inheritance)

cmdb_ci_service ──┬── sn_customerservice_case (1:N)
                  └── sn_customerservice_case (1:N)

sn_customerservice_customer ──┬── sn_customerservice_case (1:N)
                              └── sn_customerservice_account (1:N)

sn_customerservice_account ──┬── sn_customerservice_case (1:N)
                              └── sn_customerservice_contract (1:N)
```

---

## 3. Out-of-Box Features

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Omnichannel Engagement** | Unified inbox for email, phone, chat, chatbot, social media, and self-service | Manage all customer interactions from one place |
| **Case Management** | Complete case lifecycle management from creation to resolution | Track and resolve customer issues efficiently |
| **Knowledge Management** | Knowledge base for agents and customers | Reduce case volume through self-service |
| **Case Routing** | Skills-based routing and workload balancing | Route cases to the right agent automatically |
| **Case Workflow** | Automated case lifecycle workflows | Standardize case handling processes |
| **Customer 360 View** | Unified customer profile with history and context | Provide personalized service |
| **Entitlement Management** | Manage customer service entitlements and SLAs | Enforce service level agreements |
| **Knowledge Management** | Knowledge base for customers and agents | Enable self-service and reduce case volume |
| **Customer Feedback** | Customer satisfaction surveys and feedback collection | Measure and improve customer satisfaction |
| **Integration Hub** | Integration with external systems (CRM, ERP, etc.) | Connect CSM with other business systems |
| **Performance Analytics** | Dashboards and reports for CSM metrics | Track CSM performance and trends |

---

## 4. Re-usable Code & Meta Data

### Script Includes

#### CSM Case Automation

```javascript
var CSMCaseAutomation = Class.create();
CSMCaseAutomation.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    autoAssignCase: function(caseSysId, assignmentGroupSysId) {
        var caseGr = new GlideRecord('sn_customerservice_case');
        if (!caseGr.get(caseSysId)) {
            return JSON.stringify({error: 'Case not found'});
        }
        
        // Find available agent in the group
        var userGr = new GlideRecord('sys_user');
        userGr.addQuery('groups', assignmentGroupSysId);
        userGr.addQuery('active', true);
        userGr.addQuery('time_zone', '!=', '');
        userGr.query();
        
        var agents = [];
        while (userGr.next()) {
            agents.push({
                sys_id: userGr.getValue('sys_id'),
                user_name: userGr.getValue('user_name'),
                first_name: userGr.getValue('first_name'),
                last_name: userGr.getValue('last_name')
            });
        }
        
        if (agents.length === 0) {
            return JSON.stringify({error: 'No available agents in group'});
        }
        
        // Simple round-robin assignment (in production, use more sophisticated logic)
        var agentIndex = Math.floor(Math.random() * agents.length);
        var selectedAgent = agents[agentIndex];
        
        caseGr.assigned_to = selectedAgent.sys_id;
        caseGr.assignment_group = assignmentGroupSysId;
        caseGr.state = '2'; // In Progress
        caseGr.update();
        
        return JSON.stringify({
            assigned_to: selectedAgent.user_name,
            assigned_to_sys_id: selectedAgent.sys_id,
            assignment_group: assignmentGroupSysId,
            case_number: caseGr.getValue('number')
        });
    },
    
    type: 'CSMCaseAutomation'
});
```

#### Case Escalation Manager

```javascript
var CSMEscalationManager = Class.create();
CSMCaseEscalationManager.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    escalateCase: function(caseSysId, reason) {
        var caseGr = new GlideRecord('sn_customerservice_case');
        if (!caseGr.get(caseSysId)) {
            return JSON.stringify({error: 'Case not found'});
        }
        
        var currentPriority = parseInt(caseGr.getValue('priority')) || 3;
        var newPriority = Math.max(1, currentPriority - 1); // Escalate by increasing priority (lower number = higher priority)
        
        caseGr.priority = newPriority;
        caseGr.comments = (caseGr.comments || '') + '\n[CSM Escalation] ' + new Date().toISOString() + ': ' + reason;
        caseGr.update();
        
        // Create task for the escalation
        var taskGr = new GlideRecord('sn_customerservice_case_task');
        taskGr.initialize();
        taskGr.parent = caseSysId;
        taskGr.short_description = 'Escalation: ' + reason;
        taskGr.description = 'Case escalated due to: ' + reason + '\nOriginal case: ' + caseGr.getValue('number');
        taskGr.state = '1'; // Open
        taskGr.priority = newPriority;
        taskGr.insert();
        
        return JSON.stringify({
            case_number: caseGr.getValue('number'),
            new_priority: newPriority,
            previous_priority: currentPriority,
            task_number: taskGr.getValue('number')
        });
    },
    
    type: 'CSMCaseEscalationManager'
});
```

### Business Rules

#### Case SLA Monitor

**Name:** CSM Case SLA Monitor  
**Table:** sn_customerservice_case  
**Type:** Before  
**Operations:** insert, update

```javascript
(function rule(current, previous) {
    var SLA_THRESHOLD_HOURS = 24; // 24 hours for standard priority
    
    var createdOn = current.getValue('sys_created_on');
    var currentTime = new Date();
    var createdTime = new Date(createdOn);
    var hoursElapsed = (currentTime - createdTime) / (1000 * 60 * 60);
    
    if (hoursElapsed > SLA_THRESHOLD_HOURS && caseGr.getValue('state') != '7') { // Not resolved
        current.priority = 1; // Escalate to highest priority
        current.comments = (current.comments || '') + '\n[SLA] Case exceeded SLA threshold of ' + SLA_THRESHOLD_HOURS + ' hours at ' + new Date().toISOString();
        
        // Notify manager
        var assignmentGroup = current.getValue('assignment_group');
        if (assignmentGroup) {
            var groupGr = new GlideRecord('sys_user_group');
            if (groupGr.get(assignmentGroup)) {
                var manager = groupGr.getValue('manager');
                if (manager) {
                    // Send notification to manager
                    var notif = new GlideRecord('sys_notification');
                    notif.initialize();
                    notif.user = manager;
                    notif.subject = 'SLA Breach: Case ' + caseGr.getValue('number');
                    notif.message = 'Case ' + caseGr.getNumber() + ' has exceeded SLA threshold of ' + SLA_THRESHOLD_HOURS + ' hours.';
                    notif.insert();
                }
            }
        }
    }
})(current, previous);
```

---

## 5. Integrations

CSM integrates with the following ServiceNow modules and external systems:

| Integration | Purpose | Method |
|-------------|---------|--------|
| **ServiceNow CMDB** | Configuration Item data for service context | Direct table joins |
| **ServiceNow Knowledge Base** | Knowledge articles for self-service and agent assistance | Direct table access |
| **ServiceNow Incident Management** | Incident-case linking and escalation | Direct table relationships |
| **ServiceNow Change Management** | Change impact analysis on customer service | Change records |
| **ServiceNow Field Service Management** | Field service coordination | Integration Hub, REST API |
| **External CRM Systems** (Salesforce, Microsoft Dynamics) | Customer data synchronization | Integration Hub, REST API |
| **External Communication Channels** (Email, Phone, Chat, Social Media) | Omnichannel customer engagement | Integration Hub, REST API, MID Server |
| **External Telephony Systems** (Avaya, Cisco, Genesys) | Phone system integration | Integration Hub, REST API, MID Server |
| **External Survey Tools** (SurveyMonkey, Qualtrics) | Customer satisfaction survey integration | Integration Hub, REST API |
| **ServiceNow Flow Designer** | Automated customer service workflows | Flow Designer actions |
| **ServiceNow Notifications** | Customer and agent notifications | Email, SMS, Slack, Teams |

### Integration Example: External CRM Data Ingestion

```javascript
// Example: Ingest customer data from external CRM via REST Message
var restMessage = new sn_ws.RESTMessageV2('CRM Integration', 'Get Customer');
restMessage.setStringParameter('customer_id', customerSysId);
var response = restMessage.execute();
var responseStatus = response.getStatusCode();

if (responseStatus === 200) {
    var responseData = JSON.parse(response.getBody());
    // Process and create/update customer record
}
```

---

## 5. Getting Started Steps

1. **Enable ServiceNow CSM application** on your instance
2. **Configure CMDB** with accurate customer and service data
3. **Configure Integration Hub** for external CRM and communication channel integration
4. **Configure MID Server** for on-premise system connectivity
5. **Configure Knowledge Base** with customer self-service articles
6. **Configure Case Routing** with skills-based routing rules
7. **Configure Entitlements** with customer service entitlements
8. **Configure Performance Analytics** for CSM dashboards
9. **Configure Flow Designer** for automated customer service workflows
10. **Configure Dashboards** for CSM performance monitoring
11. **Train agents and managers** on ServiceNow CSM usage

---

## 5. Related Resources

- [ServiceNow CSM Documentation](https://docs.servicenow.com/bundle/orlando-customer-service-management/)
- [ServiceNow ITSM Documentation](https://docs.servicenow.com/bundle/orlando-it-service-management/)
- [ServiceNow Integration Hub Documentation](https://docs.servicenow.com/bundle/orlando-integration-hub/)
- [ServiceNow Flow Designer Documentation](https://docs.servicenow.com/bundle/orlando-flow-designer/)
- [ServiceNow Performance Analytics Documentation](https://docs.servicenow.com/bundle/orlando-performance-analytics/)

---

*Generated by Kilo on 2026-11-05. Part of the ServiceNow_Learning_SAM repository at github.com/eltonaguiar/ServiceNow_Learning_SAM.*
