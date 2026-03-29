# FastAPI CRUD Product API

A simple and clean **CRUD (Create, Read, Update, Delete)** API built using **FastAPI** and **SQLAlchemy**. This project demonstrates how to build RESTful APIs with proper structure, validation, and database integration.

---

## Features

* Create new products 
* Get all products 
* Get single product by ID 
* Update existing product 
* Delete product 
* Automatic API docs (Swagger UI) 

---

## Tech Stack

* **FastAPI** – Web framework
* **SQLAlchemy** – ORM for database
* **SQLite / PostgreSQL** – Database
* **Pydantic** – Data validation

---

## Project Structure

```
.
├── main.py              # Entry point
├── db_models.py         # SQLAlchemy models (DB tables)
├── schemas.py           # Pydantic models (request/response)
├── database.py          # DB connection setup
└── requirements.txt     # Dependencies
```

---

## Installation & Setup

### Clone the repository

```bash
git clone https://github.com/your-username/fastapi-crud.git
cd fastapi-crud
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn main:app --reload
```

---

## API Documentation

After running the server, open:

* Swagger UI:
  http://127.0.0.1:8000/docs

* ReDoc:
  http://127.0.0.1:8000/redoc

---

## API Endpoints

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| POST   | /product      | Create new product |
| GET    | /products     | Get all products   |
| GET    | /product/{id} | Get product by ID  |
| PUT    | /product/{id} | Update product     |
| DELETE | /product/{id} | Delete product     |

---

## How It Works

1. Client sends request (JSON)
2. FastAPI validates using Pydantic models
3. Data is converted to SQLAlchemy model
4. Database operation is performed
5. Response is returned

---

## Example Request (Create Product)

```json
{
  "name": "Phone",
  "description": "Smart device",
  "price": 500,
  "quantity": 10
}
```

---

## Future Improvements

* Add authentication (JWT) 
* Pagination & filtering 
* Docker support 
* Deployment (Render / AWS) 

---

## Contributing

Feel free to fork this repo and submit pull requests.

---

## License

This project is open-source and available under the MIT License.

---
