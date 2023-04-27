import matplotlib.pyplot as plt

with open("data.txt", "r") as f:
    data_x = []
    data_y = []
    for x in f.readlines():
        spis = []
        spis = list(map(float, x.split()))
        data_x.append(spis[0])
        data_y.append(spis[1])

plt.plot(data_x, data_y, ".")
plt.show()