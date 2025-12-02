# Cinema Management System — Flask + ReactJS + PostgreSQL

A full-stack web application to manage cinema operations: movies, showtimes, rooms, seats, tickets, snack combos, users, and payments — with JWT authentication and Swagger API docs.

---

##  Project Structure

WEB_CINEMA/
│
├── backend/ # Flask backend (API server)
│ ├── app.py # Flask app factory + entrypoint
│ ├── config.py # Config (DB, JWT, Swagger, CORS)
│ ├── models.py # SQLAlchemy models (optional split per module)
│ ├── controllers/ # Business logic per domain
│ ├── routes/ # Blueprints: auth, movie, room, seat, tickets, showtime, cinema, payments, combo, user, ticket_type
│ ├── swagger/ # Swagger YAML specs (Flasgger)
│ └── ...
│
├── frontend/ # ReactJS SPA (Vite or CRA)
│ ├── src/
│ ├── package.json
│ └── ...
│
├── requirements.txt # Python dependencies (root)
├── runtime.txt # Python version for Render (e.g., python-3.12.3)
├── render.yaml # (Optional) One-click multi-service deploy on Render
└── README.md


---

## Tech Stack

- **Backend:** Flask, Flask-SQLAlchemy, Flask-JWT-Extended, Flasgger, Flask-CORS, Gunicorn  
- **Frontend:** ReactJS (Vite/CRA), Axios, React Router, TailwindCSS or Bootstrap  
- **Database:** PostgreSQL (SQLAlchemy ORM)  
- **Hosting:** Render (Web Service + Static Site + PostgreSQL)

---

## Getting Started

###  Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r ../requirements.txt
python app.py

### Frontend setup
cd ../frontend
npm install
npm run dev

---

### Members
| Name                  | Role                  |
| --------------------- | --------------------- |
| **Nguyễn An Đức**     | Backend Developer     |
| **Đoàn Hoài Việt**    | Frontend Developer    |
