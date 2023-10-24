import openai
import gradio as gr
import os

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_KEY")

def generate_response(prompt, max_tokens=50):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text

def generate_response_with_gradio(prompt, max_tokens=50):
    response = generate_response(prompt, max_tokens)
    return response

iface = gr.Interface(
    fn=generate_response_with_gradio,
    inputs="text",
    outputs="text",
    layout="horizontal",
    title="Few-Shot Prompting",
    description="Enter a text prompt.",
    capture_session=True
)

if __name__ == '__main__':
    iface.launch()

