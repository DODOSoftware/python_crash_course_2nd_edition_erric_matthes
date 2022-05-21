''' Chapter 006 NOTES - Dictionaries

Dictionairy is a collection of key-value pairs. Each key is connected to the
value, and you use keys to access their values. Key's value can be everything,
a number, a string, a list or other dictionairy. You can use any object created
in Python as a value in the dictionairy. And you can use as many key-value 
pairs as you want.

Dictionaries are dynamic structures.'''

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

'''alien_1 = {'color': 'yellow', 'points': 10}

print(alien_1['color'])
print(alien_1['points'])

alien_2 = {'color': 'red', 'points': 15}

print(alien_2['color'])
print(alien_2['points'])'''

new_points = alien_0['points']
print(f"You've earned {new_points} points!")