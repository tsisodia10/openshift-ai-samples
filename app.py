import openai
import gradio as gr
import os
import threading
import time
import psutil
from prometheus_client import start_http_server, Counter, Histogram, Gauge

# Start Prometheus client
start_http_server(8000)  # Exposes metrics at http://localhost:8000

# Define metrics
REQUESTS = Counter('generate_response_total', 'Total number of generate_response calls')
MEMORY_USAGE = Gauge('application_memory_usage_bytes', 'Memory usage of the application')
CPU_USAGE = Gauge('application_cpu_usage_seconds_total', 'Total CPU time used by the application')

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_KEY")

def generate_response(prompt, max_tokens=50):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens
    )
    REQUESTS.inc()  # Increment request count
    return response.choices[0].text

def generate_response_with_gradio(prompt, max_tokens=50):
    response = generate_response(prompt, max_tokens)
    return response

iface = gr.Interface(
    flagging_dir="/tmp/flagged",
    fn=generate_response_with_gradio,
    inputs="text",
    outputs="text",
    layout="horizontal",
    title="Few-Shot Prompting",
    description="Enter a text prompt.",
    capture_session=True
)

def collect_metrics():
    process = psutil.Process(os.getpid())
    while True:
        MEMORY_USAGE.set(process.memory_info().rss)  # RSS: Resident Set Size
        CPU_USAGE.set(process.cpu_times().user)
        time.sleep(5)  # Update metrics every 5 seconds

metrics_thread = threading.Thread(target=collect_metrics)
metrics_thread.start()

if __name__ == '__main__':
    iface.launch()

