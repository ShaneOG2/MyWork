# Write a function that prints out a menu of commands we can perform, ie add,
# view and quit. The function should return what the user chose. 
# Author: Shane O'Gorman 

def displayMenu():
    print("What would you like to do?")
    print("\t (a) Add new student")
    print("\t (v) View students")
    print("\t (q) Quit")

    val = input("Type one letter (a/v/q): ").strip()
    return val

def doAdd(students):
    currentStudent = {} # Creates blank dir currentStudent
    currentStudent["name"] = input("Enter students name: ") # Adds key name value inputted name
    currentStudent["modules"] = readModules() # Adds key modules value call function readModules

    students.append(currentStudent) # Adds current student to students list

def readModules():
    modules = [] 
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)

        moduleName=input("\tEnter next module name (blank to quit):").strip()

        return modules

def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"])) 

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])


students = []
choice = displayMenu()
while choice != "q":
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    elif choice != "q":
        print("\n\nPlease select either (a), (v) and (q)")
    choice = displayMenu()