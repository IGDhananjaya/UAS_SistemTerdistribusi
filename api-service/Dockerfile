# Gunakan base image yang sesuai dengan bahasa pemrograman dan runtime yang Anda gunakan
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Salin requirements.txt dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file aplikasi
COPY . .

# Ekspose port yang digunakan oleh aplikasi
EXPOSE 8000

# Tentukan command untuk menjalankan aplikasi
CMD ["python", "app.py"]
