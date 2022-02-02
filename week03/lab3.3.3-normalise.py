#
# Author: Shane O'Gorman 

inputStr = input("Please enter a string: ")
inputStrLen = len(inputStr)

newStr = (inputStr.strip()).lower()
newStrLen = len(newStr)

print("That String normalised is: {}".format(newStr))
print("We reduced the input string from {} to {} characters".format(inputStrLen, newStrLen))