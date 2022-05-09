motorcycles = [ 'honda', 'yamaha', 'harley' ]
print ( motorcycles )
print ( *motorcycles, sep=", ")

motorcycles.append( 'ducati' ) # Paul 09.05.2022 - method append() will add element at the end of the list, without modyfing it.
print ( motorcycles )
print ( *motorcycles, sep=", ") # PAul 09.05.2022 - Very useful, but won't let me add period at the end of the print.

# Paul 09.05.2022 - it will add element, and let it print you with another number in []
message_moto = f"{ motorcycles[0] }, { motorcycles[1] }, { motorcycles[2] }, { motorcycles[3] }." # Paul 09.05.2022 - will let me add period.
print ( message_moto )

# using empty list add another elements with append() method

games_list = []
games_list.append( 'Doom' )
games_list.append( 'Warcraft II' )
games_list.append( 'TekWar' )
games_list.append( 'Worms' )
games_list.append( 'Quake' )
games_list.append( 'Super Mario Bros' )
games_list.append( 'Another World' )
games_list.append( 'Half-Life' )
games_list.append( 'Fallout 2' )
games_list.append( 'Heores of Might and Magic III' )
games_list.append( 'Half-Life 2' )
games_list.append( 'Jedi Knight' )
games_list.append( 'Rune' )
games_list.append( 'Quake 2' )
games_list.append( 'Aliens vs Predator' )
games_list.append( 'Fallout: New Vegas' )
games_list.append( 'The Last of Us' )
games_list.append( 'Alien: Isolation' )
games_list.append( 'God of War IV' )
print ( games_list )

print ( *games_list, sep=", " ) # Paul 09.05.2022 - printing whole list without square brackets!