# Creates a plot of salaries vs. age
# Author: Shane O'Gorman 

from turtle import color
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

#Set Values
minAge = 21
maxAge = 65

# Generate an array salaries
ages = np.random.randint(minAge,maxAge,numOfEnteries)

xpoints = np.array(range(1,101))
ypoints = xpoints**2

plt.scatter(ages,salaries,label="salaries")
plt.plot(xpoints,ypoints,color="red",label="x Squared")

plt.title("random plot")
plt.xlabel("salaries")
plt.ylabel("age")
plt.legend()
#plt.show()
plt.savefig("prettier-plot.png")