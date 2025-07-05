# Retirement Planner

This project provides a basic scaffold for a retirement planning web application.
It includes a Svelte + Vite frontend and a FastAPI backend. Market data is
fetched from Alpha Vantage with a fallback to Yahoo Finance and cached in Redis.

## Project Structure

```
backend/  - FastAPI app
frontend/ - Svelte + Vite project
shared/   - Pydantic models shared between frontend and backend
```

## Requirements
- Python 3.10+
- Node.js 18+
- Docker (optional for running via `docker-compose`)

## Setup
1. Copy `.env.example` to `.env` and fill in the required values.
2. Install Python dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
   The backend uses **Pydantic v2**, so `pydantic-settings` is also required
   for loading environment variables.

3. Install frontend dependencies:
   ```bash
   cd frontend && npm install
   ```

## Running Locally

With Docker:
```bash
docker-compose up --build
```
This will start the backend on `localhost:8000` and the frontend on `localhost:3000`.

Without Docker:
1. Start Redis locally (`redis-server`).
2. Run the backend:
   ```bash
   uvicorn app.main:app --reload --app-dir backend
   ```
3. Run the frontend:
   ```bash
   cd frontend && npm run dev -- --host 0.0.0.0
   ```

## Endpoints
- `POST /api/user/profile` – store a user profile
- `GET /api/market/{symbol}` – fetch market data
- `POST /api/simulate` – run a Monte Carlo simulation
- `GET /api/recommendations` – get suggested actions

These endpoints are only placeholders and need real implementations.
