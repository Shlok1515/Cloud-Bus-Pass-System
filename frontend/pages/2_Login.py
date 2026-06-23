import streamlit as st
import requests

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Login")

email = st.text_input(
    "Email Address",
    placeholder="Enter your email"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    try:

        response = requests.post(
            "http://localhost:8000/users/login",
            json={
                "email": email,
                "password": password
            }
        )

        if response.status_code == 200:

            data = response.json()

            st.session_state["token"] = data["access_token"]
            st.session_state["user_id"] = data["user_id"]
            st.success("Login Successful")

            st.json(data)

        else:
            st.error("Invalid Credentials")

    except Exception as e:
        st.error(str(e))