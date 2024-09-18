# Base image
FROM python:3.11-alpine

# Install system dependencies
# RUN apt-get update && apt-get install -y \
#     gcc \
#     libpq-dev \
#     python3-dev \
#     build-essential \
#     libjpeg-dev \
#     zlib1g-dev


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files
COPY . /app

# Expose port 8000 for the Django application
EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]