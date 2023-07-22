# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "main.py"]
