from google import genai
import os
from dotenv import load_dotenv
import streamlit as st
user_input = st.text_input("Ask me anything")
pressd = st.button("Submit")

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents=user_input
)

out_put=response.text
if pressd:
    st.write(out_put)