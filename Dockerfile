# Use an official Python runtime as a parent  image
FROM ubuntu:22.04

# Set non-interactive timezone configuration
ENV DEBIAN_FRONTEND=noninteractive


# Set the working directory in the container
WORKDIR /app

# Install Python, pip, and essential build tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python3", "manage.py", "runserver", "--insecure", "0.0.0.0:8010"]
