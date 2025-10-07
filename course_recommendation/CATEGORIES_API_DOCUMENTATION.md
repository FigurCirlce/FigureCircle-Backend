# Categories Management API Documentation

## Overview
This API provides comprehensive CRUD operations for managing different categories including Education, Industry, Experience Level, Role, and Skills. All categories are stored in a single `categories` table with a `category_type` field to differentiate between them.

## Database Schema

### Categories Table
```sql
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_type VARCHAR(50) NOT NULL CHECK (category_type IN ('education', 'industry', 'experience_level', 'role', 'skills')),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(category_type, name)
);
```

## API Endpoints

### 1. Education APIs

#### Get All Education Categories
```http
GET /api/education
```

**Response:**
```json
{
  "education": [
    {
      "id": 1,
      "name": "Bachelor of Science",
      "description": "Undergraduate degree in science",
      "created_at": "2024-01-01T00:00:00",
      "updated_at": "2024-01-01T00:00:00"
    }
  ]
}
```

#### Create Education Category
```http
POST /api/education
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Bachelor of Engineering",
  "description": "Undergraduate engineering degree",
  "is_active": true
}
```

#### Get Specific Education Category
```http
GET /api/education/{education_id}
```

#### Update Education Category
```http
PUT /api/education/{education_id}
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Bachelor of Engineering",
  "description": "Updated description",
  "is_active": true
}
```

#### Delete Education Category (Soft Delete)
```http
DELETE /api/education/{education_id}
Authorization: Bearer <JWT_TOKEN>
```

### 2. Industry APIs

#### Get All Industry Categories
```http
GET /api/industry
```

#### Create Industry Category
```http
POST /api/industry
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Fintech",
  "description": "Financial technology industry",
  "is_active": true
}
```

#### Get Specific Industry Category
```http
GET /api/industry/{industry_id}
```

#### Update Industry Category
```http
PUT /api/industry/{industry_id}
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Fintech",
  "description": "Updated fintech description",
  "is_active": true
}
```

#### Delete Industry Category (Soft Delete)
```http
DELETE /api/industry/{industry_id}
Authorization: Bearer <JWT_TOKEN>
```

### 3. Experience Level APIs

#### Get All Experience Level Categories
```http
GET /api/experience-level
```

#### Create Experience Level Category
```http
POST /api/experience-level
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Associate",
  "description": "1-3 years of experience",
  "is_active": true
}
```

#### Get Specific Experience Level Category
```http
GET /api/experience-level/{experience_id}
```

#### Update Experience Level Category
```http
PUT /api/experience-level/{experience_id}
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Associate",
  "description": "Updated description",
  "is_active": true
}
```

#### Delete Experience Level Category (Soft Delete)
```http
DELETE /api/experience-level/{experience_id}
Authorization: Bearer <JWT_TOKEN>
```

### 4. Role APIs

#### Get All Role Categories
```http
GET /api/role
```

#### Create Role Category
```http
POST /api/role
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Full Stack Developer",
  "description": "Develops both frontend and backend",
  "is_active": true
}
```

#### Get Specific Role Category
```http
GET /api/role/{role_id}
```

#### Update Role Category
```http
PUT /api/role/{role_id}
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Full Stack Developer",
  "description": "Updated description",
  "is_active": true
}
```

#### Delete Role Category (Soft Delete)
```http
DELETE /api/role/{role_id}
Authorization: Bearer <JWT_TOKEN>
```

### 5. Skills APIs

#### Get All Skills Categories
```http
GET /api/skills
```

#### Create Skill Category
```http
POST /api/skills
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Docker",
  "description": "Containerization technology",
  "is_active": true
}
```

#### Get Specific Skill Category
```http
GET /api/skills/{skill_id}
```

#### Update Skill Category
```http
PUT /api/skills/{skill_id}
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Docker",
  "description": "Updated Docker description",
  "is_active": true
}
```

#### Delete Skill Category (Soft Delete)
```http
DELETE /api/skills/{skill_id}
Authorization: Bearer <JWT_TOKEN>
```

### 6. Bulk Operations

#### Bulk Create Categories
```http
POST /api/categories/bulk
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "categories": [
    {
      "category_type": "education",
      "name": "Bachelor of Medicine",
      "description": "Medical degree",
      "is_active": true
    },
    {
      "category_type": "skills",
      "name": "Kubernetes",
      "description": "Container orchestration",
      "is_active": true
    }
  ]
}
```

**Response:**
```json
{
  "message": "Created 2 categories",
  "created": [
    {
      "category_type": "education",
      "name": "Bachelor of Medicine",
      "description": "Medical degree"
    },
    {
      "category_type": "skills",
      "name": "Kubernetes",
      "description": "Container orchestration"
    }
  ],
  "errors": []
}
```

### 7. Search Operations

#### Search Categories
```http
GET /api/categories/search?q=python&type=skills
```

**Query Parameters:**
- `q` (required): Search query
- `type` (optional): Filter by category type

**Response:**
```json
{
  "query": "python",
  "category_type": "skills",
  "results": [
    {
      "id": 1,
      "category_type": "skills",
      "name": "Python",
      "description": "Python programming language",
      "created_at": "2024-01-01T00:00:00"
    }
  ],
  "count": 1
}
```

## Error Responses

### Common Error Codes
- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Missing or invalid JWT token
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

### Error Response Format
```json
{
  "error": "Error message description"
}
```

## Sample Data

Run the `sample_categories_data.py` script to populate the database with sample data:

```bash
python sample_categories_data.py
```

This will add sample data for all category types:
- **Education**: 10 sample education levels
- **Industry**: 10 sample industries
- **Experience Level**: 10 sample experience levels
- **Role**: 12 sample job roles
- **Skills**: 15 sample skills

## Authentication

Most endpoints require JWT authentication. Include the JWT token in the Authorization header:

```http
Authorization: Bearer <your_jwt_token>
```

## Usage Examples

### Frontend Integration (JavaScript)
```javascript
// Get all education categories
const response = await fetch('/api/education');
const data = await response.json();
console.log(data.education);

// Create a new skill
const newSkill = await fetch('/api/skills', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${jwtToken}`
  },
  body: JSON.stringify({
    name: 'React Native',
    description: 'Mobile app development framework',
    is_active: true
  })
});

// Search for categories
const searchResults = await fetch('/api/categories/search?q=javascript&type=skills');
const searchData = await searchResults.json();
console.log(searchData.results);
```

### Python Integration
```python
import requests

# Get all roles
response = requests.get('http://localhost:5000/api/role')
roles = response.json()['role']

# Create new industry
new_industry = requests.post(
    'http://localhost:5000/api/industry',
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {jwt_token}'
    },
    json={
        'name': 'Blockchain',
        'description': 'Blockchain and cryptocurrency industry',
        'is_active': True
    }
)
```

## Notes

1. **Soft Delete**: All delete operations are soft deletes (sets `is_active` to `false`)
2. **Unique Constraints**: Each category type has unique name constraints
3. **Case Sensitivity**: Search is case-insensitive
4. **Timestamps**: All timestamps are in ISO format
5. **Validation**: Category types are validated against allowed values
6. **Bulk Operations**: Bulk create handles errors gracefully and reports both successes and failures

## Database Indexes

For optimal performance, the following indexes are recommended:

```sql
CREATE INDEX idx_categories_type ON categories(category_type);
CREATE INDEX idx_categories_name ON categories(name);
CREATE INDEX idx_categories_active ON categories(is_active);
```
