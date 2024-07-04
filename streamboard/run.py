import streamlit as st

pg = st.navigation(
    [
        st.Page("intro.py", title="Introduction"),
        st.Page("sections.py", title="Sections"),
        st.Page("walls.py", title="Walls"),
    ]
)
pg.run()
