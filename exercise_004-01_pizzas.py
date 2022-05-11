

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Paul 10.05.2022 - looping for for looping

print ( '\nLOOP "FOR" GUEST "IN" GUESTS:' )

guests = [ 'albert einstein', 'elon musk', 'marek jurek', 'socrates', 'adam zborowski' ]
for guest in guests:
	print ( guest )

print ( '\nLIST OF MY MINI-BUNNIES (only two):' )

rabbits = [ 'rapek', 'kofi' ]
for rabbit in rabbits:
	print ( rabbit )

print ( '\nLIST OF DOGS I WOULD LIKE TO HAVE:') # I would love to have two belgian malinois oraz dutch shepherd dogs, but I'm affraid that I will not have time for such demanding canine.

dogs = [ 'belgian malinois', 'dutch shepherd dog', 'german shepherd', 'swiss shepherd', 'french shepherd dog bauceron', 'american pit bull terier' ]

for dog in dogs:
	print ( dog )
  # print ( dog[0] ) - Paul 10.05.2022 that was kinda funny when indexed letter from items was between them XD


print ( '\nGAMES LIST:') # Paul 10.05.2022 - let's try to combine list first (yeah yeah, I've ctrl+c and ctrl+v it obviously XD )

games_list = []

games_list.append( 'Doom' )
games_list.append( 'Warcraft II' )
games_list.append( 'Duke Nukem' )
games_list.append( 'TekWar' )
games_list.append( 'Worms' )
games_list.append( 'Quake' )
games_list.append( 'Super Mario Bros' )
games_list.append( 'Another World' )
games_list.append( 'Quake 2' )
games_list.append( 'Aliens vs Predator' )
games_list.append( 'Half-Life' )
games_list.append( 'Fallout 2' )
games_list.append( 'Heores of Might and Magic III' )
games_list.append( 'Half-Life 2' )
games_list.append( 'Jedi Knight' )
games_list.append( 'Rune' )
games_list.append( 'Warcraft III' )
games_list.append( 'Fallout: New Vegas' )
games_list.append( 'Alien: Isolation' )
games_list.append( 'The Last of Us Part II' )
games_list.insert( len( games_list ), 'God of War IV' ) # Paul 10.05.2022 -1 won't insert at the end, need to use len() function.
games_list.insert( 1, 'The Last of Us' )

for game in games_list:
	print ( game.title() ) # Paul 10.05.2022 - nice little .title() you have there. Would be shame if it won't work proper on roman letters...

