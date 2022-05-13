# Exercise 004-01 Pizzas:

pizzas = [ 'neapolitanian', 'chicago', 'sicilian', 'greek' ]
for pizza in pizzas:
	print(f'I like a {pizza.title()} a lot.')

print('in fact I like many kinds of pizza, but anchois...\n')
print('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n')
print(f'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n')
print('End of pizza loop - no more pizza for you.\n')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Paul 10.05.2022 - looping for for looping

print('\nLOOP "FOR" GUEST "IN" GUESTS:')

guests = ['albert einstein', 'elon musk', 'marek jurek', 'socrates', 'adam zborowski']
for guest in guests:
	print(guest)

print('\nLIST OF MY MINI-BUNNIES (only two):')

rabbits = ['rapek', 'kofi']
for rabbit in rabbits:
	print(rabbit)

print ( '\nLIST OF DOGS I WOULD LIKE TO HAVE:')
''' I would love to have two belgian malinois oraz dutch shepherd dogs,
but I'm affraid that I will not have time for such demanding canine.'''

dogs = ['belgian malinois', 'dutch shepherd dog', 'german shepherd', 'swiss shepherd', 'french shepherd dog bauceron', 'american pit bull terier']

for dog in dogs:
	print(dog)
	''' print(dog[0]) - Paul 10.05.2022 that was kinda funny when indexed letter
	from items was between them XD'''


print('\nGAMES LIST:')
'''Paul 10.05.2022 - let's try to combine list first
(yeah yeah, I've ctrl+c and ctrl+v it obviously XD)'''

games_list = []

games_list.append('Doom')
games_list.append('Warcraft II')
games_list.append('Duke Nukem')
games_list.append('TekWar')
games_list.append('Worms')
games_list.append('Quake')
games_list.append('Super Mario Bros')
games_list.append('Another World')
games_list.append('Quake 2')
games_list.append('Aliens vs Predator')
games_list.append('Half-Life')
games_list.append('Fallout 2')
games_list.append('Heores of Might and Magic III')
games_list.append('Half-Life 2')
games_list.append('Jedi Knight')
games_list.append('Rune')
games_list.append('Warcraft III')
games_list.append('Fallout: New Vegas')
games_list.append('Alien: Isolation')
games_list.append('The Last of Us Part II')
games_list.insert(len( games_list ), 'God of War IV')
# Paul 10.05.2022 -1 won't insert at the end, need to use len() function.
games_list.insert(1, 'The Last of Us')
games_list.remove('Duke Nukem')
# Paul 11.05.2022 - not really that fav, I couldn't .pop() that one out, dunno why.

for game in games_list:
	print(game.title())
	''' Paul 10.05.2022 - nice little .title() you have there....
	Would be shame if it won't work proper on roman letters...'''

print('\n---\n')

for game in games_list:
	print(f'One of games I used to play a lot: {game.title() }!') 
	# Paul 11.05.2022 - again .title, I'll figure it out later I guessss.
	print(f'Gimmie more time to play a lot the {game.title() }!')
	print(f'Gibberish gibberish gibberish a lot {game.title() }!')
	print(f'One of games I like a lot to play: {game.title() }!\n') 
	# Paul 11.05.2022 - ok I get the idea

print('I used to play a lot, thank you - especially older games - for many memories.')
'''Paul 11.05.2022 - cutting for next task after the loop, e.g. giving
Play Now button displayed or some sort of summarize.'''


''' TNTENDET INDENTEN ERRORS BEYON THIS LINE:

guests = [ 'albert einstein', 'elon musk', 'marek jurek', 'socrates', 'adam zborowski' ]
# Paul 11.05.2022 - IndentationError: expected an indented block after 'for' statement on line __
for guest in guests:
print ( guest )

for game in games_list: # Paul 11.05.2022 - logical error, beacuse the final value is god of war, only this game will get printed.
	print ( f'One of games I used to play a lot: { game.title() }!' )
print ( f'Gimmie more time to play a lot the { game.title() }!' )
print ( f'Gibberish gibberish gibberish a lot { game.title() }!' )
print ( f'One of games I like a lot to play: { game.title() }!\n' )

message = '\nHello World!\n\n' # Paul 11.05.2022 - IndentationError: unexpected indent
	print ( message )

for game in games_list: # Paul 11.05.2022 - logical error, beacuse the print is indented, the loop will contain it.
	print ( f'One of games I used to play a lot: { game.title() }!' )
	print ( f'Gimmie more time to play a lot the { game.title() }!' )
	print ( f'Gibberish gibberish gibberish a lot { game.title() }!' )

	print ( f'One of games I like a lot to play:!\n' )

	'''