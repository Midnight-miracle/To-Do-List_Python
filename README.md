# To-Do-List_Python
A simple REST API for managing a to-do list, built with FastAPI and SQLAlchemy.

## Features

- Create, read, update and delete to-dos
- Request validation with Pydantic
- Database storage with SQLAlchemy

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

## Setup

1. Clone the repository and move into the folder.

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project folder with your database URL:

   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/your_database
   ```

4. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

The tables are created automatically on startup. Interactive API docs are available at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Endpoint       | Description        |
|--------|----------------|--------------------|
| GET    | `/todos`       | Get all to-dos     |
| GET    | `/todos/{id}`  | Get one to-do      |
| POST   | `/todos`       | Create a to-do     |
| PUT    | `/todos/{id}`  | Update a to-do     |
| DELETE | `/todos/{id}`  | Delete a to-do     |

### Example request body

```json
{
  "name": "Buy milk",
  "completed": false
}
```

### Example response

```json
{
  "id": 1,
  "name": "Buy milk",
  "completed": false
}
```

## Project Structure

```
main.py             # API routes
models.py           # Pydantic models (request/response)
database_models.py  # SQLAlchemy table models
database.py         # Database connection and session
```
