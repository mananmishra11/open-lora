# syntax=docker/dockerfile:1

# Base image: Python 3.8
FROM python:3.8-slim-buster

# Set current directory as working directory
WORKDIR /

# Intall required Python packages
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy source code
COPY . .

# Run
CMD [ "python3", "-u", "master.py" ]