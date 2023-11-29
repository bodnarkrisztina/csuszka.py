import streamlit as st

level = st.slider("Kettő hatványai:", 0, 16)
st.text('Hatványa: {}'.format(level**2)) 
