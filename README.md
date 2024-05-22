# Order Management Service

This Django-based API manages Order-Management.

## Git clone
   ```bash
   git clone https://github.com/sheikhrokonuzzman34/CRUD-API-Endpoints-for-Order-Management-django-rest_api.git

   ``` 


## How to Run

1. virtual environment Crete : `python -m venv env`
2. virtual environment active : `. env/Scripts/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. file directory change : `cd CRUD-API-Endpoints-for-Order-Management-django-rest_api/`
5. Apply makemigrations: `python manage.py makemigrations`
6. Apply migrations: `python manage.py migrate`
7. Apply refresh_and_seed: `python manage.py refresh_and_seed`
8. Run the server: `python manage.py runserver`

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

## Fake generator user
-
  ```text
  username : 'testuser'
  password : '123456'
  ```


## Authentication Endpoints

### Token Authentication
- **URL:** `POST /token/`
- **Description:** Get refres and access token.
- **Description:** Body username and password
- **Response:**
  - Status Code: 200 OK
  

### List products
- **URL:** `POST /products/`
- **Description:** List products.
- **Authentication:** Required
- **Headers:** Authorization Bearer token
- **Response:**
  - Status Code: 201 Created
  - Content: Newly created department data.

### Retrieve, Update, Delete products
- **URL:** `GET/PUT/PATCH/DELETE /products/{products_id}/`
- **Description:** Get, update, or delete a specific products by ID.
- **Authentication:** Required
- **Response:**
  - Status Code: 200 OK (for GET), 200 OK (for PUT/PATCH), 204 No Content (for DELETE)
  - Content: Department data.

---

## Orders Endpoints

### List orders
- **URL:** `GET /orders/`
- **Description:** Get a list of all orders.
- **Authentication:** Required
- **Response:**
  - Status Code: 200 OK
  - Content: List of employees in the system.

### Create orders
- **URL:** `POST /orders/`
- **Description:** Create a new orders.
- **Authentication:** Required
- **Request:**
  - Body: (id, user, payment_info, created_at,updated_at,delivery_status,total_amount,items:{"id":1},product:{"id":2},quantity).
- **Response:**
  - Status Code: 201 Created
  - Content: Newly created employee data.

### Retrieve, Update, Delete order_detail
- **URL:** `GET/PUT/PATCH/DELETE /orders/{orders_id}/`
- **Description:** Get, update, or delete a specific orders by ID.
- **Authentication:** Required
- **Response:**
  - Status Code: 200 OK (for GET), 200 OK (for PUT/PATCH), 204 No Content (for DELETE)
  - Content: Employee data.

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
- This documentation is for version 1 of the Order-Management API.

---

