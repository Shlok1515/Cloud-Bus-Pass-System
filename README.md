# 🚌 Cloud Bus Pass System.

A cloud-native Bus Pass & Ticket Booking Platform built using **FastAPI**, **Streamlit**, **PostgreSQL**, and deployed on **Render**, **Neon PostgreSQL**, and **Streamlit Community Cloud**.

## 🚀 Live Demo

### Frontend

https://cloud-bus-pass-systemgit-erqxrskkb5bzp9qh8nq3wj.streamlit.app/

### Backend API

https://cloud-bus-pass-system-34vc.onrender.com

### API Documentation

https://cloud-bus-pass-system-34vc.onrender.com/docs

---

# 📌 Features

## 👤 User Features

* User Registration
* User Login with JWT Authentication
* Search Available Buses
* Book Bus Tickets
* View Booking History
* QR Code Ticket Generation
* Real-time Ticket Management

## 🚌 Bus Management

* Add New Buses
* View Available Routes
* Manage Bus Details
* Fare Management

## 📊 Admin Dashboard

* Total Users Analytics
* Total Bookings Analytics
* Revenue Analytics
* Bus Performance Metrics
* Route Distribution Analysis
* Popular Bus Tracking

---

# 🏗️ System Architecture

Frontend (Streamlit)
↓
FastAPI Backend (Render)
↓
Neon PostgreSQL Database

---

# 🛠️ Tech Stack

## Frontend

* Streamlit
* Plotly
* Pandas
* Requests

## Backend

* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication
* Passlib

## Database

* PostgreSQL
* Neon PostgreSQL

## Deployment

* Render
* Streamlit Community Cloud
* Docker
* GitHub

---

# 📂 Project Structure

```bash
Cloud-Bus-Pass-System/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── database.py
│   │   ├── security.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── pages/
│   │   ├── 1_Register.py
│   │   ├── 2_Login.py
│   │   ├── 3_Bus_Search.py
│   │   ├── 4_Book_Ticket.py
│   │   ├── 5_My_Bookings.py
│   │   └── 6_Admin_Dashboard.py
│   │
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
└── screenshots/
```

---

# 🗄️ Database Schema

## Users

| Column   | Type    |
| -------- | ------- |
| user_id  | Integer |
| name     | String  |
| email    | String  |
| password | String  |

## Buses

| Column      | Type    |
| ----------- | ------- |
| bus_id      | Integer |
| bus_name    | String  |
| source      | String  |
| destination | String  |
| total_seats | Integer |
| fare        | Integer |

## Bookings

| Column       | Type     |
| ------------ | -------- |
| booking_id   | Integer  |
| user_id      | Integer  |
| bus_id       | Integer  |
| seats_booked | Integer  |
| booking_time | DateTime |

---

# 🔑 API Endpoints

## User APIs

| Method | Endpoint        |
| ------ | --------------- |
| POST   | /users/register |
| POST   | /users/login    |

## Bus APIs

| Method | Endpoint   |
| ------ | ---------- |
| GET    | /buses     |
| POST   | /buses/add |

## Booking APIs

| Method | Endpoint                 |
| ------ | ------------------------ |
| POST   | /bookings/book           |
| GET    | /bookings/user/{user_id} |

## Analytics APIs

| Method | Endpoint                    |
| ------ | --------------------------- |
| GET    | /analytics/summary          |
| GET    | /analytics/bookings-per-bus |

---

# 🐳 Docker Support

## Backend

```bash
docker build -t bus-backend ./backend
```

## Frontend

```bash
docker build -t bus-frontend ./frontend
```

## Docker Compose

```bash
docker compose up --build
```

---

# 📈 Key Highlights

* Full Stack Cloud Project
* JWT Authentication
* RESTful APIs
* QR Code Ticket Generation
* Analytics Dashboard
* Cloud Database Integration
* Dockerized Architecture
* Production Deployment

---

# 🎯 Learning Outcomes

* Backend Development with FastAPI
* Database Design with PostgreSQL
* Cloud Deployment
* Docker Containerization
* API Development
* Authentication & Security
* Data Visualization
* Full Stack Application Development

---

# 👨‍💻 Author

**Shlok Singh**

MCA (Cloud Computing)

Passout Year: 2027

GitHub: https://github.com/Shlok1515

LinkedIn: Add your LinkedIn profile link here

---

⭐ If you found this project useful, consider giving it a star on GitHub.
