import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

BOUNDARIES = "data/boundaries.csv"

st.header("Mass flow", divider="rainbow")

cont = st.container(border=True)
cont.markdown(
    "The alteration in the implantation height of the prosthesis valve does not exert an impact on the mass flow through the outlets."
)

df = pd.read_csv(BOUNDARIES)
df = df[["Height", "Location", "Mass Flow", "X", "Y", "Z"]]
df = df[
    df["Location"].isin(
        [
            "Right Carotid",
            "Left Carotid",
            "Right Subclavian",
            "Left Subclavian",
            # "Outlet",
        ]
    )
]
df["Mass Flow"] = df["Mass Flow"] * -1000000

st.subheader("Boundaries")
tab1, tab2, tab3 = st.tabs(["Low", "Neutral", "High"])
with tab1:
    df1 = df[df["Height"] == "Low"]
    fig1, ax1 = plt.subplots()
    sns.violinplot(
        data=df1, x="Mass Flow", y="Location", ax=ax1, split=True, inner="quart"
    )
    plt.xlabel("Mass Flow (mg/s)")
    plt.xlim(-25, 600)
    tab1.pyplot(fig1)
    # st.dataframe(df1)

with tab2:
    df2 = df[df["Height"] == "Neutral"]
    fig2, ax2 = plt.subplots()
    sns.violinplot(
        data=df2, x="Mass Flow", y="Location", ax=ax2, split=True, inner="quart"
    )
    plt.xlabel("Mass Flow (mg/s)")
    plt.xlim(-25, 600)
    tab2.pyplot(fig2)
    # st.dataframe(df2)

with tab3:
    df3 = df[df["Height"] == "High"]
    fig3, ax3 = plt.subplots()
    sns.violinplot(
        data=df3, x="Mass Flow", y="Location", ax=ax3, split=True, inner="quart"
    )
    plt.xlabel("Mass Flow (mg/s)")
    plt.xlim(-25, 600)
    tab3.pyplot(fig3)
    # st.dataframe(df3)
