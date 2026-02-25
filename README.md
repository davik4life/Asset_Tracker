This is the README for the Asset_Tracker API Documentation


**Setup:**
::: Local :::

Base API URL: https://127.0.0.1:8000/api/auth/token # Replace with your desired port.

**::: Production :::**

Base URL: https://your-ap.onrender.com/api/

**Endpoints:**
Authentication Endpoints (JWT)
This endpoints do not require authentication.

POST: 
```markdown
/api/auth/token/
```

**Body**
Test Login
```json
{
  "username": "runtest",
  "password": "RunPass12."
}
```
**Response**
```json
{
  "access": "token_here",
  "refresh": "token_here"
}
```
**Refresh Token**
POST
```markdown
/api/auth/token/refresh/
```
Body
```json
{
  "refresh": "your_refresh_token"
}
```
**Authentication Header**
All protected endpoints require;
Authorization: Bearer YOUR_ACCESS_TOKEN

**::: Assets Endpoints :::**
Base: 
```markdown
/api/assets/
```
POST: 
```markdown
/api/assets/
```
Body: 
```json
{
  "name": "Laptop",
  "category": "Device Fixes",
  "condition": "Looking dirty",
  "purchase_date": "2023-01-10"
}
```
Note: Owner is automatically assigned via JWT.

GET: 
```markdown
/api/assets/
```
Note: Returns only assets belonging to logged-in user.

**Get Single Asset**
GET: 
```markdown
/api/assets/{id}/
```
Example: 
```markdown
/api/assets/1/
```

**Update Asset**
PUT: /api/assets/{id}/

Body: 
```json
{
  "name": "Updated Laptop",
  "category": "Personal Device Fixes",
  "condition": "Looking like new",
  "purchase_date": "2024-01-10"
}
```

**Partial Updates**
PATCH: 
```markdown
/api/assets/{id}/
```
Example: 
```json
{
  "name": "New Name"
}
```
**Delete Asset**
DELETE: 
```markdown
/api/assets/{id}/
```

**::: Asset Filtering :::**
Filter by the following: ['name','category', 'condition']
e.g: Filter by Name: 
```markdown
/api/assets/?name=Laptop
```

**::: Asset Search :::**
Search by the following: ['name', 'category', 'condition']
e.g: Search by name: 
```markdown
/api/assets/?search=laptop
```

**::: Asset Ordering :::**
Order by the following: ['name', 'purchase_date', 'created_at']
Ascending: 
```markdown
/api/assets/?ordering=name
```
Descending: 
```markdown
/api/assets/?ordering=-name
```


**::: Maintenance Records Endpoints :::**
Base: 
```markdown
/api/records/
```

**Create Record**

POST: 
```markdown
/api/records/
```

Body:
```json
{
  "asset": 1,
  "created_by": "John",
  "service_date": "2024-02-10",
  "service_type": "Screen repair",
  "cost": 150.00,
  "notes": "This is the record of my phone fix."
  
}
```
**Get All Records**
GET: 
```markdown
/api/records/
```
Note: Returns only records belonging to user assets.

**Get Single Record**
GET: 
```markdown
/api/records/{id}/
```


**Update Record**
PUT: 
```markdown
/api/records/{id}/
```

**Delete Record**
DELETE: 
```markdown
/api/records/{id}/
```

**Records Filtering**
Filter by the following: ['asset__name', 'service_type']
e.g:  
```markdown
/api/records/?asset__name=Generator
```


**Records Search**
e.g: 
```markdown
/api/records/?search=repair
```

**Records Ordering**
Ascending: 
```markdown
/api/records/?ordering=maintenance_date
```
Descending: 
```markdown
/api/records/?ordering=-maintenance_date
```

**::: Maintenance Schedule Endpoints :::**

Base: 
```markdown
/api/schedules/
```

POST: 
```markdown
/api/schedules/
```

Body: 
```json
{
  "asset": 1,
  "interval_days": 30,
  "next_service_date": "2024-02-01"
}
```
**Get All Schedules**
GET: 
```markdown
/api/schedules/
```

**Get Single Schedule**
GET: /api/schedules/{id}/

**Update Schedule**
PUT: 
```markdown
/api/schedules/{id}/
```

**Delete Schedule**
DELETE: 
```markdown
/api/schedules/{id}/
```

**Schedule Filtering**
```markdown
/api/schedules/?interval_days=30
```

**Schedule Ordering**
Ascending: 
```markdown
/api/schedules/?ordering=next_service_date
```
Descending: 
```markdown
/api/schedules/?ordering=-next_service_date
```


**::: Complete Endpoint List (For Documentation) :::**

**Auth**

POST   
```markdown
/api/token/
```
POST   
```markdown
/api/token/refresh/
```

**Assets**
```markdown
GET    /api/assets/
POST   /api/assets/
GET    /api/assets/{id}/
PUT    /api/assets/{id}/
PATCH  /api/assets/{id}/
DELETE /api/assets/{id}/
```
**Records**
```markdown
GET    /api/records/
POST   /api/records/
GET    /api/records/{id}/
PUT    /api/records/{id}/
DELETE /api/records/{id}/
```
**Schedules**
```markdown
GET    /api/schedules/
POST   /api/schedules/
GET    /api/schedules/{id}/
PUT    /api/schedules/{id}/
DELETE /api/schedules/{id}/
```