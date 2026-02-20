import streamlit as st

def search_page():
    st.title("Search")
    st.write("This is the page where you can search for music.")

    if st.button("Home Page"):
        st.session_state["page"] = "home"
        st.rerun()
        
    if st.button("Logout👋🏻"):
        st.session_state["page"] = "login"
        st.rerun()