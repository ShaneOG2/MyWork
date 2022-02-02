# Converts dollars and cents into cents
# Author: Shane O'Gorman 

# Inputs amount in floats and returns the absolute int 
amount = float(input("Please enter an amount: "))
converted = int(abs(amount*100))

print("That amount in cent is: {}".format(converted))