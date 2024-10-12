import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
st.title("Welcome to LanguaMate👋.")
st.sidebar.success("Select a page above.")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_factory = load_lottieurl("https://lottie.host/ab2897d1-772a-478a-bc28-2dc50c6276d3/UTuCWQQsO8.json")
st_lottie(lottie_factory, key="factory")

