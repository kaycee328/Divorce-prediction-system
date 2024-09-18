# Base image
FROM python:3.11-alpine

# Install system dependencies for Alpine
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    linux-headers \
    jpeg-dev \
    zlib-dev \
    libffi-dev \
    libjpeg-turbo-dev \
    build-base \
    python3-dev \
    py3-pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files
COPY . /app

# Expose port 8000 for the Django application
EXPOSE 8000

# Command to run the Django application
CMD [ "python", "./divorce-prediction-system/manage.py", "runserver", "0.0.0.0:8000" ]
