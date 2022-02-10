# Reads in a students percentage mark and prints out corresponding grade
# Author: Shane O'Gorman

grade = round(float(input("Enter the percentage: ")),0)

# Checks percentage and returns correct grade
if (grade <= 40):
    print("Fail")
elif (grade >= 40 and grade <= 49):
    print("Pass")
elif (grade >= 50 and grade <= 59):
    print("Merit 2")
elif (grade >= 60 and grade <= 69):
    print("Merit 1")
elif (grade >= 70 and grade <= 100):
    print("Distinction")
else:# If out of bounds will be given an error
    print("Error: Please enter a percentage between 0 and 100")