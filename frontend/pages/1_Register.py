import streamlit as st
import requests

API_URL = "https://cloud-bus-pass-system-34vc.onrender.com"

st.set_page_config(page_title="Register", page_icon="🚌")

st.title("📝 User Registration")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):

    if not name or not email or not password:
        st.warning("Please fill all fields")
    else:
        try:
            response = requests.post(
                f"{API_URL}/users/register",
                json={
                    "name": name,
                    "email": email,
                    "password": password
                },
                timeout=30
            )

            if response.status_code in [200, 201]:
                st.success("✅ Registration Successful")
                st.json(response.json())

            else:
                st.error(f"❌ Error: {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Unable to connect to backend: {e}")