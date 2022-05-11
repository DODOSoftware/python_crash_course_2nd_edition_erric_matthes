# Exercise 004-03 Counting to Twenty

for value in range( 1, 21):
	print ( value )

print ( '\n\n\n' )


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

for value in range( 1, 5 ):
	print ( value )
print ( '\n' )

for value in range( 0 ):
	print ( f'Here should be "value", but range( 0 ), so we have: { value }.' )
	# Paul 11.05.2022 - no fucks given for the range is still ( 0 ), so it would not print it, giving only whitespace, right? :D
print ( '\n' )

for value in range( 1 ):
	print ( value )
print ( '\n' )

for value in range( 9 ):
	print ( value )
print ( '\n' )

for integer in range( 2 ):
	print ( integer )
print ( '\n' )

for value in range( 9, 35 ):
	print ( value )



print ( '\n\nUse range() nad list() function to create list of numbers:' )

numbers = list ( range( 1, 6) )
print ( numbers ) # Paul 11.05.2022 - neat



print ( '\n\nEVEN and ODD numbers between 1 nad 10:' )

even_numbers = list ( range( 2, 11, 2 ) ) # Paul 11.05.2022 - range() function start with 2, reapetadly adds 2 (last one stated), until it reaches or passes 11 (second value).
print ( even_numbers )

odd_numbers = list ( range(1, 10, 2) )
print ( odd_numbers )



print ( '\n\nFirst 10 squares on the list - second attempt:' )

''' Paul 11.05.2022 - I wrote it damn wrong - the value in .append() method should be 'square' not 'value' and it's obvious, but got innapropriate indent in print() call!

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

So that was interesting, but got nowhere near what I wanted. LEarned to build one side of the pyramid tho XD '''

print ( '\nWith temporarily value "square":')
squares = []
for value in range( 1, 11 ):
	square = value ** 2
	squares.append( square )
print ( squares )


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # WE LIKE CONSICE CODE RIGHT? # # # # # # # # # # # # # # # # # # # # # #


print ( '\n\n\nMORE CONSICELY - WITHOUT TEMP VALUE "SQUARE":' )
squares = []
for value in range( 1, 11 ):    # Paul 11.05.2022 - watch for last int in the range(), it must be 1 number bigger
	squares.append( value ** 2 )
print ( squares )


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print ( '\n\n\nAnd now for that mistake with indent in print() call inside the loop:' )
squares = []
for value in range( 1, 11 ):
	square = value ** 2
	squares.append( square )
	print ( squares )