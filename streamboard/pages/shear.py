import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

WALLS = "data/walls.csv"

st.header("Wall Shear Stress", divider="rainbow")

st.markdown(
    "**Wall shear stress** expresses the retarding force (per unit area) from a wall in the layers of a fluid flowing next to the wall."
)
st.latex(r"\tau_\omega = \mu \frac{\partial u}{\partial y}")
st.markdown(
    "It is used, for example, in the description of arterial blood flow, in which case there is evidence that it affects the **atherogenic** process."
)
cont = st.container(border=True)
cont.markdown(
    "The adjustment of valve prosthesis placement height leads to elevated shear stress values in the ascending aorta. Conversely, this adjustment has no discernible impact on the regions of the aortic arch and descending aorta, as expected."
)

df = pd.read_csv(WALLS)
df = df[["Height", "Location", "Shear"]]

st.subheader("Surface sections")
tab1, tab2, tab3 = st.tabs(["Low", "Neutral", "High"])
with tab1:
    df1 = df[df["Height"] == "Low"]
    fig1, ax1 = plt.subplots()
    sns.violinplot(data=df1, x="Shear", y="Location", ax=ax1, split=True, inner="quart")
    plt.xlabel("Shear (Pa)")
    plt.xlim(-0.5, 2.5)
    tab1.pyplot(fig1)
    # st.dataframe(df1)

with tab2:
    df2 = df[df["Height"] == "Neutral"]
    fig2, ax2 = plt.subplots()
    sns.violinplot(data=df2, x="Shear", y="Location", ax=ax2, split=True, inner="quart")
    plt.xlabel("Shear (Pa)")
    plt.xlim(-0.5, 2.5)
    tab2.pyplot(fig2)
    # st.dataframe(df2)

with tab3:
    df3 = df[df["Height"] == "High"]
    fig3, ax3 = plt.subplots()
    sns.violinplot(data=df3, x="Shear", y="Location", ax=ax3, split=True, inner="quart")
    plt.xlabel("Shear (Pa)")
    plt.xlim(-0.5, 2.5)
    tab3.pyplot(fig3)
    # st.dataframe(df3)

tab1, tab2, tab3 = st.tabs(["Low", "Neutral", "High"])
tab1.image("assets/shear-low.png", caption="Low height.")
tab2.image("assets/shear-neutral.png", caption="Neutral height.")
tab3.image("assets/shear-High.png", caption="High height.")
