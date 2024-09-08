import json
import os

# Loads the options from the config.json file and returns its contents
def load_config():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    
    # Load the HF_TOKEN from the environment variable
    config["hf_token"] = os.getenv("HF_TOKEN")
    return config

__all__ = ["load_config"]
