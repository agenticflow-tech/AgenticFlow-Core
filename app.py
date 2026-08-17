import streamlit as st
import urllib.request
import json

# Page Configuration
st.set_page_config(page_title="AgenticFlow Telemetry", page_icon="📡", layout="centered")

# Visual Header
st.title("📡 AgenticFlow Network Engine")
st.caption("Real-time automated data extraction & telemetry dashboard")

st.divider()

# Interactive Web Button & Extraction Logic
if st.button("⚡ Extract Live Network Data", type="primary"):
    with st.spinner("Connecting to live server..."):
        try:
            url = "http://ip-api.com/json/"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())

            st.success("✅ Network Telemetry Synchronized!")
            
            # Interactive metric cards
            col1, col2, col3 = st.columns(3)
            col1.metric("ISP Network", data.get('isp', 'N/A'))
            col2.metric("Region", f"{data.get('city', 'N/A')}, {data.get('regionName', 'N/A')}")
            col3.metric("Country", data.get('country', 'N/A'))
            
            # Expandable payload view
            with st.expander("🔍 View Raw JSON Payload"):
                st.json(data)
                
        except Exception as e:
            st.error(f"Extraction Error: {e}")
else:
    st.info("Click the button above to run the live extraction pipeline.")