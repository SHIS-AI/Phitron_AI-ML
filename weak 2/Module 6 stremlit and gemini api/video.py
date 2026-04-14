import streamlit as st

video_file = st.file_uploader("Enter your video",
                              type=['mp4','mkv'])
pressd = st.button("Enter to confirm")
if pressd:
    if video_file:

        st.video(video_file)
    else:
        st.error("You must upload a file")