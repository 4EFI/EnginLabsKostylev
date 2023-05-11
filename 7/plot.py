
import matplotlib.pyplot as plt
import numpy as np

data_u_arr = []

du = 0
dt = 0

with open("settings.txt", "r") as f:
    du = float( f.readline() )
    dt = float( f.readline() )

print( du, dt )

with open("data.txt", "r") as f:
    for x in f.readlines():
        data_u_arr.append( list(map(float, x.split())) )

data_u = np.array( data_u_arr, dtype=np.double )

data_u *= ( 3.3 / 256 ) 

t = dt * len( data_u )

print( "full time =", t, "sec"  )

print( len(data_u_arr)/82 )

x_main_ticks = []

plt.plot( data_u, "-", lw = 2)
plt.grid()
plt.show()

plt.savefig("out.png")

f.close()