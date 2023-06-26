FROM python:3.9-slim-buster

RUN mkdir /results/
RUN mkdir /uploads/

# Set the working directory in the container to /app
WORKDIR /app

COPY ./webui/requirements.txt /app/
# Add the current directory contents into the container at /app
#ADD ./webui /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

COPY ./webui/ /app/

# Run app.py when the container launches
CMD ["python", "app.py"]
