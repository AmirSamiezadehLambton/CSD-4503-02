# How we can define the OS?
# Docker images can be selected from: https://hub.docker.com/search

# Base image using "FROM" keyword
FROM python:3.9-alpine

# Define the working directory
WORKDIR /

# Copy the files from the project to the image
# COPY <local_files> <image_files>
COPY . .

# Install the libraries in the docker image
RUN pip install -r requirements.txt

# To open the port to access the application
EXPOSE 5000

# To run the application
CMD ["python", "main.py"]