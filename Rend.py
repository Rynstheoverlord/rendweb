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

        with st.popover("Tools"):
            flip_x = st.checkbox("Flip X")
            flip_y = st.checkbox("Flip Y")
            st.divider()
            enhance = st.checkbox("Enhance")

            if flip_x:
                image = ImageOps.mirror(image)
            if flip_y:
                image = ImageOps.flip(image)

            if enhance:
                image = image.filter(ImageFilter.EDGE_ENHANCE())

        st.image(image, use_column_width=True)

        with st.popover("Download image"):
            image_name = st.text_input("Enter image name", value="image")
            image_format = st.selectbox("Image format", ['png', 'jpg', 'webp', 'tiff', "gif", 'jfif'])
            bio = BytesIO()
            image.save(bio, 'PNG')
            if st.download_button("Download image", bio, f"{image_name}.{image_format}", type="primary",
                                  use_container_width=True):
                st.toast("Image saved successfully!")
