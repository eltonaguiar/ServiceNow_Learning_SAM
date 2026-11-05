# ServiceNow Sales CRM

**Module:** Sales CRM  
**Category:** Sales Force Automation  
**Certification Path:** ServiceNow Certified Implementation Specialist – Sales  
**Author:** Kilo AI Agent  
**Date:** 2026-11-05  
**Repository:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM  
**Branch:** kilo-2026-11-05-sam-modules

---

## 1. Overview

ServiceNow Sales CRM is a sales force automation solution that helps sales teams manage leads, opportunities, accounts, and opportunities throughout the sales lifecycle. It provides end-to-end sales process management from lead generation to deal closure.

### Core Value Proposition

- **Lead Management** - Capture, qualify, and route sales leads
- **Opportunity Management** - Track sales opportunities through the sales cycle
- **Account Management** - Manage customer accounts and relationships
- **Pipeline Management** - Visualize and manage sales pipeline
- **Forecasting** - Sales forecasting and revenue projections
- **Activity Management** - Track sales activities and interactions
- **Quote Management** - Create and manage sales quotes and proposals
- **Territory Management** - Manage sales territories and assignments

---

## 2. Key Table Hierarchy

Sales CRM relies on the following core tables:

| Table Name | Table Name (sys_db_object) | Description | Key Fields |
|------------|---------------------------|-------------|------------|
| `sn_sales_lead` | `sn_sales_lead` | Sales leads | `number`, `title`, `company`, `contact`, `status`, `priority`, `assigned_to`, `assignment_group` |
| `sn_sales_opportunity` | `sn_sales_opportunity` | Sales opportunities | `number`, `name`, `account`, `contact`, `amount`, `probability`, `stage`, `close_date` |
| `sn_sales_account` | `sn_sales_account` | Sales accounts/companies | `name`, `account_number`, `industry`, `size`, `region`, `status`, `annual_revenue` |
| `sn_sales_contact` | `sn_sales_contact` | Sales contacts | `first_name`, `last_name`, `email`, `phone`, `account`, `title` |
| `sn_sales_quote` | `sn_sales_quote` | Sales quotes | `number`, `opportunity`, `valid_from`, `valid_to`, `total_amount`, `status` |
| `sn_sales_quote_line` | `sn_sales_quote_line` | Quote line items | `quote`, `product`, `quantity`, `unit_price`, `total_price` |
| `sn_sales_product` | `sn_sales_product` | Sales products | `name`, `product_code`, `category`, `list_price`, `cost_price` |
| `sn_sales_activity` | `sn_sales_activity` | Sales activities | `number`, `subject`, `type`, `status`, `due_date`, `assigned_to` |
| `sn_sales_territory` | `sn_sales_territory` | Sales territories | `name`, `region`, `country`, `manager` |
| `cmdb_ci` | `cmdb_ci` | Configuration items | `name`, `serial_number`, `model`, `location`, `status` |
| `task` | `task` | Base task table | `number`, `short_description`, `state`, `priority`, `assignment_group`, `assigned_to` |

### Table Relationships

```
sn_sales_account ──┬── sn_sales_opportunity (1:N)
                   └── sn_sales_contact (1:N)
                     └── sn_sales_lead (1:N)

sn_sales_opportunity ──┬── sn_sales_quote (1:N)
                       └── sn_sales_activity (1:N)

sn_sales_quote ──┬── sn_sales_quote_line (1:N)

sn_sales_product ──┬── sn_sales_quote_line (1:N)

cmdb_ci ──┬── sn_sales_opportunity (1:N)
          └── sn_sales_account (1:N)

cmn_location ──┬── sn_sales_account (1:N)
               └── sn_sales_territory (1:N)

sn_sales_territory ──┬── sn_sales_opportunity (1:N)
                     └── sn_sales_lead (1:N)
```

---

## 3. Out-of-Box Features

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Lead Management** | Capture, qualify, and route sales leads | Manage lead lifecycle from capture to conversion |
| **Opportunity Management** | Track sales opportunities through the sales cycle | Manage sales pipeline from prospect to close |
| **Account Management** | Manage customer accounts and relationships | Maintain customer account information and relationships |
| **Contact Management** | Manage sales contacts and stakeholders | Track contacts and their relationships |
| **Pipeline Management** | Visualize and manage sales pipeline | Track opportunities through sales stages |
| **Sales Forecasting** | Sales forecasting and revenue projections | Forecast sales revenue and performance |
| **Activity Management** | Track sales activities and interactions | Track calls, emails, meetings, and tasks |
| **Quote Management** | Create and manage sales quotes and proposals | Generate and track sales quotes |
| **Product Management** | Manage sales products and pricing | Manage product catalog and pricing |
| **Territory Management** | Manage sales territories and assignments | Assign sales territories to sales reps |
| **Integration Hub** | Integration with external systems (CRM, ERP, etc.) | Connect Sales CRM with other business systems |
| **Performance Analytics** | Sales performance dashboards and reports | Track sales performance and trends |

---

## 4. Re-usable Code & Meta Data

### Script Includes

#### Sales Lead Scoring

```javascript
var SalesLeadScoring = Class.create();
SalesLeadScoring.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    calculateLeadScore: function(leadSysId) {
        var lead = new GlideRecord('sn_sales_lead');
        if (!lead.get(leadSysId)) {
            return JSON.stringify({error: 'Lead not found'});
        }
        
        var score = 0;
        var factors = [];
        
        // Company size scoring
        var companySize = lead.getValue('company_size');
        if (companySize) {
            if (companySize == 'enterprise') {
                score += 30;
                factors.push('Enterprise company (+30)');
            } else if (companySize == 'mid_market') {
                score += 20;
                factors.push('Mid-market company (+20)');
            } else if (companySize == 'small_business') {
                score += 10;
                factors.push('Small business (+10)');
            }
        }
        
        // Industry scoring
        var industry = lead.getValue('industry');
        if (industry) {
            if (industry == 'technology' || industry == 'financial_services' || industry == 'healthcare') {
                score += 20;
                factors.push('High-value industry (+20)');
            } else {
                score += 10;
                factors.push('Standard industry (+10)');
            }
        }
        
        // Budget scoring
        var budget = parseInt(lead.getValue('budget')) || 0;
        if (budget > 100000) {
            score += 30;
            factors.push('High budget (>$100k) (+30)');
        } else if (budget > 50000) {
            score += 20;
            factors.push('Medium budget (>$50k) (+20)');
        } else if (budget > 10000) {
            score += 10;
            factors.push('Low budget (>$10k) (+10)');
        }
        
        // Timeline scoring
        var timeline = lead.getValue('timeline');
        if (timeline) {
            if (timeline == '0-3_months') {
                score += 20;
                factors.push('Immediate timeline (0-3 months) (+20)');
            } else if (timeline == '3-6_months') {
                score += 15;
                factors.push('Near-term timeline (3-6 months) (+15)');
            } else if (timeline == '6-12_months') {
                score += 10;
                factors.push('Medium-term timeline (6-12 months) (+10)');
            }
        }
        
        if (score > 100) score = 100;
        
        var leadScore = 'low';
        if (score >= 70) leadScore = 'high';
        else if (score >= 40) leadScore = 'medium';
        
        return JSON.stringify({
            lead_sys_id: leadSysId,
            lead_number: lead.getValue('number'),
            score: score,
            score_label: leadScore,
            factors: factors
        });
    },
    
    type: 'SalesLeadScoring'
});
```

#### Sales Forecast Calculator

```javascript
var SalesForecastCalculator = Class.create();
SalesForecastCalculator.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    
    calculateForecast: function(opportunitySysId) {
        var opp = new GlideRecord('sn_sales_opportunity');
        if (!opp.get(opportunitySysId)) {
            return JSON.stringify({error: 'Opportunity not found'});
        }
        
        var amount = parseFloat(opp.getValue('amount')) || 0;
        var probability = parseInt(opp.getValue('probability')) || 0;
        var closeDate = opp.getValue('close_date');
        
        var weightedAmount = amount * (probability / 100);
        
        var forecast = {
            opportunity_sys_id: opportunitySysId,
            opportunity_number: opp.getValue('number'),
            opportunity_name: opp.getValue('name'),
            amount: amount,
            probability: probability,
            weighted_amount: weightedAmount,
            close_date: closeDate,
            forecast_date: new Date().toISOString()
        };
        
        return JSON.stringify(forecast);
    },
    
    type: 'SalesForecastCalculator'
});
```

### Business Rules

#### Opportunity Stage Change

**Name:** Sales Opportunity Stage Change  
**Table:** sn_sales_opportunity  
**Type:** Before  
**Operations:** update

```javascript
(function rule(current, previous) {
    var oldStage = previous.getValue('stage');
    var newStage = current.getValue('stage');
    
    if (oldStage !== newStage) {
        current.comments = (current.comments || '') + '\n[Sales CRM] Stage changed from ' + oldStage + ' to ' + newStage + ' at ' + new Date().toISOString();
        
        // Update probability based on stage
        var stageProbabilities = {
            'prospecting': 10,
            'qualification': 25,
            'needs_analysis': 40,
            'value_proposition': 60,
            'negotiation': 80,
            'closed_won': 100,
            'closed_lost': 0
        };
        
        if (stageProbabilities[newStage] !== undefined) {
            current.probability = stageProbabilities[newStage];
        }
    }
})(current, previous);
```

---

## 5. Integrations

Sales CRM integrates with the following ServiceNow modules and external systems:

| Integration | Purpose | Method |
|-------------|---------|--------|
| **ServiceNow CMDB** | Configuration Item data for products and services | Direct table joins |
| **ServiceNow Integration Hub** | Integration with CRM, ERP, and marketing systems | REST API, MID Server |
| **ServiceNow Flow Designer** | Automated sales workflows | Flow Designer actions |
| **ServiceNow Notifications** | Sales notifications and alerts | Email, SMS, Slack, Teams |
| **External CRM Systems** (Salesforce, Microsoft Dynamics) | CRM data synchronization | Integration Hub, REST API |
| **External Marketing Automation** (HubSpot, Marketo, Pardot) | Marketing automation integration | Integration Hub, REST API |
| **External ERP Systems** (SAP, Oracle, Microsoft Dynamics) | ERP integration for orders and invoicing | Integration Hub, REST API |
| **External Communication** (Email, Phone, Video) | Sales communication integration | Integration Hub, REST API |
| **ServiceNow Data Management** | Data quality and deduplication | Data management policies |
| **ServiceNow Reporting** | Sales performance reporting and dashboards | Performance Analytics |

### Integration Example: External CRM Data Sync

```javascript
// Example: Sync Salesforce leads to ServiceNow
var restMessage = new sn_ws.RESTMessageV2('Salesforce Integration', 'Get Leads');
restMessage.setStringParameter('status', 'Open');
var response = restMessage.execute();
var responseStatus = response.getStatusCode();

if (responseStatus === 200) {
    var responseData = JSON.parse(response.getBody());
    responseData.records.forEach(function(lead) {
        var leadGr = new GlideRecord('sn_sales_lead');
        leadGr.addQuery('external_id', lead.Id);
        leadGr.query();
        if (leadGr.next()) {
            // Update existing lead
            leadGr.short_description = lead.Name;
            leadGr.company = lead.Company;
            leadGr.update();
        } else {
            // Create new lead
            var newLead = new GlideRecord('sn_sales_lead');
            newItem.initialize();
            newItem.short_description = lead.Name;
            newItem.company = lead.Company;
            newItem.email = lead.Email;
            newItem.phone = lead.Phone;
            newItem.external_id = lead.Id;
            newItem.insert();
        }
    });
}
```

---

## 5. Getting Started Steps

1. **Enable ServiceNow Sales CRM application** on your instance
2. **Configure CMDB** with accurate product and service data
3. **Configure Integration Hub** for external CRM and ERP system integration
4. **Configure MID Server** for on-premise system connectivity
5. **Configure Sales Territories** with sales territories and assignments
6. **Configure Product Catalog** with products and pricing
7. **Configure Sales Stages** with sales stage definitions
8. **Configure Performance Analytics** for sales dashboards
9. **Configure Flow Designer** for automated sales workflows
10. **Configure Dashboards** for sales performance monitoring
11. **Train sales team** on ServiceNow Sales CRM usage

---

## 5. Related Resources

- [ServiceNow Sales CRM Documentation](https://docs.servicenow.com/bundle/orlando-sales-force-automation/)
- [ServiceNow ITSM Documentation](https://docs.servicenow.com/bundle/orlando-it-service-management/)
- [ServiceNow Integration Hub Documentation](https://docs.servicenow.com/bundle/orlando-integration-hub/)
- [ServiceNow Flow Designer Documentation](https://docs.servicenow.com/bundle/orlando-flow-designer/)
- [ServiceNow Performance Analytics Documentation](https://docs.servicenow.com/bundle/orlando-performance-analytics/)

---

*Generated by Kilo on 2026-11-05. Part of the ServiceNow_Learning_SAM repository at github.com/eltonaguiar/ServiceNow_Learning_SAM.*
