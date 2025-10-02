import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Page title
st.title("🚀 About Me")
st.write("---")
st.set_page_config(page_title="About This App",layout="centered")
st.header("Welcome to the Multi-Page Streamlit App")
st.markdown("""
This is a multi-page Streamlit app.

**Features:**
- Simple UI
- Multiple Pages
- Interactive Widgets
""")

