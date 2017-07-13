# from the sys package import argv feature 
from sys import argv
# from the imported argv, assign the script filename to variable script
# then assign the second argument to the variable filename
script, filename = argv
# define variable and fill it with contents of the file at filename
txt = open(filename)
# print string and title of the filename, then txt (text file contents)
print "Here's your file %r." % filename
print txt.read()
# print string and take raw input, storing to a new variable for the file name
print "Type the filename again:"
file_again = raw_input("> ")
# open the file through this newly input filename and store to new var
txt_again = open(file_again)
# print this variable, reading only 8 bytes
print txt_again.read(8)

txt.close()
txt_again.close()
print 'Files have been closed.'
