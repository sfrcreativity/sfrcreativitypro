import streamlit as st


# Set page config
st.set_page_config(
    page_title="Modern Streamlit App",
    layout="wide",  # Use "centered" for traditional layout
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Use the sidebar to navigate.")

# Page title
st.title("🚀 Modern Streamlit Layout")

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📁 Data", "⚙️ Settings"])

with tab1:
    st.header("📊 Dashboard")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Main Chart")
        st.line_chart({"Sales": [100, 200, 150, 300]})
    with col2:
        st.subheader("Stats")
        st.metric("Users", 1200, "+5%")
        st.metric("Revenue", "$15K", "+8%")

with tab2:
    st.header("📁 Data Explorer")
    st.dataframe({"Product": ["A", "B", "C"], "Sales": [100, 150, 200]})

with tab3:
    st.header("⚙️ Settings")
    theme = st.selectbox("Choose theme", ["Light", "Dark"])
    st.write("Theme selected:", theme)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")