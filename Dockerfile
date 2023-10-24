FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENAI_KEY=""

EXPOSE 7860

CMD ["python3", "./app.py"]
