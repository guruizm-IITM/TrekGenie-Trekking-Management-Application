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
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── extensions.py
│   ├── seed.py
│   ├── requirements.txt
│   └── instance/
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── components/
│
├── screenshots/
│
├── docs/
│
└── README.md
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
