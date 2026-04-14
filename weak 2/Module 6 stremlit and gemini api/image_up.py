import streamlit as st

st.title("WellCome to my World")
st.divider()
st.header("image uplode.")
st.selectbox("Choose your profisonal",
             ("Student","Employe","Businessman"),
             index=None,accept_new_options=True)
image_file = st.file_uploader("Enter your image",
                            type=['jpg','jpeg','png'],
                            accept_multiple_files=True)

press = st.button("Enter to confirm")
if press:
    if image_file:
        col = st.columns(len(image_file))
        for i, per_image in enumerate(image_file):
            with col[i]:
                st.image(per_image)

st.divider()

st.image("/home/shis/Downloads/1767576853642-removebg-preview.png")
