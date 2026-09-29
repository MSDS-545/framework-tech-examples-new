"""Streamlit reruns this Python script from top to bottom after interactions."""
import streamlit as st

# Page configuration should be one of the first Streamlit calls.
st.set_page_config(page_title="Streamlit Basic Example", page_icon="👋")

# Streamlit commands create browser UI elements directly from Python.
st.title("Hello from Streamlit!")
st.write("This interface is defined with Python commands.")

# text_input creates a widget and returns its current value.
name = st.text_input("Enter your name")

# button returns True on the rerun triggered by a click.
if st.button("Greet me"):
    if name.strip():
        st.success(f"Welcome, {name}!")
    else:
        st.warning("Enter a name first.")
