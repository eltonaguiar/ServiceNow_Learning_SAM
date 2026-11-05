# ServiceNow Transaction Service Operations Management (TSOM)

**Module:** Transaction Service Operations Management (TSOM)  
**Category:** IT Operations Management (ITOM)  
**Certification Path:** ServiceNow Certified Implementation Specialist – IT Operations Management (CIS-ITOM)  
**Author:** Kilo AI Agent  
**Date:** 2026-11-05  
**Repository:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM  
**Branch:** kilo-2026-11-05-sam-modules

---

## 1. Overview

ServiceNow Transaction Service Operations Management (TSOM) is designed to help IT teams monitor, analyze, and remediate transaction performance issues across complex, multi-tier application architectures. TSOM provides end-to-end visibility into business transactions by correlating application performance data with infrastructure metrics, enabling IT teams to quickly identify root causes of performance degradation.

### Core Value Proposition

- **End-to-end transaction visibility** across hybrid, multi-cloud environments
- **Automatic discovery** of application dependencies and service maps
- **Real-time performance monitoring** with anomaly detection
- **Proactive remediation** through AI-driven insights and automated remediation workflows
- **Cross-domain correlation** between application performance and infrastructure health

---

## 2. Key Table Hierarchy

TSOM relies on the following core tables in the ServiceNow CMDB and data model:

| Table Name | Table Name (sys_db_object) | Description | Key Fields |
|------------|---------------------------|-------------|------------|
| `cmdb_ci_service` | `cmdb_ci_service` | Configuration items representing services | `name`, `category`, `subcategory`, `owned_by`, `supported_by` |
| `cmdb_ci_service_offering` | `cmdb_ci_service_offering` | Service offerings linked to services | `name`, `service`, `cost_center`, `charge_model` |
| `cmdb_ci_service_group` | `cmdb_ci_service_group` | Service groups for logical grouping | `name`, `description`, `members` |
| `cmdb_ci_application` | `cmdb_ci_application` | Application configuration items | `name`, `version`, `vendor`, `acquired_date` |
| `cmdb_ci_app_server` | `cmdb_ci_app_server` | Application server CIs | `name`, `ip_address`, `os_version`, `cpu_count`, `memory` |
| `cmdb_ci_web_server` | `cmdb_ci_web_server` | Web server configuration items | `name`, `web_server_type`, `version`, `port` |
| `cmdb_ci_db_server` | `cmdb_ci_db_server` | Database server CIs | `name`, `db_type`, `version`, `instance_name`, `port` |
| `tm_transaction` | `tm_transaction` | Transaction records | `name`, `sys_id`, `start_time`, `end_time`, `duration`, `status` |
| `tm_transaction_trace` | `tm_transaction_trace` | Detailed transaction trace data | `transaction_id`, `node_name`, `component_name`, `start_time`, `duration` |
| `tm_transaction_error` | `tm_transaction_error` | Transaction errors and exceptions | `transaction_id`, `error_code`, `error_message`, `stack_trace` |
| `tm_transaction_dependency` | `tm_transaction_dependency` | Transaction dependency mappings | `transaction_id`, `dependent_ci`, `relationship_type` |
| `tm_metric` | `tm_metric` | Transaction performance metrics | `transaction_id`, `metric_name`, `metric_value`, `timestamp` |

### Table Relationships

```
tm_transaction ──┬── tm_transaction_trace (1:N)
                ├── tm_transaction_error (1:N)
                ├── tm_transaction_dependency (1:N)
                └── tm_metric (1:N)

cmdb_ci_service ──┬── cmdb_ci_service_offering (1:N)
                  ├── cmdb_ci_service_group (1:N)
                  └── cmdb_ci_application (1:N)

cmdb_ci_application ──┬── cmdb_ci_app_server (1:N)
                      ├── cmdb_ci_web_server (1:N)
                      └── cmdb_ci_db_server (1:N)

cmdb_ci_app_server ── tm_transaction_dependency (N:1)
cmdb_ci_web_server ── tm_transaction_dependency (N:1)
cmdb_ci_db_server ── tm_transaction_dependency (N:1)
```

---

## 3. Out-of-Box Features

TSOM provides the following out-of-box capabilities:

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Transaction Discovery** | Automatically discovers business transactions across hybrid cloud environments | Auto-discover transactions without manual instrumentation |
| **Service Mapping** | Visualizes service dependencies and relationships | Understand how services and CIs interconnect |
| **Performance Monitoring** | Real-time monitoring of transaction performance metrics | Identify slow transactions and performance bottlenecks |
| **Anomaly Detection** | ML-based anomaly detection for transaction performance | Proactively identify performance degradation |
| **Error Tracking** | Tracks transaction errors and exceptions | Identify and prioritize error resolution |
| **Dependency Mapping** | Maps transaction dependencies across infrastructure | Understand impact of changes and incidents |
| **Dashboard & Reporting** | Pre-built dashboards for transaction performance | Executive and operational visibility |
| **Alerting** | Configurable alerts for transaction anomalies | Proactive notification of performance issues |
| **Integration with ITOM** | Integrates with ITOM Discovery, Service Mapping, Event Management | Unified view of IT operations |
| **Mobile Support** | Mobile access to transaction performance data | Monitor transactions on-the-go |

---

## 4. Re-usable Code & Meta Data

### Script Includes

#### Transaction Performance Calculator

```javascript
var TSOMMetricCalculator = Class.create();
TSOMMetricDefinition.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    calculateTransactionPerformance: function(txnSysId) {
        var txn = new GlideRecord('tm_transaction');
        if (!txn.get(txnSysId)) {
            return JSON.stringify({error: 'Transaction not found'});
        }
        
        var response = {
            sys_id: txn.getValue('sys_id'),
            name: txn.getValue('name'),
            duration: txn.getValue('duration'),
            status: txn.getValue('state'),
            start_time: txn.getValue('start_time'),
            end_time: txn.getValue('end_time')
        };
        
        // Get associated traces
        var traces = [];
        var traceGr = new GlideRecord('tm_transaction_trace');
        traceGr.addQuery('transaction_id', txnSysId);
        traceGr.query();
        while (traceGr.next()) {
            traces.push({
                node: traceGr.getValue('node_name'),
                component: traceGr.getValue('component_name'),
                duration: traceGr.getValue('duration'),
                start_time: traceGr.getValue('start_time')
            });
        }
        response.trace_details = traces;
        
        // Get associated errors
        var errors = [];
        var errGr = new GlideRecord('tm_transaction_error');
        errGr.addQuery('transaction_id', txnSysId);
        errGr.query();
        while (errGr.next()) {
            errors.push({
                error_code: errGr.getValue('error_code'),
                error_message: errGr.getValue('error_message'),
                stack_trace: errGr.getValue('stack_trace')
            });
        }
        response.error_details = errors;
        
        return JSON.stringify(response);
    },
    
    type: 'TSOMMetricCalculation'
});
```

#### Transaction Health Calculator

```javascript
var TSOMHealthCalculator = Class.create();
TSOMHealthCalculator.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    calculateHealthScore: function(txnSysId) {
        var txn = new GlideRecord('tm_transaction');
        if (!txn.get(txnSysId)) {
            return JSON.stringify({error: 'Transaction not found'});
        }
        
        var txnSysId = txn.getValue('sys_id');
        var threshold = 2000; // 2 seconds threshold for good performance
        
        var txnDuration = parseInt(txn.getValue('duration')) || 0;
        var errorCount = 0;
        
        var errGr = new GlideRecord('tm_transaction_error');
        errGr.addQuery('transaction_id', txnSysId);
        errGr.query();
        while (errGr.next()) {
            errorCount++;
        }
        
        var healthScore = 100;
        var factors = [];
        
        if (txnDuration > threshold) {
            var penalty = Math.min((txnDuration / threshold - 1) * 20, 50);
            healthScore -= penalty;
            factors.push('High response time: ' + txnDuration + 'ms (threshold: ' + threshold + 'ms)');
        }
        
        if (errorCount > 0) {
            var penalty = Math.min(errorCount * 10, 30);
            healthScore -= penalty;
            factors.push('Error count: ' + errorCount);
        }
        
        if (healthScore < 0) healthScore = 0;
        
        var status = 'healthy';
        if (healthScore < 50) status = 'critical';
        else if (healthScore < 75) status = 'warning';
        
        return JSON.stringify({
            sys_id: txnSysId,
            title: txn.getValue('name'),
            health_score: healthScore,
            status: status,
            duration: txnDuration,
            error_count: errorCount,
            factors: factors,
            threshold: threshold
        });
    },
    
    type: 'TSOMHealthCalculator'
});
```

### Business Rules

#### Transaction Performance Monitor

**Name:** TSOM Transaction Performance Monitor  
**Table:** tm_transaction  
**Type:** Before  
**Operations:** insert, update

```javascript
(function rule(current, previous) {
    var HIGH_RISK_THRESHOLD = 5000; // 5 seconds
    var MEDIUM_RISK_THRESHOLD = 2000; // 2 seconds
    
    var duration = parseInt(current.duration) || 0;
    
    if (duration > HIGH_RISK_THRESHOLD) {
        current.priority = 1;
        current.comments = (current.comments || '') + '\n[TSOM] High transaction duration detected: ' + duration + 'ms at ' + new Date().toISOString();
    } else if (duration > MEDIUM_RISK_THRESHOLD) {
        current.priority = 2;
        current.comments = (current.comments || '') + '\n[TSOM] Moderate transaction duration detected: ' + duration + 'ms at ' + new Date().toISOString();
    }
})(current, previous);
```

#### Transaction Error Handler

**Name:** TSOM Transaction Error Handler  
**Table:** tm_transaction_error  
**Type:** After  
**Operations:** insert

```javascript
(function rule(current, previous) {
    var criticalErrorPatterns = ['OutOfMemoryError', 'ConnectionTimeout', 'SocketTimeout', 'NullPointerException'];
    
    var errorMessage = current.error_message || '';
    var isCritical = false;
    
    criticalErrorPatterns.forEach(function(pattern) {
        if (errorMessage.indexOf(pattern) !== -1) {
            isCritical = true;
        }
    });
    
    if (isCritical) {
        current.priority = 1;
        current.comments = (current.comments || '') + '\n[TSOM] Critical error detected: ' + current.error_code + ' - ' + current.error_message;
        
        // Create incident for critical errors
        var incident = new GlideRecord('incident');
        incident.initialize();
        incident.short_description = 'TSOM: Critical Transaction Error - ' + current.error_code;
        incident.description = 'Transaction Error detected:\n' +
            'Transaction: ' + current.transaction_id + '\n' +
            'Error Code: ' + current.error_code + '\n' +
            'Error Message: ' + current.error_message + '\n' +
            'Stack Trace: ' + (current.stack_trace || 'N/A') + '\n' +
            'Time: ' + new Date().toISOString();
        incident.priority = 2;
        incident.urgency = 2;
        incident.impact = 2;
        incident.category = 'Software';
        incident.subcategory = 'Application Error';
        incident.insert();
        
        current.comments = (current.comments || '') + '\n[TSOM] Incident created: ' + incident.getValue('number');
    }
})(current, previous);
```

---

## 5. Integrations

TSOM integrates with the following ServiceNow modules and external systems:

| Integration | Purpose | Method |
|-------------|---------|--------|
| **ServiceNow CMDB** | Configuration Item data for transaction dependencies | Direct table joins |
| **ServiceNow ITOM Discovery** | Automatic discovery of servers and applications | MID Server, REST API |
| **ServiceNow Service Mapping** | Service relationship mapping | Shared data model |
| **ServiceNow Event Management** | Event correlation for transaction anomalies | Event rules, event rules |
| **ServiceNow Incident Management** | Incident creation from transaction errors | Business rules, REST API |
| **ServiceNow Change Management** | Change impact analysis on transactions | Update sets, change records |
| **External APM Tools** (Dynatrace, AppDynamics, New Relic) | External APM data ingestion | REST API, MID Server, Import Sets |
| **External Monitoring** (Prometheus, Grafana) | Metrics ingestion | REST API, MID Server |
| **ServiceNow Flow Designer** | Automated remediation workflows | Flow Designer actions |
| **ServiceNow Notifications** | Alert notifications for transaction issues | Email, SMS, Slack, Teams |

### Integration Example: External APM Data Ingestion

```javascript
// Example: Ingest APM data via REST Message
var restMessage = new sn_ws.RESTMessageV2('APM Integration', 'Get Transaction Metrics');
restMessage.setStringParameter('application_id', appSysId);
var response = restMessage.execute();
var responseBody = response.getBody();
var responseStatus = response.getStatusCode();

if (responseStatus === 200) {
    var responseData = JSON.parse(responseBody);
    // Process and create transaction records
}
```

---

## 5. Getting Started Steps

1. **Enable ServiceNow ITSM/ITOM application** on your instance
2. **Configure CMDB** with accurate CI data for services, applications, and infrastructure
3. **Configure Service Mapping** to discover application dependencies
4. **Configure MID Server** for on-premise discovery and monitoring
5. **Configure Integration Hub** for external APM tool integration
6. **Configure Performance Analytics** for transaction performance dashboards
7. **Configure Event Management** for transaction error and alert correlation
8. **Configure Flow Designer** for automated remediation workflows
9. **Configure Dashboards** for transaction performance monitoring
10. **Train teams** on ServiceNow TSOM usage and procedures

---

## 5. Related Resources

- [ServiceNow ITSM Documentation](https://docs.servicenow.com/bundle/orlando-it-service-management/)
- [ServiceNow ITOM Documentation](https://docs.servicenow.com/bundle/orlando-it-operations-management/)
- [ServiceNow Performance Analytics Documentation](https://docs.servicenow.com/bundle/orlando-performance-analytics/)
- [ServiceNow Integration Hub Documentation](https://docs.servicenow.com/bundle/orlando-integration-hub/)
- [ServiceNow Flow Designer Documentation](https://docs.servicenow.com/bundle/orlando-flow-designer/)

---

*Generated by Kilo on 2026-11-05. Part of the ServiceNow_Learning_SAM repository at github.com/eltonaguiar/ServiceNow_Learning_SAM.*
