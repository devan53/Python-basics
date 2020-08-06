import numpy as np
import math
import matplotlib.pyplot as plt
x_range_deg = range(0, 360)
x_range_deg_slice = x_range_deg[::5]

x_range = np.divide(x_range_deg_slice,(math.pi/float(180)))
y_range = np.tan(x_range)

plt.plot(x_range, y_range, color = "red", marker = ".")
plt.title("sine wave b/w -360 to 360")
plt.xlabel("Angle values in radians")
plt.ylabel("Sine values of angles")
plt.show()
