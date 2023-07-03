import streamlit as st
from functions.welcome import cbm_loop, cem_loop, welcome_message, identify_law_type, law_keywords, ENTITY_MEMORY_CONVERSATION_TEMPLATE, ConversationChain, ConversationBufferMemory, ConversationEntityMemory, SystemMessage
from functions.fake_type import fake_type

# Set the page title and icon
st.set_page_config(page_title="Welcome to Lemo AI", page_icon=":man_office_worker:", layout="wide", initial_sidebar_state="collapsed",)

st.title("Welcome to Onboarding 🙌")
st.sidebar.success("Select from the following LeMo tools")

# create a container for the welcome message
with st.chat_message("LeMo", "👨🏽‍💼"): # type: ignore
    st.markdown(fake_type(welcome_message))

# create a container for the user input
@st.cache(allow_output_mutation=True)
def get_userdata():
  st.text_input("What is your name?" , key="client")


