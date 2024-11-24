# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code into the container
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the FastAPI app using Gunicorn with Uvicorn workers
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]

# # Build the Docker image
# docker build -t fastapi-app .

# # Run the Docker container
# docker run -d --name fastapi-app -p 8000:8000 fastapi-app

# # Kill the Docker container
# docker kill fastapi-app