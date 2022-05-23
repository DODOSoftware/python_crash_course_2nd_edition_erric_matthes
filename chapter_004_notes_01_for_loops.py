# Chapter 004 NOTE for looping

# Paul 10.05.2022 - looping for 'for' looping

print('\nLOOP "FOR" GUEST "IN" GUESTS:')

guests = ['albert einstein', 'elon musk', 'marek jurek', 'socrates',
          'adam zborowski']
for guest in guests:
    print(guest)

print('\nLIST OF MY MINI-BUNNIES (only two):')

rabbits = ['rapek', 'kofi']
for rabbit in rabbits:
    print(rabbit)

print('\nLIST OF DOGS I WOULD LIKE TO HAVE:')
# I would love to have two belgian malinois and dutch shepherd dogs,
# but I'm afraid that I will not have time for such demanding canine.

dogs = ['belgian malinois', 'dutch shepherd dog', 'german shepherd',
        'swiss shepherd', 'french shepherd dog bauceron',
        'american pit bull terier']

for dog in dogs:
    print(dog)
    # print(dog[0]) - Paul 10.05.2022 that was kinda funny when indexed letter
    # from items was between them XD


print('\nGAMES LIST:')
# Paul 10.05.2022 - let's try to combine list first
# (yeah yeah, I've ctrl+c and ctrl+v it obviously XD)

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
games_list.insert(len(games_list), 'God of War IV')
# Paul 10.05.2022 -1 won't insert at the end, need to use len() function.
games_list.insert(1, 'The Last of Us')
games_list.remove('Duke Nukem')
# Paul 11.05.2022 - not really that fav,
# I couldn't .pop() that one out, dunno why.

for game in games_list:
    print(game.title())
    # Paul 10.05.2022 - nice little .title() you have there....
    # Would be shame if it won't work proper on roman letters...

print('\n---\n')

for game in games_list:
    print(f'One of games I used to play a lot: {game.title() }!') 
    # Paul 11.05.2022 - again .title, I'll figure it out later I guessss.
    print(f'Gimmie more time to play a lot the {game.title() }!')
    print(f'Gibberish gibberish gibberish a lot {game.title() }!')
    print(f'One of games I like a lot to play: {game.title() }!\n') 
    # Paul 11.05.2022 - ok I get the idea

print('I used to play a lot, thank you - especially older games - '
      'for memories.')
# Paul 11.05.2022 - cutting for next task after the loop, e.g. giving
# Play Now button displayed or some sort of summarize.


''' INTENDED INDENTED ERRORS BEYOND THIS LINE:

# Paul 11.05.2022 - IndentationError: expected an indented block after 'for'
# statement on line:
guests = ['albert einstein', 'elon musk', 'marek jurek', 'socrates', 
'adam zborowski']
for guest in guests:
print(guest)

# Paul 11.05.2022 - logical error, because the final value is god of war,
# only this game will get printed:
for game in games_list:
    print(f'One of games I used to play a lot: {game.title()}!')
print(f'Gimmie more time to play a lot the {game.title()}!')
print(f'Gibberish gibberish gibberish a lot {game.title()}!')
print(f'One of games I like a lot to play: {game.title()}!\n')

# Paul 11.05.2022 - IndentationError: unexpected indent:
message = '\nHello World!\n\n'
    print(message)

# Paul 11.05.2022 - logical error, because the print is indented,
# the loop will contain it:
for game in games_list:
    print(f'One of games I used to play a lot: {game.title()}!')
    print(f'Gimmie more time to play a lot the {game.title()}!')
    print(f'Gibberish gibberish gibberish a lot {game.title()}!')

    print(f'One of games I like a lot to play:!\n')
    
ERRORS ABOVE'''