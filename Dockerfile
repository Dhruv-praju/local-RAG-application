FROM python:3.12

# install system-wide deps for python and node
RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3-dev curl gnupg

# set working directory
WORKDIR /usr/app

# copy our application code to the container
COPY . .

# Install the required Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port the app runs on (update if necessary)
EXPOSE 8080

# Run the application
CMD ["python3", "chat.py"]