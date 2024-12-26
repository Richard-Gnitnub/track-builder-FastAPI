# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the FastAPI app runs on
EXPOSE 8000

# Set the command to run the FastAPI app
CMD ["uvicorn", "track_app.__init__:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
