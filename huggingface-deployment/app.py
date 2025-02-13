import gradio as gr
from fastai import *
from fastai.vision.all import *

model = load_learner('fruit_recognizer_v3.pkl')

labels = (
    'Banana', 'Coconut', 'Guava', 'Hog Plum', 'Jackfruit', 'Litchi', 'Mango', 'Papaya', 'Starfruit', 'Watermelon', 'Wood Apple'
)

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(labels, map(float, probs)))

image = gr.Image()
label = gr.Label()
examples = [
    'unknown_001.jpg',
    'unknown_002.jpg',
    'unknown_003.jpg',
    'unknown_004.jpg',
    'unknown_005.jpg',
    ]

demo = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
demo.launch(inline=False)