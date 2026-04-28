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
- Infermedica API credentials
- [Docker](https://www.docker.com/) with Docker Compose
- Python 3.10+ (only for local development)
- Node.js 18+ (only for local development)

---

## Environmental variables

Before running the application, cope environmental variables from .env.example files:

```bash
# Backend (setting infermedica credentials required)
cp backend/.env.example backend/.env

# Frontend (optional when using docker command)
cp frontend/.env.example frontend/.env
```

## Running application

In order to start full-stack application with a single command, run:

```bash
docker compose up --build
```