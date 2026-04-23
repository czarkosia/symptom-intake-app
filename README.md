# Symptom Intake App

## Technology stack

* **Backend:** Python, FastAPI
* **Frontend:** Vue.js 3, Vite
* **Infrastructure:** Docker, Docker Compose

---

## Project structure (Monorepo)

This monorepo contains:

- `/backend` - Application logic and REST API (FastAPI)
- `/frontend` - User interface (Vue.js)

---

## Requirements

In order to run the project, make sure you have:
- [Docker](https://www.docker.com/) with Docker Compose
- Python 3.10+ 
- Node.js 18+

---

## Environmental variables

Before running the application, cope .env variables from .env.example files:

```bash
# Dla backendu
cp backend/.env.example backend/.env

# Dla frontendu
cp frontend/.env.example frontend/.env