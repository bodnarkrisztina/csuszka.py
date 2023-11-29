import streamlit as st

st.write("2 Hatványai") 
level = st.slider("Kettő hatványai:", 0, 16)
st.text('Hatványa: {}'.format(2**level))
