import gensim.downloader
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import streamlit as st

def make_plot(words):
  model = gensim.downloader.load('glove-wiki-gigaword-50')
  fig = plt.figure(figsize = (10,10))
  ax = plt.axes(projection='3d')
  list_of_vectors = []

  for word in words:
    vector = model[word][0:3]
    ax.text(vector[0], vector[1], vector[2], word)
    vector_2 = np.append([0, 0, 0], vector)
    list_of_vectors.append(vector_2)

  soa = np.array(list_of_vectors)
  X, Y, Z, U, V, W = zip(*soa)
  ax.quiver(X, Y, Z, U, V, W)
  ax.set_xlim([-1.5, 1.5])
  ax.set_ylim([-1.5, 1.5])
  ax.set_zlim([-1.5, 1.5])
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z')
  return fig


  