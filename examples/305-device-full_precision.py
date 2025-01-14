import sdkit
from sdkit.models import load_model
from sdkit.generate import generate_images

context = sdkit.Context()
context.half_precision = False # loads in full precision (i.e. float32, instead of float16). consumes more VRAM
context.model_paths['stable-diffusion'] = 'D:\\path\\to\\sd-v1-4.ckpt'

load_model(context, 'stable-diffusion')

# generate image
images = generate_images(context, prompt='Photograph of an astronaut riding a horse', seed=42, width=512, height=512)
images[0].save(f'image.jpg')
