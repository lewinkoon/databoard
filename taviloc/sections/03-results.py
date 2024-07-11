import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

SECTIONS = "data/sections.csv"
WALLS = "data/walls.csv"
BOUNDARIES = "data/boundaries.csv"

with st.sidebar:
    parameter = st.selectbox("Choose parameter.", ("Velocity", "Shear", "Mass Flow"))
    height = st.selectbox("Select prosthesis height.", ("Low", "Neutral", "High"))

st.title(f"Results 📊 - {parameter}")

if parameter == "Velocity":
    st.header(f"{parameter} contours", divider="rainbow")
    st.markdown(
        """
        An elevation in the placement height of the valve prosthesis leads to heightened velocities within the ascending aorta region. Nevertheless, this velocity disparity diminishes with increasing distance from the aortic valve.
        """
    )

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.image("assets/velocity-low-s1.png")
        col2.image("assets/velocity-low-s2.png")
        col3.image("assets/velocity-low-s3.png")
        col4.image("assets/velocity-low-s4.png")
        col5.image("assets/velocity-low-s5.png")
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.image("assets/velocity-neutral-s1.png")
        col2.image("assets/velocity-neutral-s2.png")
        col3.image("assets/velocity-neutral-s3.png")
        col4.image("assets/velocity-neutral-s4.png")
        col5.image("assets/velocity-neutral-s5.png")
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.image("assets/velocity-high-s1.png")
        col2.image("assets/velocity-high-s2.png")
        col3.image("assets/velocity-high-s3.png")
        col4.image("assets/velocity-high-s4.png")
        col5.image("assets/velocity-high-s5.png")
    st.image("assets/velocity-legend.png", caption="Velocity contours.")

    df = pd.read_csv(SECTIONS)
    df = df[["Height", "Location", parameter, "X", "Y", "Z"]]
    df = df[df["Height"] == height]
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x=parameter, y="Location", ax=ax, split=True, inner="quart")
    plt.xlabel("Velocity (m/s)")
    plt.xlim(-0.1, 0.6)
    st.pyplot(fig)

    # st.markdown(
    #     """
    #     The following velocity contours show the significant increment on velocity in higher tavi placements.
    #     """
    # )

    st.header(f"{parameter} field", divider="rainbow")
    st.image(
        f"assets/{parameter.lower()}-{height.lower()}.png", caption=f"{height} height."
    )

    st.header(f"{parameter} data", divider="rainbow")
    st.dataframe(df, use_container_width=True)
elif parameter == "Shear":
    with st.expander("See definition", expanded=True, icon="🔥"):
        st.markdown(
            """
            **Wall shear stress** expresses the retarding force (per unit area) from a wall in the layers of a fluid flowing next to the wall.
            """
        )
        st.latex(r"\tau_\omega = \mu \frac{\partial u}{\partial y}")
        st.markdown(
            """
            It is used, for example, in the description of arterial blood flow, in which case there is evidence that it affects the **atherogenic** process.
            """
        )
    st.header(f"{parameter} contours", divider="rainbow")
    st.markdown(
        """
        The adjustment of valve prosthesis placement height leads to elevated shear stress values in the ascending aorta. Conversely, this adjustment has no discernible impact on the regions of the aortic arch and descending aorta, as expected.
        """
    )
    df = pd.read_csv(WALLS)
    df = df[["Height", "Location", parameter]]
    df = df[df["Height"] == height]
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x=parameter, y="Location", ax=ax, split=True, inner="quart")
    plt.xlabel("Shear (Pa)")
    # plt.xlim(-0.5, 2.5)
    st.pyplot(fig)

    st.header(f"{parameter} field", divider="rainbow")
    st.image(
        f"assets/{parameter.lower()}-{height.lower()}.png", caption=f"{height} height."
    )

    st.header(f"{parameter} data", divider="rainbow")
    st.dataframe(df, use_container_width=True)
elif parameter == "Mass Flow":
    st.header(f"{parameter} contours", divider="rainbow")
    df = pd.read_csv(BOUNDARIES)
    df = df[["Height", "Location", parameter, "X", "Y", "Z"]]
    df = df[
        df["Location"].isin(
            [
                "RCA",
                "LCA",
                # "Right Subclavian",
                # "Left Subclavian",
                # "Outlet",
            ]
        )
    ]
    df[parameter] = df[parameter] * -1000000
    df = df[df["Height"] == height]
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x=parameter, y="Location", ax=ax, split=True, inner="quart")
    plt.xlabel("Mass Flow (mg/s)")
    # plt.xlim(-25, 100)
    st.pyplot(fig)
