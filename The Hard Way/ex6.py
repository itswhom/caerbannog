# define x as a string with a format character for the types of people
x = "There are %d types of people." % 10
# define binary as a string
binary = "binary"
# define do_not as a string
do_not = "don't"
# define y as a string with format characters
y = "those who know %s and those who %s." % (binary, do_not)
# print x and y on separate lines
print x
print y
# print strings which also call variables with format characters
print "I said: %r." % x
print "I also said: '%s'." % y
# define boolean variable and a string with an open format character
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# print variable with open format character, and fill it with other var value
print joke_evaluation % hilarious
# define two strings
w = "This is the left side of..."
e = "a string with a right side."
# print those two strings on the same line
print w + e
