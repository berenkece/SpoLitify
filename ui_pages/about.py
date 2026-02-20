import streamlit as st

def about_page():
    st.title("About Us")
    st.write("This is the page I am coding for the Spotify API and some features.")

    if st.button("Home Page"):
        st.session_state["page"] = "home"
        st.rerun()
        
    if st.button("Logout👋🏻"):
        st.session_state["page"] = "login"
        st.rerun()