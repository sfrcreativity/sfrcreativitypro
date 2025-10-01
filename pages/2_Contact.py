import streamlit as st

st.set_page_config(page_title="Contact", layout="centered")
st.write("We'd love to hear from you! Fill out the form below:")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send"):
    st.success("Thank you! Your message has been sent.")