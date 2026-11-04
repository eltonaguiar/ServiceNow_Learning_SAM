# Lab: ServiceNow SAM REST Message Integration

**Lab:** ServiceNow SAM Developer / Technical Consultant  
**Module:** Integration / Scripting  
**Target Role:** ServiceNow SAM Developer  
**Difficulty:** Beginner  
**Estimated Time:** 60 minutes  
**Source:** https://github.com/eltonaguiar/ServiceNow_Learning_SAM  
**Agent:** Kilo  
**Date:** 2026-11-04  

---

## Lab Overview

**Goal:** Build a working ServiceNow SAM REST Message integration that calls a public API, retrieves data, and displays it on a ServiceNow record.

**What You'll Learn:**
- How to create an outbound REST Message in ServiceNow SAM
- How to configure HTTP method, endpoint, and authentication
- How to call a REST Message from a Business Rule or Script Include
- How to parse the JSON response
- How to display the result on a ServiceNow record

**Prerequisites:**
- ServiceNow developer instance access
- `web_service_admin` role (or `admin`)
- Internet access from your ServiceNow instance

---

## Lab Setup

### Step 1: Verify Access

1. Log into your ServiceNow instance
2. Navigate to **System Web Services → Outbound REST Messages**
3. Verify you can see the list (if not, you need the `web_service_admin` role)
4. Log out and back in after adding any roles

### Step 2: Create an Update Set

1. Go to **System Update Sets → Local Update Sets**
2. Click **New**
3. Name: `SAM REST Message Lab - [Your Name]`
4. State: `In Progress`
5. Click **Submit**
6. Click **Make Current**

---

## Lab Steps

### Step 1: Create the REST Message

1. Go to **System Web Services → Outbound REST Messages**
2. Click **New**
3. Fill in:
   - **Name:** `SAM License Lookup`
   - **Application:** `Global`
   - **Endpoint:** `https://jsonplaceholder.typicode.com/posts/1`
   - **HTTP Method:** `GET`
4. Click **Submit**

### Step 2: Create the REST Message Function

1. Open the REST Message record you just created
2. Scroll to the **REST Message Functions** related list
3. Click **New**
4. Fill in:
   - **Name:** `Get License`
   - **HTTP Method:** `GET`
   - **Endpoint:** `/posts/1` (relative to the main endpoint)
5. Click **Submit**

### Step 3: Create a Script Include to Call the REST Message

1. Go to **System Definition → Script Includes**
2. Click **New**
3. Fill in:
   - **Name:** `SAM REST Message Example`
   - **Application:** `Global`
   - **Client callable:** `true`
   - **Script:**
   ```javascript
   var SAMRESTMessageExample = Class.create();
   SAMRESTMessageExample.prototype = Object.extendsObject(AbstractAjaxProcessor, {
     getLicense: function() {
       var rm = new sn_ws.RESTMessageV2('THIS_IS_YOUR_MESSAGE_SYS_ID', 'Get License');
       var response = rm.execute();
       var httpStatus = response.getStatusCode();
       var body = response.getBody();
       
       var answer = new Object();
       answer.status = httpStatus;
       answer.body = body;
       return JSON.stringify(answer);
     },
     type: 'SAMRESTMessageExample'
   });
   ```
4. **Important:** Replace `THIS_IS_YOUR_MESSAGE_SYS_ID` with the actual sys_id of your REST Message record (find it by opening the REST Message record and looking at the sys_id in the URL or by right-clicking → Copy sys_id)
5. Click **Submit**

### Step 4: Test from a Script

1. Go to **System Definition → Script Includes**
2. Open your `SAM REST Message Example` record
3. Click **Test** (if available) or create a simple test:
   - Go to **System Definition → Script Includes**
   - Create a new test script include:
   ```javascript
   var test = new SAMRESTMessageExample();
   var result = test.getLicense();
   gs.print(result);
   ```
4. Run the script and check the output

### Step 5: Display on a Record (Optional)

1. Go to an `alm_license` record
2. Add a UI Policy or Client Script that calls your REST Message when the form loads
3. Display the result in a field or UI action

---

## Lab Validation

- [ ] REST Message record created with correct endpoint
- [ ] REST Message Function created
- [ ] Script Include created and references the correct REST Message sys_id
- [ ] Script executes without errors
- [ ] Response body contains JSON data from the API
- [ ] HTTP status code is 200

---

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Wrong sys_id in Script Include | `null` or error when calling REST Message | Copy sys_id from the REST Message record URL |
| Wrong HTTP method | 405 Method Not Allowed | Change to GET for read-only APIs |
| No internet access | Connection timeout | Check if your instance can reach external URLs |
| Missing `web_service_admin` role | Can't see REST Message menu | Add role to your user and log out/in |

---

## Critical Fields

| Field | Why It's Critical |
|-------|-------------------|
| REST Message Name | Identifies the message in scripts |
| Endpoint | The URL being called |
| HTTP Method | Must match what the API expects |
| REST Message Function sys_id | Used in script to call the specific function |

---

## Related Lists

| Related List | What It Shows | Why It Matters |
|--------------|---------------|----------------|
| REST Message Functions | Individual API calls within the message | Each function can have different HTTP methods/endpoints |
| Error Log | Failed message attempts | Debug failed integrations |

---

## Next Steps

1. Try a POST request instead of GET
2. Add authentication (Basic Auth or OAuth)
3. Parse specific fields from the JSON response
4. Create a UI Action on `alm_license` that calls your REST Message
5. Display the result in a license field

---

*Generated by Kilo on 2026-11-04. Part of the ServiceNow_Learning_SAM repository at github.com/eltonaguiar/ServiceNow_Learning_SAM.*
