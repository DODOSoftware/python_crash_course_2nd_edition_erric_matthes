# Exercise 004-08-09 Cubes from 1-10 and list comprehension

print ( 'With temporarily value "cube":')
cubes = []
for value in range( 1, 11 ):
	cube = value ** 3
	cubes.append( cube )
print ( cubes )

print ( '\nWithout temp value "cube":' )
cubes = []
for value in range( 1, 11 ):
	cubes.append( value ** 3 )
print ( cubes )

print ( '\nList comprehension:' )
cubes = [ value ** 3 for value in range( 1, 11 ) ]
print ( cubes )