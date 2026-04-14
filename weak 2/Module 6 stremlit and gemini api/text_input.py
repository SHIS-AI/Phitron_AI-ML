import streamlit as st

st.title("Welcome to Streamlit",anchor=False)
st.header("this is header 1",divider=True)
st.subheader("this line is sub header.")
st.text("this line is normal text.")
## markdown
st.markdown("**SHIS** *SHIS* SHIS")
## color
st.markdown(":red[SHIS]")
## back-ground color
st.markdown(":red-background[SHIS]")
st.divider()

name=st.text_input("Enter your name.")
age = st.number_input("Enter your age.",value=None,placeholder="Type your age")
pressd=st.button("Enter to Confirm")

if pressd:
    st.write(f"Your name {name} and Your age {age}")