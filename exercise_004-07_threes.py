# Exercise 004-07 Make a list of the multiples of 3 from 3 to 30:

print('List comprehensions:')
threes = [value ** 3 for value in range(3, 31)]
print(threes)

for three in threes:
	print(three)

print('\n\nList with temporarily value:')
threes = []
for value in range(3, 31):
	three = value ** 3
	threes.append(three)
print(threes)

for three in threes:
	print(three)

print('\n\nList without temporarily value:')
threes = []
for value in range(3, 31):
	threes.append(value ** 3)
print(threes)

for three in threes:
	print(three)
