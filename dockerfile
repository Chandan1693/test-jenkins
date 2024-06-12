# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Install cowsay
RUN apt-get update && apt-get install -y cowsay

# Copy the rest of the working directory contents into the container
COPY . .

# Set the default command to run the script with an argument
ENTRYPOINT ["python", "say.py"]

