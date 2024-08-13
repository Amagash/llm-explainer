import gensim.downloader
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


model = gensim.downloader.load('glove-wiki-gigaword-50')
words = ["cat", "dog", "car", "truck"]
print(words[0], model[words[0]])
print(words[1], model[words[1]])
print(words[2], model[words[2]])
print(words[3], model[words[3]])

vector_1 = model[words[0]][0:3]
vector_2 = model[words[1]][0:3]
vector_3 = model[words[2]][0:3]
vector_4 = model[words[3]][0:3]

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')

ax.text(vector_1[0], vector_1[1], vector_1[2], words[0])
ax.text(vector_2[0], vector_2[1], vector_2[2], words[1])
ax.text(vector_3[0], vector_3[1], vector_3[2], words[2])
ax.text(vector_4[0], vector_4[1], vector_4[2], words[3])

soa = np.array([[0, 0, 0, vector_1[0], vector_1[1], vector_1[2]], 
                [0, 0, 0, vector_2[0], vector_2[1], vector_2[2]],
                [0, 0, 0, vector_3[0], vector_3[1], vector_3[2]],
                [0, 0, 0, vector_4[0], vector_4[1], vector_4[2]],
                ])

X, Y, Z, U, V, W = zip(*soa)
ax.quiver(X, Y, Z, U, V, W, color=['r','b','g','y'])
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()