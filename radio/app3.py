import gradio as gr
from prometheus_client import start_http_server, Counter

# Start Prometheus metrics server
start_http_server(8000)

# Create a counter metric
FEEDBACK_COUNTER = Counter("feedback_stars", "Number of feedbacks by stars", ["stars"])

def get_feedback(star):
    # Increment the counter based on the star rating received
    FEEDBACK_COUNTER.labels(stars=str(star)).inc()

    return f"Received {star} star feedback. Thank you!"

# Create Gradio interface
iface = gr.Interface(
    fn=get_feedback,
    inputs=gr.Radio(["1", "2", "3", "4", "5"], label="Star Rating"),
    outputs="text",
    live=True
    
)


iface.launch()
