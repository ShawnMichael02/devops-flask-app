# Use Python as the base image
FROM python:3.14

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install Flask dependencies
RUN pip install --no-cache-dir flask

# Expose Flask's default port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]