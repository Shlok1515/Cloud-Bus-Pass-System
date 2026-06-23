import streamlit as st
import requests

API_URL = "https://cloud-bus-pass-system-34vc.onrender.com"

st.set_page_config(
    page_title="My Bookings",
    page_icon="📋",
    layout="wide"
)

st.title("📋 My Bookings")

if "user_id" not in st.session_state:
    st.warning("Please login first")
    st.stop()

try:

    response = requests.get(
        f"{API_URL}/bookings/user/{st.session_state['user_id']}",
        timeout=30
    )

    if response.status_code != 200:
        st.error("Unable to fetch bookings")
        st.stop()

    bookings = response.json()

    if not bookings:
        st.info("No bookings found")
        st.stop()

    for booking in bookings:

        with st.container():

            st.markdown("---")

            col1, col2, col3 = st.columns([3, 3, 2])

            with col1:
                st.subheader(
                    f"🚌 {booking['bus_name']}"
                )

            with col2:
                st.write(
                    f"📍 {booking['source']} ➜ {booking['destination']}"
                )

            with col3:
                st.metric(
                    "Seats",
                    booking["seats_booked"]
                )

            st.write(
                f"🎫 Booking ID: {booking['booking_id']}"
            )

            st.write(
                f"💰 Fare: ₹{booking['fare']}"
            )

except Exception as e:
    st.error(str(e))