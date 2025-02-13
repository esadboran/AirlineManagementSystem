# ✈ Airline Management System

The **Airline Management System** is a web-based application designed to manage airline operations efficiently. This system allows users to handle flights, reservations, and airplane details using a **RESTful API** built with **Django** and **Django REST Framework**.

---

## 🚀 Features
- 🛬 **Manage airplanes** with details such as capacity, production year, and status.
- ✈ **Create and track flights**, including departure, arrival, and assigned airplanes.
- 🎫 **Make and manage reservations** for passengers.
- 🔎 **Search and filter data** using advanced query capabilities.
- 🔒 **Secure API endpoints** for managing airline operations.

> This project serves as a foundation for an airline management system and can be extended with additional features such as **payment integration**, **real-time flight tracking**, and **user authentication**.

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/esadboran/AirlineManagementSystem.git
cd AirlineManagementSystem
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install essential dependencies manually:
```bash
pip install djangorestframework django-filter
```

### 4️⃣ Update `settings.py`
#### 📧 Email Backend Configuration
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
#### ⚙ Django REST Framework Configuration
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```
#### 🔌 Installed Apps
Ensure the following applications are added to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'airline',  # Application
    'django_filters', # Filter
]
```

### 5️⃣ Apply Migrations
```bash
python manage.py migrate
```

### 6️⃣ Run the Server
```bash
python manage.py runserver
```
The server will be available at: **`http://127.0.0.1:8000/`**

---

## 📌 API Endpoints

### ✈ Airplane API
| Method | Endpoint                  | Description |
|--------|---------------------------|-------------|
| **GET** | `api/airplanes/`          | List all airplanes |
| **GET** | `api/airplanes/{id}/`        | Get details of a specific airplane |
| **GET** | `api/airplanes/{id}/flights` | Get flights of a specific airplane |
| **POST** | `api/airplanes/`             | Add a new airplane |
| **PATCH** | `api/airplanes/{id}/`        | Update a specific airplane |
| **DELETE** | `api/airplanes/{id}/`        | Delete a specific airplane |

#### ➕ Add a new airplane
```json
{
  "tail_number": "ABC123",
  "model": "Boeing 737",
  "capacity": 180,
  "status": true,
  "production_year": 2015
}
```

---

### 🛫 Flight API
| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `api/flights/` | List all flights |
| **GET** | `api/flights/{id}/` | Get details of a specific flight |
| **GET** | `api/flights/{id}/reservations` | Get reservations for a specific flight |
| **POST** | `api/flights/` | Add a new flight |
| **PATCH** | `api/flights/{id}/` | Update a specific flight |
| **DELETE** | `api/flights/{id}/` | Delete a specific flight |

#### ➕ Add a new flight
```json
{
  "flight_number": "TK1234",
  "departure": "Istanbul",
  "destination": "London",
  "departure_time": "2025-03-01T12:00:00Z",
  "arrival_time": "2025-03-01T15:00:00Z",
  "airplane": 1
}
```

---

### 🎟 Reservation API
| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `api/reservations/` | List all reservations |
| **GET** | `api/reservations/{id}/` | Get details of a specific reservation |
| **POST** | `api/reservations/` | Add a new reservation |
| **PATCH** | `api/reservations/{id}/` | Update a specific reservation |

#### ➕ Add a new reservation
```json
{
  "passenger_name": "John Doe",
  "passenger_email": "johndoe@example.com",
  "flight": 1,
  "status": true,
  "reservation_code": "ABC123"
}
```
---
## Data Validation Rules
The system enforces several validation rules to maintain data integrity:

- **Airplane**
  - Tail number must be unique and alphanumeric.
  - Model name must be at least 3 characters long.
  - Capacity must be a positive number.
  - Production year must be between 1903 and the current year.


- **Flight**
  - Flight number must be unique.
  - Departure and destination must be at least 3 characters long and cannot be the same.
  - Departure time must be in the future.
  - Arrival time must be later than departure time.


- **Reservation**
  - Passenger name must be at least 3 characters long.
  - Passenger email must be valid.
  - Flights cannot be booked if capacity is full.
  - Reservation status must be either `true` or `false`.

These rules help ensure that the system operates efficiently and avoids common data errors.

---

## 🔍 Advanced Filtering  

This system supports advanced filtering options for retrieving specific data efficiently. You can apply various filters to refine search results when making API requests.  

### ✈️ Airplane Filtering  
Filter airplanes based on:  
- **Tail Number** (`icontains`): Partial match on the tail number.  
- **Model** (`icontains`): Search for specific airplane models.  
- **Status** (`boolean`): Filter active/inactive airplanes.  
- **Production Year** (`gte`, `lte`): Get airplanes produced within a specific time range.  
- **Capacity** (`gte`, `lte`): Filter airplanes based on seat capacity.  

### 🛫 Flight Filtering  
Refine flights using:  
- **Flight Number** (`icontains`): Search flights by partial flight number.  
- **Departure & Destination** (`icontains`): Find flights based on origin and destination cities.  
- **Departure & Arrival Time** (`gte`, `lte`): Filter flights within specific time frames.  
- **Airplane** (`exact`): Retrieve flights based on assigned airplane.  

### 🎟️ Reservation Filtering  
Search for reservations using:  
- **Passenger Name & Email** (`icontains`): Look up reservations by passenger details.  
- **Flight** (`exact`): Filter reservations by flight ID.  
- **Status** (`boolean`): Retrieve active or canceled reservations.  
- **Reservation Code** (`iexact`): Find reservations using a specific code.  
- **Created Date** (`gte`, `lte`): Get reservations made within a particular time frame.  

These filtering options enable precise data retrieval and improve API usability! 🚀  

---

## 🛠 API Testing with Postman  
You can test this API using **Postman** by importing the collection with the following link:  

[📂 Airline Management System Postman Collection](https://raw.githubusercontent.com/esadboran/AirlineManagementSystem/main/AirlineManagementSystem.postman_collection.json)

---
Esad Boran
---

🚀 Happy coding!

