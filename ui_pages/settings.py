import streamlit as st

def settings_page():
    st.title("Your Settings")
    st.write("This is the page where you can manage your settings.")

    if st.button("Home Page"):
        st.session_state["page"] = "home"
        st.rerun()

    if st.button("Logout👋🏻"):
        st.session_state["page"] = "login"
        st.rerun()