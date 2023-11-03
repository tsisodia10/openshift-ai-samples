FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org gradio prometheus_client

# Port 7860 available to the world outside this container
EXPOSE 7860

# Port 8000 available for Prometheus metrics
EXPOSE 8000

# Define environment variable for gradio to run on port 7860
ENV GRADIO_SERVER_PORT 7860

# Run the provided code when the container launches
CMD ["python", "app3.py"]
