# Exercise 004-12 - More loops (tired of foods, so going to anything else instead):

items = []
items.append('item00')
items.append('item01')
items.append('item02')
items.append('item03')
items.append('item04')
items.append('item05')
items.append('item06')
items.append('item07')
items.append('item08')
items.append('item09')

print ("All items in items list, the 'for' loop:")
for item in items:
	print (item)

print ('\nAll items in .title():')
for item in items:
	print (item.title())


movies = [ 'terminator 1', 'termiantor 2', 'predator', 'leon', 'taxi driver', 'godfather', 'the matrix', 'gladiator', 'lord of the rings', 'shrek', 'green mile', 'the silence of the lambs', 'fight club (you dont talk about it)', 'pulp fiction', 'cast away', 'american beauty', 'gran torino', 'i am legend', 'the walking dead series', 'interstellar', 'goonies', 'the departed', 'goodfellas', 'untouchables', 'million dollar baby', 'scarface', 'the shawshank redemption', 'saving private ryan', 'fury', 'braveheart', 'apocalypse now', 'the good, the bad and the ugly', 'the snatch', 'man in black', 'shichinin no samurai', 'alien', 'aliens', 'black hawk down', 'blow', 'unforgiven', 'raiders of the lost ark', 'dances with wolves', '2001: a space odyssey', 'dune', 'john wick', 'the blues brothers' ]
print ("\nNice movies:")
for movie in movies:
	print (movie.title())

print ("\nA bit of slice:")
for movie in movies[:10]:
	print (movie.title())