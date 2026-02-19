import streamlit as st
from components.navbar import navbarShow

def home_page():
    navbarShow()
    st.title("Welcome to the Home Page of Spolitfy!")
    st.write("This is the home page where you can find your favorite music.")

    if st.button("🎧 Playlists", key="playlists"):
        st.session_state["page"] = "playlists"
        st.rerun()
    if st.button("🔎 Search", key="search"):
        st.session_state["page"] = "search"
        st.rerun()
    if st.button("🔮 Recommendations", key="recommendations"):
        st.session_state["page"] = "recommendations"
        st.rerun()
    if st.button("💬 Chatroom", key="chatroom"):
        st.session_state["page"] = "chatroom"
        st.rerun()


    