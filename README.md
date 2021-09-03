# Sergio and Laura's Wedding
---
## Overview: 
My brother is going to get married, and all his wedding invitation system it's going to be digital and build by him (frontend) and  me (backend).
The invitation system allows the user to confirm its assistance and its family assistance to the wedding. As well as food allergies, number of assistents and additional comments. Finally, the system will send automatically a personalized invitation once the  user confirm that is going to be at the wedding.

### Scope
The goal is to provide a suitable Api which allows http requests from the frontend. that way the frontend has access to the data base, users authentication, family forms and reports. 

#### Use-Cases

* User login with their phone.
* User confirm assitance once is logged in and receive the general invitation.
* User confirm the assistance once is logged in and receive the form to fill up.
* If a family member already filled out the form you can check it or modify it.
* User fill up the form and receive the form summary.
* The system admin can download the report of the users that already confirmed the assistance.

#### Out of Scope (use-cases not supported)

* Users can't have the guest report.
* User decline the assistance once is logged in and receive the greating card.

## Architecture

### Diagram
<p>
    <img src="https://drive.google.com/uc?export=view&id=10u5iXSAPQUDJ8oXiiuRSMzyoc0ZyT4cg">
</p>

### Data Modeling
Entities, Jsons, Tables, entity-relations diagram.

#### Entity-Relationship Diagram
<p>
    <img src="https://drive.google.com/uc?export=view&id=1WjfJHrR2180hvx6tTgzC58HFzRfZvBJi">
</p>


## Limitations
* Get requests should have a x ms latency or less.
* Api latency is X ms
* No more than X requests per second

## Testing Plan

* User login, invitation received, form received, is filled up?, check user info, receiving form summary, admin system.

