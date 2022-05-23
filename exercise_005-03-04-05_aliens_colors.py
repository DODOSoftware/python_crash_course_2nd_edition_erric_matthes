# Exercise 005-03 Aliens colors #1:
alien_color = 'green'

if alien_color == 'green':
    print("You've killed alien grunt and earned 5 points!")
if alien_color == 'yellow':
    print("You've killed alien master and earned 10 points!")

# Exercise 005-04 Aliens colors #2:
if alien_color == 'yellow':
    print("You've killed alien grunt and earned 5 points!")
else:
    print("You've killed alien master and earned 10 points!")

# Exercise 005-05 Aliens colors #3:
alien_color = 'red'

if alien_color == 'green':
    print("You've earned 5 points!")
elif alien_color == 'yellow':
    print("You've earned 10 points!")
elif alien_color == 'red':
    print("You've killed alien leader and earned 15 points!")
# Paul 15.05.2022 used "elif" instead of "else".

# There are at least two ways to do it:
# - first is standard and simple "if",
# - second is with "if-elif".
