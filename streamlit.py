import streamlit as st
import pandas as pd
import numpy as np
import gensim.downloader
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from data import make_plot

st.title('LLM explainer')

st.write("Choose words you would like to visualize (separare with one space):")
txt = st.text_input("word_1", key="word_1")

words = txt.split(" ")
make_plot(words)