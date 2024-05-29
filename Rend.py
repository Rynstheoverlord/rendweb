import streamlit as st
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

image = st.file_uploader("Upload Image")

if image is not None:
    image = Image.open(image)
    with st.expander("Image"):
        blur = st.slider("Blur", min_value=0, max_value=20)

        image = image.filter(ImageFilter.GaussianBlur(blur))
        st.image(image, use_column_width=True)

        flip_x = st.checkbox("Flip X")
        flip_y = st.checkbox("Flip Y")

        if flip_x:
            image = ImageOps.mirror(image)
        if flip_y:
            image = ImageOps.flip(image)

        with st.popover("Download image"):
            bio = BytesIO()
            image.save(bio, 'PNG')
            st.download_button("Download image", bio, "image.png")
