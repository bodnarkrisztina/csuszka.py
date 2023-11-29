import streamlit as st

st.title("2 Hatványai") 
level = st.slider("Kettő hatványai:", 0, 16)
st.text('Hatványa: {}'.format(level**2))
