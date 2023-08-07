# Stable Diffusion Text-to-Image App 🚀

This is a Streamlit app that utilizes the power of the `StableDiffusionPipeline` from the `diffusers` library to generate images from text prompts. The app leverages the `Accelerator` class from the `accelerate` library to run the model efficiently on the available device (CPU or GPU).

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

1. Make sure you have Python installed on your system.

2. Open your terminal or command prompt and navigate to the project directory.

3. Run the app by executing the following command:
   ```
   streamlit run app.py
   ```
   Replace `app.py` with the name of the Python file containing the provided code.

4. Wait for the app to start, and a new browser window will automatically open with the app's interface.

5. Input your text prompt in the text area provided on the web page.

6. Click on the "Generate Image" button to generate an image based on your input text.

7. The generated image will be displayed on the same page along with a caption.

8. The image will also be saved in a folder named "images" within the same directory where the script is running.

9. The saved image file will be named "Saved_img.png."

## Notes

- The app uses a pre-trained model from the `CompVis/stable-diffusion-v1-4` repository to generate images from text.

- The model loading process is optimized using the `@st.cache_resource` decorator to avoid re-loading the model every time an image is generated, which speeds up the process.

- If there are any errors during image generation or saving, the app will display appropriate error messages and stack traces to help diagnose the issue.

- Feel free to explore different text prompts and observe the variations in the generated images.

- If you encounter any problems or have suggestions for improvements, don't hesitate to report them in the project's repository.

- This app is also deployed on streamlit community cloud.

Enjoy experimenting with the Stable Diffusion Text-to-Image App and generating intriguing images from text prompts! 🌟
