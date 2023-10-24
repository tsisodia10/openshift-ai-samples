FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

USER root

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt 

RUN mkdir /tmp/flagged && \
    chmod -R 777 /tmp/flagged

# Adjust permissions for /app to ensure all content has appropriate permissions
RUN chown -R root:root /app

# Copy the current directory contents into the container at /app
COPY . .

# Define an environment variable for the OpenAI API key (no value is set)
ENV OPENAI_KEY=""

EXPOSE 7860

# Run the Gradio app when the container launches
CMD ["python3", "app.py"]