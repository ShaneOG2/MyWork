# Lab3.1.2
# Reads in two numbers and takes first away from second and returns result
# Author: Shane O'Gorman 

# Input reads in a string so we need to convert to int so we can perform math computation 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

ans = num1 - num2 

print("{} minus {} is {}".format(num1, num2, ans))
