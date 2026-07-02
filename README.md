# Trekking Management Application (TMA)

## Overview

The Trekking Management Application (TMA) is a web-based platform designed to manage trekking events and bookings. The system supports three types of users:

* Admin
* Trek Staff
* Trekker

The application allows administrators to manage treks and staff members, staff users to oversee assigned treks, and trekkers to browse and book available trekking events.

## Technology Stack

### Backend

* Flask
* Flask-SQLAlchemy
* Flask-Security

### Frontend

* Vue.js
* Bootstrap

### Database

* SQLite

### Additional Components

* Redis (Caching)
* Celery (Background Jobs)

## Expected Project Structure

The project structure is currently planned as follows and may be refined during development:

```text
tma_v2/
│
backend/
│
├── application/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── trek.py
│   │   ├── booking.py
│   │   └── staff_profile.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── admin.py
│   │   ├── staff.py
│   │   └── trekker.py
│   │
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   └── seed.py
│
├── requirements.txt
└── run.py
```

## Planned Features

* User Authentication and Authorization
* Trek Management
* Trek Booking System
* Role-Based Access Control
* Caching using Redis
* Background Jobs using Celery
* Reports and Analytics
* Export Functionality

## Milestone Status

### Milestone 0

* [x] Project repository created
* [x] Initial README added
* [ ] Backend setup
* [ ] Database schema implementation
* [ ] Authentication system
* [ ] Trek management module
* [ ] Booking management module
* [ ] Caching and background jobs
* [ ] Reports and export features
* [ ] Project deployment

```
```
