import streamlit as st
import requests

API_URL = "https://cloud-bus-pass-system-34vc.onrender.com"

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

    if not email or not password:
        st.warning("Please enter email and password")

    else:
        try:

            response = requests.post(
                f"{API_URL}/users/login",
                json={
                    "email": email,
                    "password": password
                },
                timeout=30
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state["token"] = data["access_token"]
                st.session_state["user_id"] = data["user_id"]

                st.success("✅ Login Successful")

            else:
                st.error("❌ Invalid Credentials")

        except requests.exceptions.RequestException as e:
            st.error(f"Unable to connect to backend: {e}")