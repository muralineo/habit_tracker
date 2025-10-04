import streamlit as st
import pandas as pd
from datetime import date, timedelta
import altair as alt

from utils.helper import get_entries_df

st.title("📊 Weekly Summary")

df = get_entries_df()
if not df.empty:
    df["day"] = pd.to_datetime(df["day"]).dt.date
    start_of_week = date.today() - timedelta(days=date.today().weekday())
    weekly = df[df["day"] >= start_of_week].copy()
    weekly.sort_values("day", inplace=True)

    if not weekly.empty:
        weekly["day_str"] = pd.to_datetime(weekly["day"]).dt.strftime("%a %d")
        day_order = weekly["day_str"].tolist()

        melted = weekly.melt(
            id_vars=["day_str"],
            value_vars=["power", "root"],
            var_name="Habit",
            value_name="Score"
        )

        chart = (
            alt.Chart(melted)
            .mark_bar(width=18)
            .encode(
                x=alt.X("day_str:N", title="Day", sort=day_order),
                xOffset="Habit:N",
                y=alt.Y("Score:Q", title="Score"),
                color=alt.Color("Habit:N",
                                scale=alt.Scale(domain=["power","root"],
                                                range=["#2ecc71","#e74c3c"])),
                tooltip=["day_str:N", "Habit:N", "Score:Q"]
            )
            .properties(width={"step": 40})
        )

        st.altair_chart(chart, use_container_width=True)

        total_power = int(weekly["power"].sum())
        total_root = int(weekly["root"].sum())
        ratio = f"{total_power}:{max(total_root,1)}"

        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Total Power", total_power)
        with c2: st.metric("Total Root", total_root)
        with c3: st.metric("Power:Root Ratio", ratio)

    st.subheader("📖 All Entries")
    st.dataframe(df.sort_values("day", ascending=False))
    st.download_button(
        "⬇️ Download CSV",
        df.to_csv(index=False),
        "habit_curve.csv",
        "text/csv",
    )
