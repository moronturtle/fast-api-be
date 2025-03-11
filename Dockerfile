# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Set PYTHONPATH
ENV PYTHONPATH=/app

# Copy files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Alembic migrations before starting FastAPI
# CMD alembic upgrade head && python app/db/seed_data.py && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
CMD bash -c "alembic upgrade head && python app/db/seed_data.py && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"
