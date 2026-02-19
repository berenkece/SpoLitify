import streamlit as st
from ui_pages import login
from ui_pages import home
from ui_pages import playlists
from ui_pages import recommendations
from ui_pages import search

if "page" not in st.session_state:
    st.session_state["page"] = "login"

if st.session_state["page"] == "login":
    login.login_page()
elif st.session_state["page"] == "home":
    home.home_page()
elif st.session_state["page"] == "playlists":
    playlists.playlists_page()
elif st.session_state["page"] == "recommendations":
    recommendations.recommendations_page()
elif st.session_state["page"] == "search":
    search.search_page()
else:
    st.error("Something went wrong")