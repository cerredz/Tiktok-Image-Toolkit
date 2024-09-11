# Tiktok-Image-Toolkit

## Overview
**Tiktok-Image-Toolkit** is a tool designed to streamline the process of creating TikTok slideshow videos by automating image generation. The script reads sentences from the `sentences.txt` file and generates corresponding images using the Flux Dev model. Additionally, it offers the option to email the generated images to the user. The tool can also be used to generate images for general purposes beyond TikTok video creation.

## Setup

> **Note**: For a more in-depth guide or information on customization options, refer to `documentation.txt`.

### Steps:
1. **Fork the Repository**  
   Clone or fork this repository to your local machine.
   
2. **Configure `config.json`**  
   Fill out the following fields in the `config.json` file:
   - `"hf_token"`: Your Hugging Face token. [Create one here](https://huggingface.co/settings/tokens) if you don’t have one.
   - `"email"`: The Google account email address you will use to send images.
   - `"password"`: The app password for your Google account. Regular passwords are not valid. [Learn how to generate an app password](https://www.youtube.com/watch?v=pmG-OFPzvtg).
   
3. **Adjust Other Settings (Optional)**  
   In the `config.json` file, you can also customize:
   - Image dimensions
   - Output directory
   - Model name
   - Inference steps
   - Strength of the image generation
   - Whether to send images via email

4. **Prepare Your Sentences**  
   Type your sentences in the `sentences.txt` file, with one sentence per line.

5. **Run the Script**  
   In the root directory of the project, run the following command:
   ```bash
   python main.py
