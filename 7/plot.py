import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

with open( "settings.txt", "r" ) as settings:
    tmp = [float(i) for i in settings.read().split( "\n" )]

data_array = np.loadtxt( "data.txt", dtype=np.double )

size       = np.shape(data_array)[0]
maximum    = data_array.max()
maxIndex   = np.where (data_array == maximum)
chargeTime = maxIndex[0][0] * tmp[0]
time2      = (size - maxIndex[0][0]) * tmp[0]

timeArr = np.arange(size) * tmp[0]

fig, ax = plt.subplots( figsize=(16, 10) )

ax.plot(timeArr, data_array, '-', linewidth=2, color='black')
ax.set_xlabel("Время, c")
ax.set_ylabel("Напряжение, B")
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")
ax.legend ("V(t)")
ax.text(15, 1,   f"Время заряда t = {chargeTime} c")
ax.text(15, 0.5, f"Время разряда t = {time2} c")
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0, 3.5)
ax.set_xlim(0, 150)
ax.grid( which='minor', linewidth=0.5, linestyle='dashed' )
ax.grid( which='major', linewidth=1 )
fig.savefig("plot.png")