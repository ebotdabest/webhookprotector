import PIL.MicImagePlugin
import flask
from flask import Flask, request
app = Flask(__name__)  # app name

import torch
from diffusers import StableDiffusionPipeline

counter = 0

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)

@app.route("/create")
def create_img():
    global counter
    prompt = request.headers.get("prompt")
    generator = torch.Generator("cuda").manual_seed(1024)

    image = pipe(prompt, num_inference_steps=70, generator=generator).images[0]
    image.save(f"./imgs/{counter}.png")
    counter += 1

    return f"./imgs/{counter}.png"

