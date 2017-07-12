# 100 cars
cars = 100
# 4 seats per car
space_in_a_car = 4
# 30 drivers
drivers = 30
# 90 passengers
passengers = 90
# cars in excess of number of drivers are cars not driven
cars_not_driven = cars - drivers
# as many cars will be driven as there are drivers
cars_driven = drivers
# total carpool capacity is space per car multiplied by cars driven
carpool_capacity = cars_driven * space_in_a_car
# finding the average
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
