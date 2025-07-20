# Use official Python image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 3000

# Run the application
CMD ["python", "app.py"]

