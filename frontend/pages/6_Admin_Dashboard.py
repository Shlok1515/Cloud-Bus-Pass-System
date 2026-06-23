import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Admin Dashboard")
st.markdown("Monitor users, bookings, revenue, and bus performance")

try:

    # Analytics Summary
    summary = requests.get(
        "http://localhost:8000/analytics/summary"
    ).json()

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Users",
            summary["total_users"]
        )

    with col2:
        st.metric(
            "🚌 Buses",
            summary["total_buses"]
        )

    with col3:
        st.metric(
            "🎫 Bookings",
            summary["total_bookings"]
        )

    with col4:
        st.metric(
            "💰 Revenue",
            f"₹{summary['total_revenue']}"
        )

    st.divider()

    # Bus Data
    buses_response = requests.get(
        "http://localhost:8000/buses/"
    )

    buses = buses_response.json()

    if buses:

        buses_df = pd.DataFrame(buses)

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("💰 Fare Analysis")

            fare_chart = px.bar(
                buses_df,
                x="bus_name",
                y="fare",
                title="Fare By Bus"
            )

            st.plotly_chart(
                fare_chart,
                use_container_width=True
            )

        with col2:

            st.subheader("🛣 Route Distribution")

            route_df = (
                buses_df
                .groupby(
                    ["source", "destination"]
                )
                .size()
                .reset_index(name="count")
            )

            route_chart = px.pie(
                route_df,
                values="count",
                names="destination",
                title="Routes"
            )

            st.plotly_chart(
                route_chart,
                use_container_width=True
            )

    st.divider()

    # Popular Buses
    try:

        booking_stats = requests.get(
            "http://localhost:8000/analytics/bookings-per-bus"
        ).json()

        if booking_stats:

            booking_df = pd.DataFrame(
                booking_stats
            )

            st.subheader(
                "🔥 Most Popular Buses"
            )

            popular_chart = px.bar(
                booking_df,
                x="bus_name",
                y="total_bookings",
                title="Bookings Per Bus"
            )

            st.plotly_chart(
                popular_chart,
                use_container_width=True
            )

    except:
        st.info(
            "Bookings analytics API not added yet"
        )

except Exception as e:
    st.error(
        f"Dashboard Error: {e}"
    )