import streamlit as st

def chatroom_page():
    st.title("Chat Room")
    st.write("This is the page where you can chat with others.")

    if st.button("Home Page"):
        st.session_state["page"] = "home"
        st.rerun()
        
    if st.button("Logout👋🏻"):
        st.session_state["page"] = "login"
        st.rerun()