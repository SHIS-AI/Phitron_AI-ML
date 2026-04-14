import streamlit as st

name = st.text_input("Enter your name.")
age = st.number_input("Enter your age.",value=None,placeholder="Enter your age")
box = st.selectbox("select your profession",["Student","Teacher","Freelancer"],index=None)

pressd = st.button("Enter to Confirm.")

if pressd:
    if name and age and box:
        st.success(f"Your name {name}, Your age {age}, and Your profession {box}.")
    else:
        st.warning("Please fill all the fields.")