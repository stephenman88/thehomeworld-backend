# Use the official Python image from the DockerHub
FROM python:3.10-slim

# Set the working directory in docker
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

USER django-user