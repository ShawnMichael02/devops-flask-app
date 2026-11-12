
# Use Python as the base image
FROM python:3.14

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Flask and Redis dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Expose Flask's default port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
