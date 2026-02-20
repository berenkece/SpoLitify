import streamlit as st

def profile_page():
    st.title("Your Profile")
    st.write("This is the page where you can manage your profile.")

    if st.button("Home Page"):
        st.session_state["page"] = "home"
        st.rerun()
        
    if st.button("Logout👋🏻"):
        st.session_state["page"] = "login"
        st.rerun()