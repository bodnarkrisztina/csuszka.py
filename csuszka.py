import streamlit as st

level = st.slider("Kettő hatványai:", 0, 16)
st.text('Selected: {}'.format(level**2))
