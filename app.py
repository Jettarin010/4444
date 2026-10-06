import streamlit as st

name = st.text_input("Your name")
if name:
    st.write(f"Hello, {name}!")