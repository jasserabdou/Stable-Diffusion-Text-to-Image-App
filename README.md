# Stable Diffusion Text-to-Image App 🚀

This is a Streamlit app that harnesses the power of the `StableDiffusionPipeline` from the `diffusers` library to generate stunning images from text prompts. The app efficiently utilizes the `Accelerator` class from the `accelerate` library to run the model on the available device, whether it's a CPU or a GPU.

## Installation

1. Clone the repository by running:
   ```
   git clone https://github.com/jasserabdou/Stable-Diffusion-Text-to-Image-App.git
   ```
   

2. Install the required libraries by running:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure that you have Python installed on your system.

2. Open your terminal or command prompt and navigate to the project directory.

3. Run the app by executing the following command:
   ```
   streamlit run app.py
   ```
   Replace `app.py` with the name of the Python file containing the provided code.

4. Wait for the app to start, and a new browser window will automatically open with the app's interface.

5. Input your text prompt in the text area provided on the web page.

6. Click on the "Generate Image" button to create an image based on your input text.

7. The generated image will be displayed on the same page along with a caption.

8. The image will also be saved in a folder named "images" within the same directory where the script is running.

9. The saved image file will be named "Saved_img.png."

## Notes

- The app uses a pre-trained model from the `CompVis/stable-diffusion-v1-4` repository to generate images from text.

- The model loading process is optimized using the `@st.cache_resource` decorator to avoid re-loading the model every time an image is generated, which speeds up the process.

- If any errors occur during image generation or saving, the app will display appropriate error messages and stack traces to help diagnose the issue.

- Feel free to experiment with various text prompts and observe the fascinating variations in the generated images.

- If you encounter any problems or have suggestions for improvements, don't hesitate to report them in the project's repository.

- This app is also deployed on the Streamlit community cloud, and you can access it at this server: https://stable-diffusion-text-to-image-app-tqxr4b9r9y7yidb4838qss.streamlit.app/.

## Test Prompts
1. "A peaceful river flows through a lush forest, reflecting the vibrant colors of nature."
2. "A lone astronaut explores a mysterious alien planet, surrounded by breathtaking landscapes."
3. "A majestic castle stands tall amidst rolling hills, basking in the glow of the setting sun."
4. "An adorable puppy plays in a field of wildflowers, bringing joy to everyone around."
5. "A magical portal opens, revealing a fantastical world filled with mythical creatures."
6. "A group of friends gathers around a campfire, sharing stories under a starry sky."
7. "A serene beach at sunset, where waves gently touch the shore, creating a peaceful melody."
8. "A futuristic cityscape, with flying cars and neon lights illuminating the night sky."
9. "A cozy library filled with ancient books, where knowledge and adventure await."
10. "An enchanted forest with glowing mushrooms, where fairies dance in the moonlight."

Enjoy experimenting with the Stable Diffusion Text-to-Image App and generating intriguing images from text prompts! 🌟
