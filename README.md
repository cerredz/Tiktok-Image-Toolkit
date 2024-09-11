# Tiktok-Image-Toolkit
## Overview

Tiktok-Image-Toolkit serves as a tool that makes making TikTok slideshow videos more efficiently. What the script does is take the sentences in the sentences.txt file and generates images using the Flux Dev model, and then optionally emails the user the results. The script can also generate the images for general purposes and not just making tiktok videos. Additionally, there is a config file where the user can customize options such as the model that generates the images, size of the images, whether or not the script should email them the images, output directory, and more. 

## Setup
* for more in depth setup / customizable options make sure to look at the documentation.txt file *
  
1) Fork the repository
2) In the config.json file, fill out the following:
       - "hf_token" : your own hugging face token, if you do not have a token you can create on here: https://huggingface.co/settings/tokens
       - "email" : the email account of your google account that you will be sending the images to
       - "password" : the app password of the google account corresponding to the email. Regular passwords are not valid, to figure out how to generate an app password for your google account click here -> https://www.youtube.com/watch?v=pmG-OFPzvtg
3) Change the image dimension, output directory, model name, inference steps, whether or not to send images via email, and strength in the config.json file is necessary
4) Type your sentences in the "sentences.txt" file, one sentence per line
5) Type the following command in the root of your folder:

'''
python main.py
'''

