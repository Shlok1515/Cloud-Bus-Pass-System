import streamlit as st

st.set_page_config(
    page_title="Cloud Bus Pass System",
    page_icon="🚌",
    layout="wide"
)

st.title("🚌 Cloud Bus Pass System")

if "token" in st.session_state:
    st.success("✅ Logged In")
else:
    st.warning("⚠️ Not Logged In")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Users", "100+")

with col2:
    st.metric("Routes", "25+")

with col3:
    st.metric("Bookings", "500+")
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3448/3448339.png",
        width=120
    )

    st.title("Cloud Bus Pass")

    st.markdown("---")

    st.write("🎫 Smart Ticketing")
    st.write("☁️ Cloud Enabled")
    st.write("🔐 Secure Authentication")
st.divider()

st.markdown("""
### System Features

- User Registration
- Secure Login
- Search Buses
- Ticket Booking
- Seat Availability
- Booking History
- QR Ticket Generation
""")