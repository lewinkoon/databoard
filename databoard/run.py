import streamlit as st

pg = st.navigation(
    {
        "sections": [
            st.Page("sections/01-intro.py", title="Introduction", icon="📝"),
            st.Page("sections/02-methods.py", title="Methods", icon="🛠️"),
            st.Page("sections/03-results.py", title="Results", icon="📊"),
            st.Page("sections/04-discussion.py", title="Discussion", icon="🧵"),
            st.Page("sections/05-conclussions.py", title="Conclussions", icon="📌"),
        ]
    }
)
pg.run()
