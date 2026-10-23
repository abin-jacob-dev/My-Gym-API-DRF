# My Gym API

A RESTful backend for managing gyms, membership plans, memberships, users, students and payments. Built with Django and Django REST Framework (DRF), with token-based authentication. Supports two roles: **gym owners (admin)** and **members**.

## API Documentation

Full, interactive API documentation (request/response examples) is published on Postman:

👉 https://documenter.getpostman.com/view/53849222/2sBYHUSzNS

## Features

- User signup / login / logout with token authentication
- Role-based access: gym owners vs members
- Gym CRUD (list, create, detail) with owner assignment
- Membership plans per gym (list, create, detail)
- Membership management per gym and user
- Payment creation, listing, detail, history (paginated) and status updates
- Student records CRUD
- Owner-only endpoints (gym user list search/pagination, payment status update)

## Tech Stack

- Python 3.13
- Django 6.0.5
- Django REST Framework
- Token authentication (`rest_framework.authtoken`)
- SQLite (default dev database)

## Project Structure

```
my_gym/
├── manage.py
├── my_gym/          # Project config (settings, urls, wsgi/asgi)
├── accounts/        # User model, auth (signup/login/logout/profile), students
├── gyms/            # Gym, Plan, Membership models and views
├── payments/        # Payment model and views
└── db.sqlite3       # Dev database
```

## Getting Started

### Prerequisites

- Python 3.10+

### Setup

```bash
git clone <repo-url>
cd my_gym
python -m venv .venv
source .venv/bin/activate
pip install django djangorestframework
python manage.py migrate
python manage.py createsuperuser   # optional, for admin panel
python manage.py runserver
```

Server runs at `http://127.0.0.1:8000/`.

## Authentication

1. `POST /auth/signup/` — create a user (username, password, email, phone, role).
2. `POST /auth/login/` — returns a token.
3. Send `Authorization: Token <token>` header on protected endpoints.
4. `POST /auth/logout/` — invalidates the token.

Phone must be 10 digits starting with 7/8/9. Password minimum 8 characters.

## API Endpoints

Base URL: `http://127.0.0.1:8000`

### Auth (`/auth/`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/auth/signup/` | Public | Register a user |
| POST | `/auth/login/` | Public | Login, returns token |
| POST | `/auth/logout/` | Token | Logout |
| GET/PATCH/PUT | `/auth/profile/` | Token | View/update own profile |
| GET | `/auth/users/?p=&search=` | Owner | Paginated member list (search by username) |
| GET/POST | `/auth/students/` | Public | List / create students |
| GET/PATCH/PUT/DELETE | `/auth/student/<id>/` | Public | Retrieve/update/delete student |

### Gyms (`/gyms/`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/gyms/` | Public | List gyms |
| POST | `/gyms/create/` | Owner | Create gym (owner auto-set) |
| GET | `/gyms/<id>/` | Public | Gym detail |

### Plans (`/gyms/<gym_id>/plans/`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/gyms/<gym_id>/plans/` | Public | List plans |
| POST | `/gyms/<gym_id>/plans/create/` | Owner | Create plan |
| GET | `/gyms/<gym_id>/plans/<id>/` | Public | Plan detail |

### Membership (`/gyms/<gym_id>/membership/`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/gyms/<gym_id>/membership/` | Token | List memberships |
| POST | `/gyms/<gym_id>/membership/create/` | Owner | Create membership (end_date auto-calculated from plan duration) |
| GET | `/gyms/<gym_id>/membership/<id>/` | Token | Membership detail (member sees own only) |

### Payments (`/payments/`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/payments/` | Token | Current user's payments |
| POST | `/payments/create/` | Token | Create payment (status defaults to completed) |
| GET | `/payments/detail/<id>/` | Token | Payment detail (owner sees all) |
| GET | `/payments/history/?p=` | Token | Paginated payment history |
| PATCH | `/payments/status/<id>/` | Owner | Update payment status |

### Admin

Django admin available at `/admin/`.

## Models

- **User** (extends AbstractUser): role (member/owner), phone.
- **Gym**: name, address, owner (FK User).
- **Plan**: name, price, duration_days.
- **Membership**: user, plan, status (active/expired/cancelled), start_date, end_date.
- **Payment**: user, membership, amount, status (pending/completed/failed), method (card/upi/cash/net_banking), payment_date.
- **Student**: name, age, place.

## Notes

- `DEBUG=True` and a hardcoded `SECRET_KEY` are set for development; update before production deployment.
- SQLite is used for development; configure a production database in `settings.py`.
- CORS/ALLOWED_HOSTS must be configured for production.
- For complete request/response examples, see the Postman documentation link above.

## License

No license specified.