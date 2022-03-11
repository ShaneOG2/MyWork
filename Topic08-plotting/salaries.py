# Creates a randon array of salaries and uses operators to add/multiply and create new arrays
# Author: Shane O'Gorman 

import numpy as np 

# This keeps the randon numbers generate the same each time we run the program
np.random.seed(1)

# Sets values
minSalary = 20000
maxSalary = 80000
numOfEnteries = 10

# Generate an array salaries
salaries = np.random.randint(minSalary,maxSalary,numOfEnteries)

# Adds 5000 to each value in array salaries
salariesRaise1 = salaries + 5000

# Increases all salaries by 5%
salariesRaise2 = salaries * 1.05

print(salaries)
print(salariesRaise1)
print(salariesRaise2)