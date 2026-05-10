import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import os
import datetime
client=InferenceClient(token=os.getenv("HF_TOKEN"))
MODEL = "black-forest-labs/FLUX.1-schnell"
st.set_page_config(page_title="My Image Generator")
st.write("Describe your image")
prompt = st.text_input("Enter image prompt")
if st.button("generate"):
image.save("myimage.png")
st.image(image)
with open("myimage.png", "rb") as file:

    st.download_button(
        label="Download Image",
        data=file,
        file_name="myimage.png",
        mime="image/png"
    )
    with st.spinner("Image is genrating.."):
        image=client.text_to_image(prompt,model=MODEL)
        st.success("image is genereted")
