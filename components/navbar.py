import streamlit as st

def navbarShow():
    out1, out2, out3 = st.columns([1, 6, 1])

    with out2:

        # create four equal columns and place one button in each so they appear side-by-side
        column1, column2, column3, column4 = st.columns(4)

        with column1:
            if st.button("🏠 Home", key="home"):
                st.session_state["page"] = "home"
                st.rerun()

        with column2:
            if st.button("⚙️ Settings", key="settings"):
                st.session_state["page"] = "settings"
                st.rerun()

        with column3:
            if st.button("ℹ️ About", key="about"):
                st.session_state["page"] = "about"
                st.rerun()

        with column4:
            if st.button("👤 Profile", key="profile"):
                st.session_state["page"] = "profile"
                st.rerun()

        st.divider()

    
        
