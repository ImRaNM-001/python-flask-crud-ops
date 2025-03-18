# Use Python 3.12 slim image as the base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=3100

# Copy requirements first to leverage Docker cache (layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port the app runs on
EXPOSE ${PORT}

# Run the application
ENTRYPOINT ["python3"]

CMD ["flask_crud_ops.py"]