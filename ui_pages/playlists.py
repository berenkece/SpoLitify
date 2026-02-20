import streamlit as st

def playlists_page():
    st.title("Your Playlists")
    st.write("This is the page where you can manage your playlists.")

    if st.button("Home Page"):
        st.session_state["page"] = "home"
        st.rerun()
        
    if st.button("Logout👋🏻"):
        st.session_state["page"] = "login"
        st.rerun()