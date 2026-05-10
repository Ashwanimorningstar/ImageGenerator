import streamlit as st
from huggingface_hub import InferenceClient
import os

# Hugging Face client
client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

# Model
MODEL = "black-forest-labs/FLUX.1-schnell"

# Page config
st.set_page_config(page_title="My Image Generator")

st.title("AI Image Generator")

st.write("Describe your image")

# Input
prompt = st.text_input("Enter image prompt")

# Button
if st.button("Generate"):

    with st.spinner("Image is generating..."):

        # Generate image
        image = client.text_to_image(
            prompt=prompt,
            model=MODEL
        )

        # Save image
        image.save("myimage.png")

        # Display image
        st.image(image)

        st.success("Image generated successfully!")

        # Download button
        with open("myimage.png", "rb") as file:

            st.download_button(
                label="Download Image",
                data=file,
                file_name="myimage.png",
                mime="image/png"
            )
