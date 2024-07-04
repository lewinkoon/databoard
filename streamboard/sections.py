import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

SECTIONS = "data/sections.csv"

st.header("Velocity sections", divider="blue")

st.markdown("")

st.image("assets/sections.png", caption="Velocity contours for each section.")

fig, ax = plt.subplots()
df = pd.read_csv(SECTIONS)
fig = sns.catplot(
    data=df,
    x="Location",
    y="Velocity",
    hue="Height",
    kind="violin",
    palette="pastel",
)
plt.ylabel("Velocity (m/s)")
st.pyplot(fig)
st.caption("Velocity distributions in m/s")
st.dataframe(df, hide_index=True)
