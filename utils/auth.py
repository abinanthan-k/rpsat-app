import streamlit as st

USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "abinan": {"password": "user123", "role": "user"}
}

def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        user = USERS.get(username)
        if user and user["password"] == password:
            st.session_state["user"] = username
            st.session_state["role"] = user["role"]
            return True
        st.error("Invalid credentials")
    return False
