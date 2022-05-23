# Chapter 003 NOTES   

print("\n\n\n\n")

motorcycles = ['honda', 'yamaha', 'harley', 'suzuki']
print(motorcycles)
print(*motorcycles, sep=", ")

print("\n")

# Paul 09.05.2022 - method append() will add element at the end of the list
# without modifying it.

motorcycles.append('ducati')
print(motorcycles)
print(*motorcycles, sep=", ")
# Paul 09.05.2022 - Very useful, but won't let me add period
# at the end of the print.

print("\n")

# Paul 09.05.2022 - it will add element, and let it print you
# with another number in []
message_moto = f"{motorcycles[0]}, {motorcycles[1]}, {motorcycles[2]}, " \
               f"{motorcycles[3]}."
# Paul 09.05.2022 - this will let me add period.
print(message_moto)

# Paul 09.05.22 using empty list add another elements with append() method
print("\n\n\n\n")
games_list = []

games_list.append('Doom')
games_list.append('Warcraft II')  # hours of my childhood
games_list.append('Duke Nukem')
games_list.append('TekWar')
games_list.append('Worms')
games_list.append('Quake')
games_list.append('Super Mario Bros')
games_list.append('Another World')  # priceless game
games_list.append('Quake 2')
games_list.append('Aliens vs Predator')
games_list.append('Half-Life')  # :'-)
games_list.append('Fallout 2')  # MORE hours of my childhood
games_list.append('Heroes of Might and Magic III')
# and even MORE h, beautiful soundtrack!
games_list.append('Half-Life 2')
games_list.append('Jedi Knight')
games_list.append('Rune')  # I had clan for this one :D
games_list.append('Warcraft III')
games_list.append('Fallout: New Vegas')
games_list.append('Alien: Isolation')
games_list.append('The Last of Us Part II')

games_list.insert(-1, 'God of War IV')
games_list.insert(1, 'The Last of Us')
# Paul 09.05.2022 .insert() method. Must give it [1] index,
# because I pop first one played later. I don't know if you know,
# but this is the best game that was ever created :D

print(games_list)

print("\n")

print(*games_list, sep=", ")

print("\n")

last_one = games_list.pop()
# Paul 09.05.2022 The pop() method used to get access to the
# last value in the list.
first_one = games_list.pop(0)  # Paul 09.05.2022 ...aaand first one for example!

print(*games_list, sep=", ")
# Paul 09.05.2022 - and now I can't print first and last item, because of pop()

print("\n")

print(f"\n\tThe last game I bought is {last_one}.")
print(f"\n\tOne of the first games I played on 486 computer is {first_one}.") 
# Paul 09.05.2022 'Doom' value is still open for use

# Paul 09.05.2022 - by 'del' command you can erase any element from the list,
# if you know it's index, remember that using 'del' you no longer
# have access to a removed value!

print("\n\n\n\n")

motorcycles2 = ['honda', 'yamaha', 'harley', 'suzuki']

del motorcycles2[0]
print(*motorcycles2, sep=", ")
del motorcycles2[2]
print(*motorcycles2, sep=", ")
del motorcycles2[1]
print(*motorcycles2, sep=", ")

# Paul 09.05.22 another command you can use is pop() method, that allows you
# work with removed item. "You can POP the last item from a pile".
# You can use pop() to indicate any item from the list,
# but REMEMBER YOU WILL NOT HAVE FURTHER ACCESS TO IT IN THE LIST!'''

print("\n")

motorcycles3 = ['honda', 'yamaha', 'harley', 'suzuki', 'motorynka']
popped_motorcycle = motorcycles3.pop()

print(*motorcycles3, sep=", ")
print(popped_motorcycle)

''' Paul 09.05.2022 - and now for something completely different - 
a remove() method, that search items according their value.
Loop if value is more than once.'''

print("\n")

best_movies = ['terminator 2', 'predator', 'lord of rings trilogy', 'twilight']
print(*best_movies, sep=", ")

shitty_one = 'twilight'  # we assigned variable to a 'twilight' (no)value
best_movies.remove(shitty_one)
# then tell Python to remove that value from the list
print(*best_movies, sep=", ")

print("\n")

shitty_one_msg = f"I removed {shitty_one.title()}, because it's shit, " \
                 f"and can't be put inside best movies."
# and use it to tell WHY we got rid of that one
print(shitty_one_msg)
