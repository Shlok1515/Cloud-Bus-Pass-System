import streamlit as st
import requests
import pandas as pd

API_URL = "https://cloud-bus-pass-system-34vc.onrender.com"

st.set_page_config(
    page_title="Book Ticket",
    page_icon="🎫",
    layout="wide"
)

st.title("🎫 Book Bus Ticket")

# Check Login
if "user_id" not in st.session_state:
    st.warning("Please login first")
    st.stop()

try:

    buses_response = requests.get(
        f"{API_URL}/buses/",
        timeout=30
    )

    if buses_response.status_code != 200:
        st.error("Unable to fetch buses")
        st.stop()

    buses = buses_response.json()

    if not buses:
        st.warning("No buses available")
        st.stop()

    df = pd.DataFrame(buses)

    bus_options = {
        f"{row['bus_name']} ({row['source']} ➜ {row['destination']})":
        row["bus_id"]
        for _, row in df.iterrows()
    }

    selected_bus = st.selectbox(
        "Select Bus",
        list(bus_options.keys())
    )

    seats = st.number_input(
        "Number of Seats",
        min_value=1,
        max_value=10,
        value=1
    )

    if st.button(
        "Book Ticket",
        use_container_width=True
    ):

        bus_id = bus_options[selected_bus]

        booking_response = requests.post(
            f"{API_URL}/bookings/book",
            json={
                "user_id": st.session_state["user_id"],
                "bus_id": bus_id,
                "seats_booked": seats
            },
            timeout=30
        )

        if booking_response.status_code == 200:

            data = booking_response.json()

            st.success("🎉 Ticket Booked Successfully")

            st.json(data)

            st.session_state["booking_id"] = data.get(
                "booking_id"
            )

        else:
            st.error(
                f"Booking Failed: {booking_response.text}"
            )

except Exception as e:
    st.error(str(e))