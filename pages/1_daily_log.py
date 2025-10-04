from datetime import date

import streamlit as st

from utils.helper import init_db, add_entry

# --- Page UI ---
st.title("📅 Daily Log")

init_db()

with st.form("log"):
    day = st.date_input("Date", value=date.today())

    st.subheader("⚡ Power Habits")
    gym = st.checkbox("Gym / Workout")
    hydration = st.number_input("Hydration (L)", min_value=0.0, step=0.5)
    german = st.number_input("German study (mins)", min_value=0, step=5)
    ai = st.number_input("AI / Agent Work (hrs)", min_value=0.0, step=0.5)

    st.subheader("🎭 Root Habits")
    yt = st.number_input("YouTube (mins)", min_value=0, step=5)
    comfort = st.checkbox("Comfort food today?")

    notes = st.text_area("Reflection / Notes")

    submitted = st.form_submit_button("💾 Save")

if submitted:
    power = int(gym) + (1 if hydration >= 2 else 0) + (1 if german >= 20 else 0) + (2 if ai >= 1 else 0)
    root = (yt // 15) + int(comfort)

    add_entry(day.isoformat(), power, root, notes)
    st.success(f"Saved ✅ Power:Root = {power}:{max(root,1)}")
