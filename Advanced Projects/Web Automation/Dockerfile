# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY appOld/requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the image
COPY . /app

# Expose the port that Flask will run on
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app/app.py"]
