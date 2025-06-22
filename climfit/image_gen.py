from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to("cpu")  

def generate_image(prompt: str,
                   steps: int = 20,
                   width: int = 512,
                   height: int = 512,
                   out_path: str = "outfit.png") -> str:
   
    image = pipe(prompt,
                 num_inference_steps=steps,
                 width=width,
                 height=height).images[0]
    image.save(out_path)
    return out_path
