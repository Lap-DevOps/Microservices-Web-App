# Use the official Python 3.9.0 base image
FROM python:3.9.18-alpine

# Set the environment variable to prevent Python from buffering output
ENV PYTHONUNBUFFERED 1


# Set the working directory inside the container
WORKDIR /app


# Copy the requirements file to the container and install dependencies
COPY requirements.txt /app/requirements.txt
RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev && \
    pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory to the container
COPY . /app/
ENV DOCKERIZE_VERSION v0.7.0

RUN apk update --no-cache \
    && apk add --no-cache wget openssl \
    && wget -O - https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar xzf - -C /usr/local/bin \
    && apk del wget

# Command to run the Django development server on all available network interfaces


# The -t flag is used to specify the name and optionally a tag to the image
# Example build command: docker build -t your_image_name .