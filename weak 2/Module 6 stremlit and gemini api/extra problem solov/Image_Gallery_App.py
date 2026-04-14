import streamlit as st
image_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"],accept_multiple_files= True)

pressd = st.button("Confirm")

if pressd:
    image_len = len(image_file)
    if image_file:
        if image_len == 3:
            st.success("you upload 3 photo")
        if image_len > 3:
            st.warning("You can upload maximum 3 images.")
            st.image(image_file, width=200)
        else:
            st.image(image_file,width=200)