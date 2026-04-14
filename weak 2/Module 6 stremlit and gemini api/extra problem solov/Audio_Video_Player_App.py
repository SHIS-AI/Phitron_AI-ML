import streamlit as st


audio_file = st.file_uploader("Uploader your audio file", type=["mp3","ohh"])

video_file = st.file_uploader("Uploader your video file", type=["mp4","mkv"])

pressed = st.button("Play Audio")

if pressed:
    if audio_file:
        st.audio(audio_file)
    if video_file:
        st.video(video_file)
else:
    st.error("Please uploade video")