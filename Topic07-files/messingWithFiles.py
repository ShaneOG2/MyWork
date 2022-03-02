
# Write a function that reads in a number from a file that already exists
# (count.txt). test the program by calling the function and outputting the
# number.
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

# Write a function that takes in a number and overwrites a file with that
# number (count.txt). test it and check that the file has been changed
def writeNumber(num):
    with open(filename, "wt") as f:
        f.write(str(num)) # Must take in a string

# Create an “init” program that initializes the file, in this case it will just put 0
# into the file.
import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print ("File does not exist")
    #initialise file
    writeNumber(0)

def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie 0 previous runs
        return 0

# Write a program that, uses these two functions, to count how many times
# the program has been run. Test it, check to see that the number goes up
# each time.

num = readNumber()
num += 1
print("We have run this program", num, "times")
writeNumber(num)