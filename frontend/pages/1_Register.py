import streamlit as st
import requests

st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Create Account")

st.markdown(
    "Register to access the Cloud Bus Pass System"
)

with st.container():

    name = st.text_input(
        "Full Name",
        placeholder="Enter your name"
    )

    email = st.text_input(
        "Email Address",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Register"):

        if not name or not email or not password:
            st.error("Please fill all fields")

        elif password != confirm_password:
            st.error("Passwords do not match")

        else:

            response = requests.post(
                "http://127.0.0.1:8000/users/register",
                json={
                    "name": name,
                    "email": email,
                    "password": password
                }
            )

            if response.status_code == 200:
                st.success(
                    "Registration successful!"
                )
                st.json(response.json())

            else:
                st.error(
                    "Registration failed"
                )