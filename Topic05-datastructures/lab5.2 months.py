# Create a tuple that stores the months of the year, from that tuple create
# another tuple with just the summer months (May, June, July), print out the
# summer months one at a time. 

# Author: Shane O'Gorman

# Stores months in tuple
allMonths = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Takes summer months out of tuple and into summer months tuple
summerMonths = allMonths[4:7]

# Prints each month in summer months tuple
for month in summerMonths:
    print(month)