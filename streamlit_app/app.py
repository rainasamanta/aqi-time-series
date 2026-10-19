import streamlit as st

st.set_page_config(
    page_title="AQI Health Exposure Tracker",
    page_icon="🌫️",
    layout="wide"
)

st.title("AQI Health Exposure Tracker")
st.markdown("### How often people in four Indian cities breathe unhealthy air, and how predictable it is")

st.divider()

st.markdown("""
This app analyses daily air quality data across four Indian cities -
**Bengaluru, Delhi, Kolkata, and Mumbai** - from January 2019 to March 2025
(9,116 daily records).
""")

st.divider()

st.markdown("""
| Page | What it answers |
|---|---|
| City Overview | What does AQI look like in my city over time? |
| City Comparison | Which city has a worse health burden? |
| Seasonal Patterns | Which months are safest and most dangerous? |
| Diwali Impact | Is air quality worse during Diwali than in the weeks around it? |
| SARIMA Forecast | Can a SARIMA model forecast AQI better than simple seasonal guesses? |
""")

st.divider()

st.subheader("Key findings")
st.markdown("""
- **Delhi** had Poor-or-worse air (AQI above 200) on **46.6%** of days; **Bengaluru** on none.
- Every city is worst in **winter** and cleanest during the **monsoon**.
- **Diwali:** no city showed a consistent rise once the festival was compared with the weeks
  before and after (higher in only 3–4 of 6 years).
- **Forecasting:** simple seasonal baselines beat SARIMA in **3 of 4 cities**. AQI repeats so
  regularly that each month's historical average is a strong forecast.
""")

st.caption(
    "Data source: Central Pollution Control Board (CPCB), India. "
    "Analysis by Raina Samanta."
)
