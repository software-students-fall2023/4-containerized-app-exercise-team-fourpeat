# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libasound2-dev \
    portaudio19-dev \
    flac \
    pulseaudio \
    # other dependencies if needed
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock into the container at /usr/src/app
COPY Pipfile Pipfile.lock ./

# Install dependencies from Pipfile
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application's code
COPY . .

# Make port 8000 available to the world outside this container
# EXPOSE 8000

# Define environment variable
ENV NAME mlclientdocker

# Run app.py using pipenv to ensure the correct Python environment
CMD ["pipenv", "run", "python", "./machine-learning-client/ml.py"]
