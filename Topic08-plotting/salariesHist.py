# Creates a randon array of salaries and uses operators to add/multiply and create new arrays
# Author: Shane O'Gorman 

import numpy as np 
import matplotlib.pyplot as plt

# This keeps the randon numbers generate the same each time we run the program
np.random.seed(1)

# Sets values
minSalary = 20000
maxSalary = 80000
numOfEnteries = 10

# Generate an array salaries
salaries = np.random.randint(minSalary,maxSalary,numOfEnteries)

plt.hist(salaries)
plt.show()