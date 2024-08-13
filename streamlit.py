import streamlit as st
import pandas as pd
import numpy as np
import gensim.downloader
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

st.title('LLM explainer')

st.write("Choose words you would like to visualize (separare with one space):")
txt = st.text_input("word_1", key="word_1")

words = txt.split(" ")
print(type(words))
print(words)

model = gensim.downloader.load('glove-wiki-gigaword-50')
print(words[0], model[words[0]])
print(words[1], model[words[1]])

vector_1 = model[words[0]][0:3]
vector_2 = model[words[1]][0:3]

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')

ax.text(vector_1[0], vector_1[1], vector_1[2], words[0])
ax.text(vector_2[0], vector_2[1], vector_2[2], words[1])

soa = np.array([[0, 0, 0, vector_1[0], vector_1[1], vector_1[2]], 
                [0, 0, 0, vector_2[0], vector_2[1], vector_2[2]]
                ])

X, Y, Z, U, V, W = zip(*soa)
ax.quiver(X, Y, Z, U, V, W, color=['r','b'])
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

st.pyplot(fig)