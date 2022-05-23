# Chapter 006 NOTES - Dictionaries

'''Dictionary is a collection of key-value pairs. Each key is connected to the
value, and you use keys to access their values. Key's value can be everything,
a number, a string, a list or other dictionary. You can use any object created
in Python as a value in the dictionary. And you can use as many key-value
pairs as you want.
Dictionaries are dynamic structures.'''

print("New alien-dictionary:")
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

'''alien_1 = {'color': 'yellow', 'points': 10}

print(alien_1['color'])
print(alien_1['points'])

alien_2 = {'color': 'red', 'points': 15}

print(alien_2['color'])
print(alien_2['points'])'''

print("\nAdding new variable with value from the dictionary:")
new_points = alien_0['points']
print(f"You've earned {new_points} points!")

# Paul 21.05.2022 if you run this code every time the alien got shot down,
# the alien's point value will be retrieved.
# in other words - run code everytime you need retrieve a value from
# the dictionary.

# Paul 21.05.2022 inverting key-value:

print("\nInverting key with value:")
my_map = {'a': 0, 'b': 1, 'c': 2}
inv_map = {v: k for k, v in my_map.items()}

print(inv_map[0])
print(my_map['a'])

# Paul 21.05.2022 if values are unique
dict((v, k) for k, v in my_map.items())

# I begin being tired of drag'n'drop to the gitHub, I sense learning git
# commands in the near future...

print("\nAdding new key-value pairs to the dictionary:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# It's sometimes convenient or necessary to start with a dictionary:
print("\nStarting with an empty dictionary:")
alien_0 = {}
# adding elements:
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
