<p align="center">
    <img src="screenshots/logo-primary.png" width="180">
</p>

<h1 align="center">🏔 TrekGenie</h1>

<p align="center">
A Modern Full-Stack Trek Management System
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![Vue.js](https://img.shields.io/badge/Vue.js-3-42b883?logo=vuedotjs&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-Cache-red?logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-Background%20Jobs-37814A?logo=celery&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)

</p>

## 🌟 Highlights

- 🏔 Full-Stack Trek Management System
- 🔐 JWT-based Authentication & Role-Based Access Control
- ⚡ Redis Caching for Optimized Performance
- 📧 Celery & Celery Beat for Background Jobs
- 📄 Asynchronous CSV Export
- 📈 Automated Monthly Reports
- 🎨 Modern Vue.js Interface with TrekGenie Branding
- 📱 Responsive Bootstrap 5 Design

---

# 📖 About TrekGenie

TrekGenie is a full-stack web application developed for managing trekking expeditions. It provides a complete ecosystem where administrators can organize treks, assign staff, monitor bookings, and manage users, while trekkers can browse adventures, make bookings, track payment status, and export their trekking history.

The project demonstrates the integration of modern backend services such as Redis caching, Celery background jobs, JWT authentication, and RESTful APIs with a responsive Vue.js frontend.

---

# ✨ Key Features

## 👨‍💼 Administrator

- Secure JWT Authentication
- Dashboard with real-time statistics
- Create, edit and delete treks
- Assign staff to treks
- Search users, staff and treks
- Activate/Deactivate users and staff
- View all bookings

---

## 🥾 Staff

- Secure login
- Dashboard showing:
  - Assigned treks
  - Active treks
  - Completed treks
- View all assigned trekking expeditions

---

## 🎒 Trekker

- Browse available treks
- Book trekking expeditions
- View booking history
- Track payment status
- Export booking history as CSV
- Receive automated reminder emails before upcoming treks

---

# ⚙️ Background Jobs (Celery)

## 📧 Daily Trek Reminder

Automatically sends reminder emails one day before the scheduled trek containing:

- Trek Name
- Location
- Start Date
- Things to Carry
- Trek Instructions

---

## 📈 Monthly Activity Report

Automatically generates an HTML report containing:

- Total Treks
- Total Bookings
- Total Participants
- Most Popular Trek

The report is emailed to the Administrator every month.

---

## 📄 Export Booking History

Users can export their complete trekking history as a CSV file.

The export runs asynchronously using Celery and is automatically emailed to the user once completed.

---

# ⚡ Performance & Optimization

- Redis Caching
- Cached Trek APIs
- Automatic Cache Invalidation
- Optimized Dashboard APIs
- JWT Protected Routes
- Role-Based Authorization

---

# 🛠 Technology Stack

## Backend

- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- Flask CORS
- Flask Caching
- Celery
- Redis

---

## Frontend

- Vue.js 3
- Vue Router
- Axios
- Bootstrap 5

---

## Database

- SQLite

---

# 📂 Project Structure

```
backend
│
├── application
│   ├── models
│   ├── routes
│   ├── services
│   ├── tasks.py
│   ├── exports.py
│   └── mail.py
│
├── seed.py
├── seed_demo_data.py
├── celery_worker.py
└── run.py


frontend
│
├── src
│   ├── assets
│   ├── components
│   ├── router
│   ├── services
│   └── views
│
└── package.json
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone <repository-url>

cd TrekGenie
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Backend

```bash
python run.py
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# ⚙️ Background Services

## Redis

```bash
redis-server
```

---

## MailHog

```bash
MailHog
```

Open:

```
http://localhost:8025
```

---

## Celery Worker

```bash
python -m celery -A celery_worker.celery worker --loglevel=info
```

---

## Celery Beat

```bash
python -m celery -A celery_worker.celery beat --loglevel=info
```

---

# 👤 Default Administrator

| Email | Password |
|--------|----------|
| admin@trekgenie.com | admin123 |

---

# 🌱 Demo Data

To populate the application with demo users, staff members, treks and bookings:

```bash
python seed_demo_data.py
```

Demo Credentials

| Role | Email | Password |
|------|------|----------|
| Staff | rahul@trekgenie.com | staff123 |
| Trekker | amit@test.com | password123 |

---

# 📸 Application Screenshots

## Login Page

![Login](screenshots/login.png)

---

## Administrator Dashboard

![Admin Dashboard](screenshots/admin-dashboard.png)

---

## Trek Management

![Trek Management](screenshots/trek-management.png)

---

## Staff Management

![Staff Management](screenshots/staff-management.png)

---

## Trekker Dashboard

![Trekker Dashboard](screenshots/trekker-dashboard.png)

---

## Browse Treks

![Browse Treks](screenshots/browse-treks.png)

---

## Booking History

![Bookings](screenshots/bookings.png)

---

## Monthly Activity Report

![Monthly Report](screenshots/monthly-report.png)

---

# 📌 Future Enhancements

- Integrated Online Payment Gateway
- Google Maps Integration
- Weather Forecast Integration
- Trek Reviews & Ratings
- Mobile Application
- QR Code Based Trek Check-in
- AI-powered Trek Recommendation System

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- RESTful API Design
- JWT Authentication & Authorization
- Role-Based Access Control (RBAC)
- Background Job Scheduling using Celery
- Redis Caching
- Asynchronous Processing
- Vue.js Single Page Applications
- Flask Backend Development
- SQLAlchemy ORM
- Responsive UI Design

---

# 👨‍💻 Author

**Abhishek Guru**

BS in Data Science and Applications  
Indian Institute of Technology Madras

2026

---

<p align="center">
Made with ❤️ using Flask, Vue.js, Redis & Celery
</p>