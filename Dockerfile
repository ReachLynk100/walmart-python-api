# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app.py .

# Create a non-root user
RUN useradd --create-home appuser && \
    chown -R appuser:appuser /app

USER appuser

# Application port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
