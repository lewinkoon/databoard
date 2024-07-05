import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

SECTIONS = "data/sections.csv"

st.header("Pressure", divider="rainbow")

cont = st.container(border=True)
cont.markdown(
    "The elevation of the prosthetic valve placement height induces heightened pressures in the area of the ascending aorta. However, this pressure variance diminishes as the measurement location moves further from the aortic valve."
)

df = pd.read_csv(SECTIONS)
df = df[["Height", "Location", "Pressure", "X", "Y", "Z"]]

st.subheader("Sections")
tab1, tab2, tab3 = st.tabs(["Low", "Neutral", "High"])
with tab1:
    df1 = df[df["Height"] == "Low"]
    fig1, ax1 = plt.subplots()
    sns.violinplot(
        data=df1, x="Pressure", y="Location", ax=ax1, split=True, inner="quart"
    )
    plt.xlabel("Pressure (Pa)")
    plt.xlim(15995, 16025)
    tab1.pyplot(fig1)
    # st.dataframe(df1)

with tab2:
    df2 = df[df["Height"] == "Neutral"]
    fig2, ax2 = plt.subplots()
    sns.violinplot(
        data=df2, x="Pressure", y="Location", ax=ax2, split=True, inner="quart"
    )
    plt.xlabel("Pressure (Pa)")
    plt.xlim(15995, 16025)
    tab2.pyplot(fig2)
    # st.dataframe(df2)

with tab3:
    df3 = df[df["Height"] == "High"]
    fig3, ax3 = plt.subplots()
    sns.violinplot(
        data=df3, x="Pressure", y="Location", ax=ax3, split=True, inner="quart"
    )
    plt.xlabel("Pressure (Pa)")
    plt.xlim(15995, 16025)
    tab3.pyplot(fig3)
    # st.dataframe(df3)

st.subheader("Pressure field")
tab1, tab2, tab3 = st.tabs(["Low", "Neutral", "High"])
tab1.image("assets/pressure-low.png", caption="Low height.")
tab2.image("assets/pressure-neutral.png", caption="Neutral height.")
tab3.image("assets/pressure-High.png", caption="High height.")
