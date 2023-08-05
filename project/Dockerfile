# Use the official Python image as the base image
FROM python:3

# Set environment variables (if needed)
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port your Django app will listen on
EXPOSE 8000

# Command to run your Django app (use gunicorn, uWSGI, etc. for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]