import streamlit as st

def recommendations_page():
    st.title("Your Recommendations")
    st.write("This is the page where you can manage your recommendations.")

    if st.button("Home Page"):
        st.session_state["page"] = "home"
        st.rerun()
        
    if st.button("Logout👋🏻"):
        st.session_state["page"] = "login"
        st.rerun()