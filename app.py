import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import os
import datetime
client=InferenceClient(token=os.genev(HF_TOKEN)
MODEL="stabilityai/stable-diffusion-xl-base-1.0"
st.set_page_config(page_title="My Image Generator")
st.write("Describe your image")
prompt = st.text_input("Enter image prompt")
if st.button("generate"):
    with st.spinner("Image is genrating.."):
        image=client.text_to_image(prompt,model=MODEL)
        image.save("myimage.png")
        st.success("image is saved")
