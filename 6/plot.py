import matplotlib.pyplot as plt

data_x = []

with open("data.txt", "r") as f:
    for x in f.readlines():
        spis = []
        spis = list(map(float, x.split()))
        data_x.append(spis[0])

print( len(data_x)/82 )

plt.plot(data_x, ".")
plt.show()

f.close()