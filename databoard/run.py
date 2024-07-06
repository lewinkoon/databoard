import streamlit as st

pg = st.navigation({
    "Reports": [
        st.Page("reports/intro.py", title="Introduction", icon="📝"),
        st.Page("reports/velocity.py", title="Velocity"),
        st.Page("reports/pressure.py", title="Pressure"),
        st.Page("reports/shear.py", title="Wall Shear Stress"),
        st.Page("reports/mass-flow.py", title="Mass Flow"),
    ]}
)
pg.run()
