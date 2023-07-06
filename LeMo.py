import streamlit as st

import streamlit.components.v1 as components
# Set the page title and icon
st.set_page_config(page_title="Lemo - Your AI Paralegal ", page_icon=":judge:",layout="wide", initial_sidebar_state="collapsed")
st.write("# Welcome to Lemo! 👋")
st.write("## Your AI Paralegal")
st.write("##### **👈 Select a Lemo Tool from the Left** to see some examples of what Lemo can do!")
st.sidebar.success("Select from the following LeMo tools")

st.markdown("""
    # Lemo is an *`Open Source`* project  \n 
    ## Made with :heart: by LVCOI \n
    ___
    Lemo endeavors to assist you, the "client", with your legal research and form data.  navigate to the [Welcome](./Pages/1_Welcome) page where LeMo will Begin your onboarding procedure.\n
    It will generate a To Do list for you and your attorney based on your topic of interest. Lemo will also help you to upload your documents and store them in a secure location. Lemo is powered by OpenAI's GPT Family of lls. Also this project and many more like this would not be possible without the [LangChain]() To get started, please enter your OpenAI API Keyand your topic of interest below. If you do not have an OpenAI API Key, pleasevisit https://beta.openai.com/ to request access to the API. If you have any questions, please contact us at info@lvcoi.com.
    ___
    -   Visit us at   [LVCOI.com](https://lvcoi.com) \n
    -   Or shoot us a note at [info@lvcoi.com](mailto:info@lvcoi.com) \n 
    -   If the spirit so moves you or you find this useful \n
        - [PayPal Fundraiser](https://www.paypal.com/pools/c/8VwOmMkHhF) \n
        - [Bitcoin]() \n
        - [Ethereum]() \n
""", unsafe_allow_html=True)
components.iframe('https://ko-fi.com/lvcoi/')