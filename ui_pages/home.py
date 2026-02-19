import streamlit as st

def home_page():
    st.title("Welcome to the Home Page of Spolitfy!")
    st.write("This is the home page where you can find your favorite music.")

    if st.button("Logout👋🏻"):
        st.session_state["page"] = "login"
        st.rerun()