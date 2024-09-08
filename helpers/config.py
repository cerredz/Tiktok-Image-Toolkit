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
    
    return config

__all__ = ["load_config"]
