import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def intro():
    st.title("Taviloc")

    with st.expander("Introduction"):
        st.markdown(
            "**Aortic valve prostheses** are becoming an increasingly popular option for patients with severe aortic stenosis and high surgical risk [1]."
        )
        st.markdown(
            "The TAVI placement process is typically a **manual** task, which means no two prostheses are positioned exactly the same way."
        )
        st.markdown(
            "**Height** of placement is a crucial factor to consider due to its potential impact on the conduction system and, consequently, the rate of permanent pacemaker implantation post-procedure [2]. Nevertheless, the effect of TAVI height on hemodynamic flow has not yet been studied."
        )
        st.markdown(
            "Currently, the influence of **prosthesis alignment** is an increasingly studied factor. For example, the ACA clinical trial is examining how commissural alignment affects various clinical parameters [3]. This has also been studied through CFD simulations, though only with virtual geometries and always limited to the aortic root and ascending aorta [4]."
        )
        st.markdown(
            "This article aims to examine the **impact** of TAVI placement height and alignment on hemodynamic flow."
        )


def plot(data, x, y, hue):
    fig, ax = plt.subplots()
    df = pd.read_csv(data)
    fig = sns.catplot(
        data=df,
        x=x,
        y=y,
        hue=hue,
        kind="box",
        palette="pastel",
    )
    plt.ylabel("Velocity (m/s)")
    st.pyplot(fig)
    st.caption("Velocity distributions in m/s")
    st.dataframe(df, hide_index=True)
