# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Alembic migrations before starting FastAPI
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload