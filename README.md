# Calculator REST API

A small Django REST Framework API for basic calculator operations.

## Run

```powershell
C:\Users\Windows\AppData\Local\Programs\Python\Python313\python.exe manage.py runserver
```

## Endpoints

`POST /api/calculate/`

Request body:

```json
{
  "operand1": 10,
  "operand2": 5,
  "operation": "add"
}
```

Supported operations:

- `add`
- `subtract`
- `multiply`
- `divide`

Example response:

```json
{
  "id": 1,
  "operand1": 10.0,
  "operand2": 5.0,
  "operation": "add",
  "result": 15.0,
  "created_at": "2026-05-18T10:00:00Z"
}
```

Each calculation is saved in the database.

`GET /api/calculations/`

Returns calculation history.

`GET /api/calculations/<id>/`

Returns one saved calculation.
