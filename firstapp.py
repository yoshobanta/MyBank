import streamlit as st

st.title("🚀 My First Streamlit App")
st.write("Hello! If you see this, Streamlit is working 🎉")

name = st.text_input("Enter your name")
if st.button("Greet"):
    st.success(f"Hi {name}, welcome to Streamlit!")
