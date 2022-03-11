# 
# Author: Shane O'Gorman

import matplotlib.pyplot as plt
import numpy as np 

xpoints = np.array(range(1,101))
ypoints = xpoints**2

plt.plot(xpoints,ypoints)
plt.show()

#print(xpoints)
#print(ypoints)