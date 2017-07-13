# import argument variables
from sys import argv
# unpack argv variable into script, and three additional variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# start added at 0
added = 0

# determine if inputs are integers
# if so, add them to variable added

# THIS PART IS WAY BROKEN ***********
# COME BACK AND FIX *****************
try:
    check = int(first)
except ValueError:
    print "this is an error"
added = added + int(first)
if int(second) > 1 or int(second) < 2:
    added = added + int(second)
if int(third) > 1 or int(third) < 2:
    added = added + int(third)

# added = first + second + third
print added








# try:
#    val = int(userInput)
# except ValueError:
#    print("That's not an int!")
