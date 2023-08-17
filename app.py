import streamlit as st
from io import BytesIO
import torch
from accelerate import Accelerator
from diffusers import StableDiffusionPipeline

MODEL_ID = "CompVis/stable-diffusion-v1-4"
ACCELERATOR = Accelerator()
buf = BytesIO()


@st.cache_resource
def load_model():
    with ACCELERATOR.device:
        pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID, torch_dtype=torch.float32
        )
        pipe = pipe.to(ACCELERATOR.device)
    return pipe


def main():
    st.title("Stable Diffusion Text-to-Image App 🚀")
    st.markdown(
        "This app uses the [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4) model from [Hugging Face](https://huggingface.co/) to generate realistic images from text prompts."
    )

    prompt = st.text_area("Input Text:", height=50, max_chars=100)
    generate_button = st.button("Generate Image")

    if generate_button:
        if not prompt.strip():
            st.warning("Please enter a valid text prompt.")
        else:
            with st.spinner("Generating Image..."):
                pipe = load_model()

                try:
                    with torch.no_grad(), ACCELERATOR.device:
                        image = pipe(prompt).images[0]
                        st.success("Image generated successfully!")
                        st.image(
                            image, caption="Generated Image", use_column_width=True
                        )

                        image.save(buf, format="PNG")
                        byte_im = buf.getvalue()
                        download_button = st.download_button(
                            "Download Image",
                            byte_im,
                            file_name="generated_image.png",
                            mime="image/png",
                        )

                except Exception as e:
                    st.error("Image generation failed. Please try again later.")
                    st.exception(e)


if __name__ == "__main__":
    main()
