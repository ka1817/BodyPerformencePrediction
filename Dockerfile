# Use official Python image as base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose FastAPI's default port
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

