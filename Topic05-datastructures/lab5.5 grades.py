# Write a program that will read in the data for the data structure above, ie
# reads in a student’s name, then keeps reading in their modules and grades
# (until the user enters a blank module name), 
# You can break this up into two parts:
# a. Just read in the module names until the user enters blank,
# b. Then read in the grade as well
# This program can just read in one student (and their module details)

student = {} # Creates blank dict
name = input("Please enter the students name: ")
student["name"] = name # Adds key name and value name into dict

module = "blank" # Create a blank string
modules = [] # Create a blank list

while module != "": # Until nothing is inputed ask for a module
    module = input("Please enter the students module: ")
    if module == "":
        break # Won't add to list if blank
    modules.append({"courseName": module}) # Add a dictionary with key courseName and inputted module

student["modules"] = modules # Adds a key modules and values inputted list modules


for module in student["modules"]: # For each module dictionary we input the grade for each
    percent = int(input("Please input grade percentage for " + module["courseName"] + ": "))
    check = True
    while check == True:
        if percent >=0 and percent <=100:
            module.update({"grade": percent})
            break
        else: 
            percent = int(input("Grade must be between 0-100. Please input grade percentage for " + module["courseName"] + ": "))

print(student)

