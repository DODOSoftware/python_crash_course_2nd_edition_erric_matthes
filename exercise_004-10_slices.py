
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Paul 11.05.2022 - slicing the list of movies. The output retain the structure of the list and includes [ pointed ] items.

movies = [ 'terminator 1', 'termiantor 2', 'predator', 'leon', 'taxi driver', 'godfather', 'the matrix', 'gladiator', 'lord of the rings', 'shrek', 'green mile', 'the silence of the lambs', 'fight club (you dont talk about it)', 'pulp fiction', 'cast away', 'american beauty', 'gran torino', 'i am legend', 'the walking dead series', 'interstellar', 'goonies', 'the departed', 'goodfellas', 'untouchables', 'million dollar baby', 'scarface', 'the shawshank redemption', 'saving private ryan', 'fury', 'braveheart', 'apocalypse now', 'the good, the bad and the ugly', 'the snatch', 'man in black', 'shichinin no samurai', 'alien', 'aliens', 'black hawk down', 'blow', 'unforgiven', 'raiders of the lost ark', 'dances with wolves', '2001: a space odyssey', 'dune', 'john wick' ]

print ( f'\n{ movies[ 0:3 ] }' )

print ( f'\n{ movies[ 3:6 ] }' )

print ( f'\n{ movies[ 6:len(movies) ] }' ) # Paul 11.05.2022 - adding len() to print from 6 to the rest of the list, but [ 6: ] would be easier...

print ( f'\n{ movies[ 6: ] }' ) # Paul 11.05.2022 - like this

print ( f'\n{ movies[ :4 ] }' )

print ( f'\n{ movies[ 0: :2 ] }') # Paul 11.05.2022 - third digit shows Python how many items it should skip between items in specified range.

print ( f'\n{ movies[ -3: ] }')

print ( f'\n{ movies[ :-3 ] }')

print ( f'\nThe list contains { len( movies ) } movies.' )



print ( '\n\nLooping through slices:' )

print ( '\nHere are first four of the movies:' )
for movie in movies[ :4 ]:
	print ( movie.title() )