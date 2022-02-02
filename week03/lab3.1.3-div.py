# Lab3.1.3
# Reads in two numbers and divides first number by second
# Return the int result and it's remainder 
# Author: Shane O'Gorman 

# Converts inputted numbers from str to int
num1 = int(input("Enter first number: "))
num2 = int(input("Enter the number you want to divide by: "))

# Calculates what divides into the num and remainder
ans = num1//num2
rem = num1%num2 

print("{} divided by {} is {} with remainder {}".format(num1, num2, ans, rem))



