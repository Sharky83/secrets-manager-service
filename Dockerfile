FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/
COPY tests/ ./tests/
CMD ["uvicorn", "app.secrets_service:app", "--host", "0.0.0.0", "--port", "8000"]
