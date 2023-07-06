import streamlit as st
import time
from functions.welcome import (identify_law_type, welcome_message)
from functions.dictionaries import law_keywords

# Set the page title and icon
st.title("Welcome to Onboarding 🙌")
user = st.empty()
placeholder = "Talk about what your case is regarding"
ph = placeholder

col1, col2 = st.columns(2)
# create a container for the welcome message
with col1:
    # Print our the welcome message
    st.markdown(welcome_message)

with col2:
    # Create a text input for the user to enter their name
    user_input = st.text_area("Please describe your legal issue in a few sentences.")
    

onboard, lawtype = identify_law_type(user_input, law_keywords)

if user_input:
    st.write("Fiding Area of Law from :", user_input)
    progress_text = st.empty()
    my_bar = st.progress(0, text="Identifying")
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
with st.expander("Onboarding"):
    st.info(onboard) # type: ignore