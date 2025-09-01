# Secrets Management Microservice (FastAPI)

A production-ready FastAPI microservice for securely storing, rotating, and providing secrets (API keys, credentials) to other microservices, with audit logging and access control.

## Features
- REST API for secret storage, retrieval, and rotation
- Access control and audit logging
- Integration-ready for other microservices
- Unit and integration tests (pytest)
- Dockerised for deployment

## Project Structure
- `app/` — Source code
- `tests/` — Unit and integration tests
- `.env.example` — Example environment variables
- `requirements.txt` — Python dependencies
- `Dockerfile` — Containerisation
- `docker-compose.yml` — Multi-service orchestration
- `README.md` — Documentation

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run the service locally: `uvicorn app.secrets_service:app --reload`
3. Run tests locally: `pytest`
4. Build and run with Docker:
	 - Start the service: `docker-compose up --build`
	 - Run tests inside the container:
		 `docker-compose exec secrets-service env PYTHONPATH=/app pytest /app/tests`

## API Endpoints
- `POST /secrets` — Create a new secret
- `GET /secrets/{secret_id}` — Retrieve a secret
- `POST /secrets/{secret_id}/rotate` — Rotate a secret
- `GET /audit` — Get audit logs

## Environment Variables
See `.env.example` for configuration options.

## License
MIT
