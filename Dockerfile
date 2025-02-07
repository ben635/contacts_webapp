# Use Python official image as base
FROM python:3.13.2

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Copy pipfile
COPY ./Pipfile.lock ./Pipfile.lock
COPY ./Pipfile ./Pipfile

# Install system dependencies
RUN pip install pipenv

# Install dependencies from Pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile

# Set work directory
WORKDIR /app

# Copy project files
COPY ./app .

# Create tables in sqlite db
RUN python manage.py migrate

# Expose port
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]