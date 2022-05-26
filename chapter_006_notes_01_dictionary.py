# Chapter 006 NOTES - Dictionaries

# Dictionary is a collection of key-value pairs. Each key is connected to the
# value, and you use keys to access their values. Key's value can be everything,
# a number, a string, a list or other dictionary. You can use any object created
# in Python as a value in the dictionary. And you can use as many key-value
# pairs as you want.
# Dictionaries are dynamic structures.

print("New alien-dictionary:")
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

'''Other aliens:

alien_1 = {'color': 'yellow', 'points': 10}

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

# Paul 21.05.2022 inverting key-value (thank you Stackoverflow):

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

# It's sometimes convenient or necessary to start with an empty dictionary,
# typically with user-supplied data or with large dictionaries, with key-value
# pairs generated automatically.

print("\nStarting with an empty dictionary:")
alien_0 = {}
# adding elements:
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying values in a dictionary:
print("\nChanging values. Alien color is now:")
alien_0['color'] = 'not green at all!'

print(alien_0['color'])

# Storing speed value and determining how far alien should move (to the right):

print("\nSpeed and length:")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Alien original x_position: {alien_0['x_position']}.")

# Moving alien and determining how far it will go, based on his speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# New alien position = old position + increment:
# NOTE: Thanks to this method we can change alien behavior, by changing only one
# value in the dictionary.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x_position: {alien_0['x_position']}.")

# Note that del of key-value pair is permanent!
print("\ndel of key-value pair:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Storing one king of information about many objects in one dictionary.

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    # Good practice - put comma after last key-value pair also, for it shows
    # that you're ready to add another key-value pair!
}

language = favorite_language['sarah'].title()
# Creating new variable looks much cleaner.
print(f"\nSarah's favorite language is {language}.")
