# Cinema Management System — Flask + ReactJS + PostgreSQL

A full-stack web application to manage cinema operations: **movies, showtimes, rooms, seats, tickets, snack combos, users, and payments** — built with **Flask**, **ReactJS**, and **PostgreSQL**, featuring **JWT authentication** and **Swagger API documentation**.

---

## Features

- **JWT Authentication** (login/register, role-based access)
- **Movie Management** (CRUD movies, genres, duration)
- **Room & Seat Management** (custom layouts)
- **Showtime Scheduling**
- **Ticket Booking & Payment**
- **Snack Combos** management
- **Integrated Payment Module**
- **Swagger UI API Docs**
- **CORS-enabled API** for frontend integration

---

## Project Structure

```text
WEB_CINEMA/
├── backend/                      # Flask backend (API server)
│   ├── app.py                    # Flask app factory + entrypoint
│   ├── config.py                 # Config (DB, JWT, Swagger, CORS)
│   ├── models.py                 # SQLAlchemy models (optional split per module)
│   ├── controllers/              # Business logic per domain
│   ├── routes/                   # Blueprints: auth, movie, room, seat, tickets, showtime, cinema, payments, combo, user, ticket_type
│   ├── swagger/                  # Swagger YAML specs
│   └── ...
│
├── frontend/                     # ReactJS (Vite)
│   ├── src/
│   ├── package.json
│   └── ...
│
├── requirements.txt              # Python dependencies (root)
├── runtime.txt                   # Python version for Render (e.g., python-3.12.3)
├── render.yaml                   # Optional: one-click multi-service deploy on Render
└── README.md
```

---

## Tech Stack

- **Backend:** Flask, Flask-SQLAlchemy, Flask-JWT-Extended, Flasgger, Flask-CORS, Gunicorn  
- **Frontend:** ReactJS (Vite), React Router, TailwindCSS
- **Database:** PostgreSQL (SQLAlchemy ORM)  
- **Hosting:** Render (Web Service + Static Site + PostgreSQL)

---

## Getting Started

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r ../requirements.txt
python app.py
```

Backend runs at: **http://127.0.0.1:5000**

###  Frontend Setup

```bash
cd ../frontend
npm install
npm run dev
```

Frontend runs at: **http://127.0.0.1:5173**

---

## Environment Variables

Create a `.env` file in the `backend/` folder:

```env
FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5432/web_cinema
```

---

## API Documentation

After running the backend, open **Swagger UI** at:

[http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs)

---

## ☁️ Deployment (Render)

1. Create a **PostgreSQL** database on Render.  
2. Deploy **Flask API** as a **Web Service** (build command: `pip install -r requirements.txt`, start command: `gunicorn app:app`).  
3. Deploy **React app** as a **Static Site** (build command: `npm run build`, publish directory: `dist`).  
4. Add environment variables on Render for secrets and DB credentials.  

Optional: use the included `render.yaml` for **one-click deploy**.

---

## Members

| Name | Role |
|------|------|
| **Nguyễn An Đức** | Backend Developer |
| **Đoàn Hoài Việt** | Frontend Developer |

---
