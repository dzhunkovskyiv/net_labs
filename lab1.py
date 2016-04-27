import networkx as nx
import matplotlib.pyplot as plt
from random import random
import numpy as np

adjacency_matr = []
list_of_adj = []
list_to_draw = [] #list of (i, j) that will be used to draw net
n = random()*10###################################################### setting number of net's edges

for i in range(n):
    for j in range(n):
        a = random()
        if a > 0.7:
            list_of_adj.append(1)
            list_to_draw.append((i, j))
        else:
            list_of_adj.append(0)
    adjacency_matr.append(list_of_adj)
    list_of_adj = []

######################################Calculating number of edges connection
list_of_k_out = []
sum_of_out = 0

for i in range(n):
    for j in range(n):
       if adjacency_matr[i][j] == 1:
            sum_of_out += 1
    if sum_of_out >= 1:
        list_of_k_out.append(sum_of_out)
    else:
        list_of_k_out.append(1)
    sum_of_out = 0

##############################################Formating of matrix D
matr_D = []
list_of_matr_D = []

for i in range(n):
    for j in range(n):
        if i == j:
            list_of_matr_D.append(list_of_k_out[i])
        else:
            list_of_matr_D.append(0)
    matr_D.append(list_of_matr_D)
    list_of_matr_D = []

##################################Calculating of
D = np.matrix(matr_D)
A = np.matrix(adjacency_matr)
I = []

for i in range(n):
    I.append(1)

list_x_of_PR = np.dot(np.dot(D, np.linalg.inv(D - np.dot(0.85, A))), I)


print list_x_of_PR

#################################Drawing and showing of net
DG = nx.DiGraph()
DG.add_edges_from(list_to_draw)
nx.draw(DG)
plt.show()
