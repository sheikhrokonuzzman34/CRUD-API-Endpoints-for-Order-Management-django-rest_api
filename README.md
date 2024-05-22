# Employee Records Management & Analytics Service

This Django-based API manages employee records and provides analytical insights.

## Git clone
   ```bash
   git clone https://github.com/sheikhrokonuzzman34/Employee-Records-Management-Analytics-Service.git

   ``` 


## How to Run

1. virtual environment Crete : `python -m venv env`
2. virtual environment active : `. env/Scripts/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. file directory change : `cd Employee-Records-Management-Analytics-Service/`
5. Apply migrations: `python manage.py migrate`
6. Run the server: `python manage.py runserver`

## Testing

Run the test suite:

```bash
python manage.py test
```   


## Base URL
- All endpoints are relative to the base URL: `https://example.com/api/`

## Authentication
- The API requires authentication using [Token Authentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication).

---

## django default database
- django default database URL: `http://127.0.0.1:8000/admin/`
  ```text
  username : 'adminR'
  password : '123zxc123'
  ```


## Department Endpoints

### List Departments
- **URL:** `GET /departments/`
- **Description:** Get a list of all departments.
- **Authentication:** Required
- **Response:**
  - Status Code: 200 OK
  - Content: List of departments in the system.

### Create Department
- **URL:** `POST /departments/`
- **Description:** Create a new department.
- **Authentication:** Required
- **Request:**
  - Body: Department data (name).
- **Response:**
  - Status Code: 201 Created
  - Content: Newly created department data.

### Retrieve, Update, Delete Department
- **URL:** `GET/PUT/PATCH/DELETE /departments/{department_id}/`
- **Description:** Get, update, or delete a specific department by ID.
- **Authentication:** Required
- **Response:**
  - Status Code: 200 OK (for GET), 200 OK (for PUT/PATCH), 204 No Content (for DELETE)
  - Content: Department data.

---

## Employee Endpoints

### List Employees
- **URL:** `GET /employees/`
- **Description:** Get a list of all employees.
- **Authentication:** Required
- **Response:**
  - Status Code: 200 OK
  - Content: List of employees in the system.

### Create Employee
- **URL:** `POST /employees/`
- **Description:** Create a new employee.
- **Authentication:** Required
- **Request:**
  - Body: Employee data (name, department, tenure, hire_date).
- **Response:**
  - Status Code: 201 Created
  - Content: Newly created employee data.

### Retrieve, Update, Delete Employee
- **URL:** `GET/PUT/PATCH/DELETE /employees/{employee_id}/`
- **Description:** Get, update, or delete a specific employee by ID.
- **Authentication:** Required
- **Response:**
  - Status Code: 200 OK (for GET), 200 OK (for PUT/PATCH), 204 No Content (for DELETE)
  - Content: Employee data.

---

## Analytics Endpoints

### Employee Analytics
- **URL:** `GET /analytics/`
- **Description:** Get analytical data such as employee count by department, average tenure, and more.
- **Authentication:** Required
- **Response:**
  - Status Code: 200 OK
  - Content: Analytical data.

---

## Error Responses
- The API may return the following error responses:
  - Status Code: 400 Bad Request - Invalid request parameters.
  - Status Code: 401 Unauthorized - Authentication failure.
  - Status Code: 403 Forbidden - Insufficient permissions.
  - Status Code: 404 Not Found - Resource not found.
  - Status Code: 500 Internal Server Error - Unexpected server error.

---

## Versioning
- This documentation is for version 1 of the Employee Management API.

---


