# Base image
FROM python:slim-buster

# Set working directory
WORKDIR /usr/src/app

# Copy requirements
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy files
COPY ./app ./

# Starting bot
CMD [ "python", "./main.py" ]