# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at the root
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run your app using Gunicorn
# This tells Gunicorn to run the 'app' object from the 'example_app.app' module
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "example_app.app:app"]

