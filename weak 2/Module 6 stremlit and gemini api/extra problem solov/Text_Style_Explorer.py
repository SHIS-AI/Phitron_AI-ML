import streamlit as st

user_input = st.text_input("Enter your text here")

if user_input:
    st.title(user_input)
    st.divider()
    st.header(user_input)
    st.divider()
    st.subheader(user_input)
    st.divider()
    st.text(user_input)