name = 'Joseph Whom'
age = 31 # not a lie
height = 6 * 12 + 4 # inches
weight = 155 # lbs
eyes = 'Brown'
teeth = 'White-ish'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %s inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# 1 lbs = 0.4536 kg
print "%s is %d kilograms of mass." % (name, 0.452 * weight)
# gravity ~ 9.81 m/s^2
print "This is around %d newtons of force on Earth." % (9.81 * 0.452 * weight)
