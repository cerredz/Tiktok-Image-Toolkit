import json
import os
from dotenv import load_dotenv
load_dotenv()

# Loads the options from the config.json file and returns its contents
def load_config():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    
    # Check if hf_token exists in config and is not empty
    if "hf_token" not in config or config["hf_token"] == "":
        # If not, load the HF_TOKEN from the environment variable
        config["hf_token"] = os.getenv("HF_TOKEN")
    
    # check if the email's password is in the config
    if "password" not in config or config["password"] == "":
        # If not, load the password from the environment variable
        config["password"] = os.getenv("EMAIL_PASSWORD")
    
    return config

# checks if the config is valid
def validate_config(config):
    model = config["model"]
    hf_token = config["hf_token"]
    num_inference_steps = config["num_inference_steps"]
    width = config["image"]["width"]
    height = config["image"]["height"]
    output_directory = config["output_directory"]

    # check if the required parameters are in the config
    if not model or not hf_token or not num_inference_steps or not width or not height or not output_directory:
        raise ValueError("Missing required parameters in config.json")
        return False
    
    # check if the width and height are valid
    if width < 256 or width > 2048:
        raise ValueError("Invalid Width: Must be between 256 and 2048")
        return False
    
    if height < 256 or height > 2048:
        raise ValueError("Invalid Height: Must be between 256 and 2048")
        return False
    
    # check if the num_inference_steps is valid
    if num_inference_steps < 1 or num_inference_steps > 28:
        raise ValueError("Invalid Number of Inference Steps: Must be between 1 and 28")
        return False
    
    return True

__all__ = ["load_config", "validate_config"]
