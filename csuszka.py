import streamlit as st

st.header("2 Hatványai") 
level = st.slider("Kettő hatványai:", 0, 16)
st.text('Hatványa: {}'.format(level**2))
