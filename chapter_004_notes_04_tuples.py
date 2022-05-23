# Chapter 004 NOTES tuples 

dimensions = (200, 50)  # Paul 12.05.2022 for tuple use (), and really a coma...
print('\n\nA tuple:')
print(dimensions[0])
print(dimensions[1])

mt = (3,)  # one element in tuple

# Paul 12.05.2022 looping through tuple
print('\nOriginal dimensions:')
for dimension in dimensions:
    print(dimension)

# Paul 12.05.2022 redefine entire tuple

dimensions = (400, 100)  # redefined tuple
print(f'\nNew dimensions printed as list: {dimensions}.')

print('\nNew dimensions loop:')
for dimension in dimensions:
    # and loop it (kto cholera wymyślił słowo "iteracja"?!)
    print(dimension)

# Paul 13.05.2022 - about time to make length line 80 characters in my editor.
# Paul 13.05.2022 - check for tab = 4 spaces
