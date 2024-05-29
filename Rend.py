import streamlit as st
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

image = st.file_uploader("Upload Image")

if image is not None:
    image = Image.open(image)
    with st.expander("Image"):
        blur = st.slider("Blur", min_value=0, max_value=20)
        contrast = st.slider("Contrast", min_value=0, max_value=20)

        image = image.filter(ImageFilter.GaussianBlur(blur))
        image = image.filter(ImageFilter.UnsharpMask(contrast))

        st.image(image, use_column_width=True)

        flip_x = st.checkbox("Flip X")
        flip_y = st.checkbox("Flip Y")

        if flip_x:
            image = ImageOps.mirror(image)
        if flip_y:
            image = ImageOps.flip(image)

        with st.popover("Download image"):
            image_format = st.selectbox("Image format", ['png', 'jpg', 'webp', 'tiff', "gif", 'jfif'])
            bio = BytesIO()
            image.save(bio, 'PNG')
            st.download_button("Download image", bio, f"image.{image_format}", type="primary", use_container_width=True)
