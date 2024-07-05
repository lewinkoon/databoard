import streamlit as st

pg = st.navigation(
    [
        st.Page("pages/intro.py", title="Introduction"),
        st.Page("pages/velocity.py", title="Velocity"),
        st.Page("pages/pressure.py", title="Pressure"),
        st.Page("pages/shear.py", title="Wall Shear Stress"),
        st.Page("pages/mass-flow.py", title="Mass Flow"),
    ]
)
pg.run()
