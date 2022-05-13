# Exercise 004-03 Counting to Twenty

for value in range(1, 21):
	print(value)

print('\n\n\n')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

for value in range(1, 5):
	print(value)
print('\n')

for value in range(0):
	print(f'Here should be "value", but range( 0 ), so we have: {value}.')
	'''Paul 11.05.2022 - no ducks given for the range is still (0),
	so it would not print it, giving only whitespace, right? :D'''
print('\n')

for value in range(1):
	print(value)
print ('\n')

for value in range(9):
	print(value)
print('\n')

for integer in range(2):
	print (integer)
print ('\n')

for value in range(9, 35):
	print(value)


print('\n\nUse range() nad list() function to create list of numbers:')

numbers = list(range(1, 6))
print (numbers) # Paul 11.05.2022 - neat


print('\n\nEVEN and ODD numbers between 1 nad 10:')

even_numbers = list(range(2, 11, 2))
'''Paul 11.05.2022 - range() function start with 2, reapetadly adds 2
(last one stated), until it reaches or passes 11 (second value).'''
print(even_numbers)

odd_numbers = list(range(1, 10, 2))
print(odd_numbers)


print('\n\nFirst 10 squares on the list - second attempt:')

''' Paul 11.05.2022 - I wrote it damn wrong - the value in .append() method
should be 'square' not 'value' and it's obvious, but got innapropriate indent
in print() call!

squares = []
for value in range( 1, 10 ):
	square = value ** 2
	squares.append( value )
	print ( squares )

The output was:

[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

So that was interesting, but got nowhere near what I wanted.
Learned to build one side of the pyramid tho. Or stairs, you name it XD '''


print('\nWith temporarily value "square":')
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)


print('\n\nMORE CONSICELY - WITHOUT TEMP VALUE "SQUARE":')
squares = []
for value in range(1, 11):
# Paul 11.05.2022 - watch for last int in the range(), it must be 1 number bigger
	squares.append(value ** 2)
print(squares)


print('\n\nAnd now for that mistake with indent in print() call inside the loop:')
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
	print(squares)


print('\n\nMinimum, maximum and sum of a list of numbers:')

digits = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
minimal = f'The minimal digit on the list is: {min(digits)}.'
print(minimal)

maximum = f'The maximal digit on the list is: {max(digits)}.'
print(maximum)

summary = f'The sum of all digits on the list equals {sum(digits)}.'
print(summary)


print('\n\nList comprehensions:')

squares = [ value ** 2 for value in range( 1, 11 ) ]
print(*squares, sep = ", ")

other_comprehensions = [value + 4 for value in range(6, 247)]
print(f'\n{other_comprehensions}')

other_comprehensions2 = [digit * 2 for digit in range(2, 87)]
print ( f'\n{ other_comprehensions2 }' )

other_comprehensions3 = [number - 5 for number in range(-200, 14)]
print ( f'\n{ other_comprehensions3 }' )

other_comprehensions4 = [number / 2 for number in range(2, 34, 2)]
'''Paul 11.05.2022 - make even numbers 2 through 35 divided by 2,
but something is wrong with halfs in odd numbers tho.'''
print(f'\n{other_comprehensions4 }')