import streamlit as st
import pages as pg
from streamlit_navigation_bar import st_navbar

page = st_navbar(["Home", "Join Waiting List", "About Us", "Contact Us"])
st.write(page)
st.title("Summary of your CCTV Footage by AI")
st.text("""Chat with your Security Camera!""")
st.caption("""Quickest way to review your security. Save hours of CCTV footage monitoring time using our AI solution.""")
