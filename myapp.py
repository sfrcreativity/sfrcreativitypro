import streamlit as st


st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")
#st.markdown("Welcome to the professional dashboard.")

# find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
#st.set_page_config(page_title="Home", page_icon=":tada:", layout="wide")


home_page = st.Page(page="views/home.py", title="Home", icon="🏠", default=True)
about_page = st.Page(page="views/about_me.py", title="About Me", icon="🏠")
contact_page = st.Page(page="views/contact_me.py", title="Contact", icon="🏠")
app1 = st.Page(page="views/app1.py", title="App 1", icon="🏠")
app2 = st.Page(page="views/app2.py", title="App 2", icon="🏠")


pg = st.navigation(
    {"":[home_page],
    "About Me":[about_page,contact_page],
    "Projects":[app1,app2]}
    )

pg.run()



#with st.sidebar:
    # Sidebar
#    st.sidebar.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
#    st.sidebar.title("Navigation")
#    st.sidebar.markdown("Use the sidebar to navigate.") 

