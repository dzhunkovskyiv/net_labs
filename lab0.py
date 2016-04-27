from random import random
import matplotlib.pyplot as plt

##################################Formation of random matrix
matr = []
list = []

for i in range(1000):
    for j in range(1000):
        if random() > 0.5:
            list.append(1)
        else:
            list.append(0)
    matr.append(list)
    list = []

#############################Formating dict{ n : m}
############################# n - number of connections
############################# m - number of edges with such connections

dict_of_ranges = {}
number_of_connection = 0

for i in range(1000):
    for j in range(1000):
        if matr[i][j] == 1:
            number_of_connection += 1
    if (str(number_of_connection) in dict_of_ranges.keys()):
        dict_of_ranges[str(number_of_connection)] += 1
    else:
        dict_of_ranges[str(number_of_connection)] = 1
    number_of_connection = 0
print(dict_of_ranges)


##############################Formation of x_label and y_label axis and drawing of graph
x_label = []
y_label = []

list_of_keys = sorted(dict_of_ranges.keys())
for element in list_of_keys:
    x_label.append(int(element))
print(x_label)


for element in list_of_keys:
    y_label.append(dict_of_ranges[element])
print(y_label)


plt.plot(x_label, y_label)
plt.show()
