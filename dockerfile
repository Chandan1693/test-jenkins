# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . .

# Expose the port Flask will run on
EXPOSE 8000

# Set the default command to run the Flask app
ENTRYPOINT ["python", "say.py"]

