import streamlit as st

def login_page():
    st.title("Login to Spolitfy🎧")

    username = st.text_input("Username")
    password = st.text_input("Password", type = 'password')

    if st.button("Login"):
        if check_login(username, password):
            st.success("Login succesfull!")
            st.session_state["page"] = "home"
            st.rerun()
        else:
            st.error("Wrong username or password")


def check_login(username, password):
    if username == "admin" and password == "12345":
        
        return True

    