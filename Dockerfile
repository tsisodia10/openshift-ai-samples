FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Define an environment variable for the OpenAI API key (no value is set)
ENV OPENAI_KEY=""

EXPOSE 7860

# Run the Gradio app when the container launches
CMD ["python3", "app.py"]
