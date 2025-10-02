import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Home", page_icon="🏠")
st.title("🏠 Home")
st.markdown("Welcome to the professional dashboard.")


# find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Home", page_icon=":tada:", layout="wide")

# Load Lottie animation from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation from a local JSON file
def load_lottie_file(filepath: str):
    try:
        with open(str, "r", encoding="utf-8") as f:
            lottie_json = json.load(f)
            st_lottie(lottie_json, height=300, key="safe")
    except Exception as e:
        st.error(f"Failed to load animation: {e}")

# ---- Load Assets ----

#lottie_coding = load_lottieurl("Coding_boy.json")
lottie_coding = load_lottie_file("Coding_boy.json")



# ---- HEADER SECTION ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)   
    with left_column:
        st.header("Hi, I am John Doe :wave:")
        st.write("A Data Analyst From USA")
        st.write(
            """
            I am passionate about finding ways to use Python and SQL to be more efficient and effective in business settings.
            I am a quick learner and collaborate closely with clients to create effective, scalable solutions that solve 
            real-world business problems. Let's work together to bring your ideas to life!
            """
        )
        st.write("[Learn More >](https://www.linkedin.com/in/johndoe/)")
    with right_column:
        st_lottie(lottie_coding, height=250, key="local")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif")
    with text_column:
        st.subheader("Project Title")
        st.write(
            """
            Brief description of the project. This project involved using Python and SQL to analyze data and provide insights.
            """
        )
        st.markdown("[View Project >]")




