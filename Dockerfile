# Use the official Python image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and gunicorn
RUN pip install --no-cache-dir Flask gunicorn

# Expose port 3000
EXPOSE 3000

# Run the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "app:app"]
