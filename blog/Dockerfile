# Gunakan official Python runtime sebagai base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Expose port 8000 untuk mengakses container dari luar
EXPOSE 8000

# Jalankan perintah untuk menjalankan server
CMD ["python", "blog/manage.py", "runserver", "0.0.0.0:8000"]
