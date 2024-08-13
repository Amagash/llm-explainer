import streamlit as st
from data import make_plot

st.title('LLM explainer')

st.write("Choose words you would like to visualize (separare with one space):")
txt = st.text_input("word_1", key="word_1")

words = txt.split(" ")
fig = make_plot(words)
st.pyplot(fig)