import streamlit as st

level = st.slider("Select the level", 0, 16)
st.text('Selected: {}'.format(level**2))
