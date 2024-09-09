

from gradio_client import Client
import os
import random
import sys
import shutil
import uuid
from helpers.config import validate_config

'''
# Generates the images from the sentences and config

sentences: list[str] - The sentences to generate images from
config: dict - The config to use for the images
    'model': str - The model to use for the images
    'hf_token': str - The token to use for the model
    'num_inference_steps': int - The number of inference steps to use for the model
    'image': dict - The image to use for the model
        'width': int - The width of the image
        'height': int - The height of the image
    'output_directory': str - The directory to save the images to
'''
def generate_images(sentences, config):
    # extract the values from the config
    model = config["model"]
    hf_token = config["hf_token"]
    num_inference_steps = config["num_inference_steps"]
    width = config["image"]["width"]
    height = config["image"]["height"]
    output_directory = config["output_directory"]

    # validate the config
    if not validate_config(config):
        raise ValueError("Invalid config")
    
    os.makedirs(output_directory, exist_ok=True)
    image_paths = []

    # generate the images
    for i, s in enumerate(sentences):
        client = Client(model, hf_token=hf_token)
        result = client.predict(
            prompt=s,
            seed=random.randint(0, sys.maxsize),
            randomize_seed=True,
            width=width,
            height=height,
            num_inference_steps=num_inference_steps,
            api_name="/infer"
        )
        # save the image to the correct directory
        image_path = save_image(result, output_directory, i)
        image_paths.append(image_path)

    return image_paths

# After generating a image from a sentence, this function will save the image to the output directory
'''
result: tuple - The result from the gradio client
output_directory: str - The directory to save the image to
i: int - The index of the image
'''
def save_image(result, output_directory, i):
    # Handle the returned file path
    if isinstance(result, tuple) and len(result) == 2 and os.path.isfile(result[0]):
        source_path = result[0]
        file_name = f"output_{i + 1}{uuid.uuid4()}.webp"  
        file_path = os.path.join(output_directory, file_name)
        try:
            shutil.move(source_path, file_path)  
            print(f"Image {i+1} saved as {file_path}")
            return file_path
        except Exception as e:
            print(f"Error: {e}")
    return None



__all__ = ["generate_images"]
