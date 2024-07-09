import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

SECTIONS = "data/sections.csv"

st.title("Results")
st.header("Velocity", divider="rainbow")

cont = st.container(border=True)
cont.markdown(
    "An elevation in the placement height of the valve prosthesis leads to heightened velocities within the ascending aorta region. Nevertheless, this velocity disparity diminishes with increasing distance from the aortic valve."
)

df = pd.read_csv(SECTIONS)
df = df[["Height", "Location", "Velocity", "X", "Y", "Z"]]
tab1, tab2, tab3 = st.tabs(["Low", "Neutral", "High"])

with tab1:
    df1 = df[df["Height"] == "Low"]
    fig1, ax1 = plt.subplots()
    sns.violinplot(
        data=df1, x="Velocity", y="Location", ax=ax1, split=True, inner="quart"
    )
    plt.xlabel("Velocity (m/s)")
    plt.xlim(-0.1, 0.6)
    tab1.pyplot(fig1)
    # st.dataframe(df1)

with tab2:
    df2 = df[df["Height"] == "Neutral"]
    fig2, ax2 = plt.subplots()
    sns.violinplot(
        data=df2, x="Velocity", y="Location", ax=ax2, split=True, inner="quart"
    )
    plt.xlabel("Velocity (m/s)")
    plt.xlim(-0.1, 0.6)
    tab2.pyplot(fig2)
    # st.dataframe(df2)

with tab3:
    df3 = df[df["Height"] == "High"]
    fig3, ax3 = plt.subplots()
    sns.violinplot(
        data=df3, x="Velocity", y="Location", ax=ax3, split=True, inner="quart"
    )
    plt.xlabel("Velocity (m/s)")
    plt.xlim(-0.1, 0.6)
    tab3.pyplot(fig3)
    # st.dataframe(df3)

# st.image("assets/sections.png", caption="Velocity contours for each section.")
st.subheader("Velocity field")
tab1, tab2, tab3 = st.tabs(["Low", "Neutral", "High"])
tab1.image("assets/velocity-low.png", caption="Low height.")
tab2.image("assets/velocity-neutral.png", caption="Neutral height.")
tab3.image("assets/velocity-high.png", caption="High height.")
