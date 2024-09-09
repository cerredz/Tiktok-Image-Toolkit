
from helpers.sentences import get_sentences
from helpers.config import load_config
from helpers.images import generate_images
from helpers.email import send_email

def main():
    # Load the config file
    config = load_config()

    # Get the sentences for the images
    sentences = get_sentences()

    # Generate the images
    image_paths = generate_images(sentences, config)
    
    # send the images to the user if that option is enabled
    if config["send_images"] and image_paths:
        send_email(config["email"], config["password"], image_paths)



if __name__ == "__main__":
    main()
