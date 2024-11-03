FROM python:3.12

WORKDIR /usr/app

COPY . .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Docker CLI for managing containers
RUN apt-get update && apt-get install -y \
    docker.io && \
    rm -rf /var/lib/apt/lists/*

# Expose the port the app runs on (update if necessary)
EXPOSE 8080

# Run the application
CMD ["python", "chat.py"]