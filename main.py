
from helpers.sentences import get_sentences
from helpers.config import load_config
from helpers.images import generate_images

def main():
    # Load the config file
    config = load_config()

    # Get the sentences for the images
    sentences = get_sentences()

    # Generate the images
    #images = generate_images(sentences, config)
    
    
    



if __name__ == "__main__":
    main()
