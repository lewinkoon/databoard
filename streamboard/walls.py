import streamlit as st
import streamboard.helpers as db

WALLS = "data/walls.csv"

st.header("Shear walls", divider="grey")
db.plot(WALLS, "Location", "Shear", "Height")
