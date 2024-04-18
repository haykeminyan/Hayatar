# Use a base image with Python installed
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install required packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Define the environment variable for the bot token
ENV BOT_TOKEN="6425359689:AAFlmH2c6nma0zvVbr4ABCPgRVoQcGS40hk"
ENV WEATHER_API_KEY="3171b2c37c2a09802dd0b45d114c4d2a"

# Expose port 443 for HTTPS communication
EXPOSE 443

