import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Search Buses",
    page_icon="🚌",
    layout="wide"
)

st.title("🚌 Search Buses")
st.markdown("Find available buses and fares for your journey")

API_URL = "https://cloud-bus-pass-system-34vc.onrender.com"

try:
    response = requests.get(
        f"{API_URL}/buses/",
        timeout=30
    )

    if response.status_code != 200:
        st.error("Unable to fetch buses")
        st.stop()

    buses = response.json()

    if not buses:
        st.warning("No buses available")
        st.stop()

    df = pd.DataFrame(buses)

    source_options = ["Select Source"] + sorted(
        df["source"].dropna().unique().tolist()
    )

    destination_options = ["Select Destination"] + sorted(
        df["destination"].dropna().unique().tolist()
    )

    col1, col2, col3 = st.columns([4, 4, 2])

    with col1:
        source = st.selectbox(
            "Source",
            source_options
        )

    with col2:
        destination = st.selectbox(
            "Destination",
            destination_options
        )

    with col3:
        st.write("")
        st.write("")
        search_btn = st.button(
            "🔍 Search",
            use_container_width=True
        )

    if search_btn:

        if source == "Select Source" or destination == "Select Destination":
            st.warning("Please select source and destination")

        else:

            filtered = df[
                (df["source"] == source)
                &
                (df["destination"] == destination)
            ]

            st.divider()

            if filtered.empty:
                st.error("No buses found for this route")

            else:

                st.success(
                    f"{len(filtered)} bus(es) found"
                )

                for _, bus in filtered.iterrows():

                    with st.container():

                        st.markdown("---")

                        c1, c2, c3, c4 = st.columns(
                            [3, 3, 2, 2]
                        )

                        with c1:
                            st.subheader(
                                f"🚌 {bus['bus_name']}"
                            )

                        with c2:
                            st.write(
                                f"📍 {bus['source']} ➜ {bus['destination']}"
                            )

                        with c3:
                            st.metric(
                                "Seats",
                                bus["total_seats"]
                            )

                        with c4:
                            st.metric(
                                "Fare",
                                f"₹{bus['fare']}"
                            )

except Exception as e:
    st.error(f"Error: {e}")