# Exercise 3-4 Geust List


guest_list = [ 'albert einstein', 'nikola tesla', 'thomas aquinas', 'platon', 'socrates', 'leonardo da vinci', 'isaac newton']

invitation0 = f"Hereby I invite you Sir {guest_list[0].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation1 = f"Hereby I invite you Sir {guest_list[1].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation2 = f"Hereby I invite you Sir {guest_list[2].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation3 = f"Hereby I invite you Sir {guest_list[3].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation4 = f"Hereby I invite you Sir {guest_list[4].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation5 = f"Hereby I invite you Sir {guest_list[5].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation6 = f"Hereby I invite you Sir {guest_list[6].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!\n"

print(invitation0)
print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)
print(invitation5)
print(invitation6)

guest_number = f"Total guests number: {len(guest_list)}."
print(guest_number)


# Exercise 3-5 Changing Guest List


pop_newton = guest_list.pop()
msg_newton = f"\nSir {pop_newton.title()} politely must decline, for he's not done with physics laws yet.\n"
print(msg_newton)

guest_list.append('aristotle')
msg_aristotle = f"But Sir {guest_list[6].title()} will gladly take the invitation!\n\n"
print (msg_aristotle)

invitation6 = f"Hereby I invite you Sir {guest_list[6].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!\n"
print(invitation0)
print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)
print(invitation5)
print(invitation6)

guest_number = f"Total guests number: {len(guest_list)}."
print(guest_number)


# Exercise 3-6 More Guests


bigger_table_msg = "\n\nHey folks, I've found and ordered a bigger table, so we will have room for three more!\n\n"
print(bigger_table_msg)
guest_list.insert(0, "stephen hawking")
guest_list.insert(3, "alfred nobel")
guest_list.insert(len(guest_list), "max planck")
''' Paul 09.05.2022 - 'len(list_name)' command allows you to .insert()
in the last position on the list.'''

invitation0 = f"Hereby I invite you Sir {guest_list[0].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation1 = f"Hereby I invite you Sir {guest_list[1].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation2 = f"Hereby I invite you Sir {guest_list[2].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation3 = f"Hereby I invite you Sir {guest_list[3].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation4 = f"Hereby I invite you Sir {guest_list[4].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation5 = f"Hereby I invite you Sir {guest_list[5].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation6 = f"Hereby I invite you Sir {guest_list[6].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation7 = f"Hereby I invite you Sir {guest_list[7].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation8 = f"Hereby I invite you Sir {guest_list[8].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation9 = f"Hereby I invite you Sir {guest_list[9].title()} to a wild Birthday Party, on my birthday 24.01 at Costa Rica beach!\n"

print(invitation0)
print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)
print(invitation5)
print(invitation6)
print(invitation7)
print(invitation8)
print(invitation9)

guest_number = f"Total guests number: {len(guest_list)}."
print(guest_number)


# Exercise 3-7 Shrinking List


sorry = "\nDear Guests, I'm sincerely in deep sorrow, but I must refuse, because book of Python tell me to do it, and invite only two of you. Now I will pop out almost all of you, but do not despair. Please keep in mind that I will try organize our party in full soon. We will be in touch, and then everybody will be invited!\n"
print(sorry)

guest_list.pop() # Paul 09.05.2022 - YEAH, POP'EM ALL!
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()

message = f"Please keep in mind, Dear { guest_list[0].title() } and { guest_list[1].title() }, that you are still invited!"
print(message)

del guest_list[1], guest_list[0]

print (f"Is any one on the {guest_list}??? No....")
# Paul 09.05.2022 - empty list funny square brackets at last :)

guest_number = f"Total guests number: {len(guest_list)}."
print(guest_number)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  

print("\n\n\n\n")

motorcycles = ['honda', 'yamaha', 'harley', 'suzuki']
print(motorcycles)
print(*motorcycles, sep = ", ")

print("\n")

''' Paul 09.05.2022 - method append() will add element at the end of the list
without modyfing it.'''

motorcycles.append('ducati')
print(motorcycles)
print(*motorcycles, sep = ", ")
# Paul 09.05.2022 - Very useful, but won't let me add period at the end of the print.

print("\n")

# Paul 09.05.2022 - it will add element, and let it print you with another number in []
message_moto = f"{motorcycles[0]}, {motorcycles[1]}, {motorcycles[2]}, {motorcycles[3]}."
# Paul 09.05.2022 - this will let me add period.
print(message_moto)

# Paul 09.05.22 using empty list add another elements with append() method

print ("\n\n\n\n")
games_list = []

games_list.append('Doom')
games_list.append('Warcraft II') # hours of my childhood
games_list.append('Duke Nukem')
games_list.append('TekWar')
games_list.append('Worms')
games_list.append('Quake')
games_list.append('Super Mario Bros')
games_list.append('Another World') # priceless game
games_list.append('Quake 2')
games_list.append('Aliens vs Predator')
games_list.append('Half-Life') # :'-)
games_list.append('Fallout 2') # MORE hours of my childhood
games_list.append('Heores of Might and Magic III')  # and even MORE h, beautiful soundtrack!
games_list.append('Half-Life 2')
games_list.append('Jedi Knight')
games_list.append('Rune') # I had clan for this one :D
games_list.append('Warcraft III')
games_list.append('Fallout: New Vegas')
games_list.append('Alien: Isolation')
games_list.append('The Last of Us Part II')

games_list.insert(-1, 'God of War IV')
games_list.insert(1, 'The Last of Us')
''' Paul 09.05.2022 .insert() method. Must give it [1] index,
bacause I pop first one played later. I don't know if you know,
but this is the best game that was ever created :D '''

print(games_list)

print("\n")

print(*games_list, sep = ", ")

print("\n")

last_one = games_list.pop() # Paul 09.05.2022 The pop() method used to get access to the last value in the list.
first_one = games_list.pop(0) # Paul 09.05.2022 ...aaand first one for example!

print (*games_list, sep = ", ") # Paul 09.05.2022 - and now I can't print first and last item, beacue of pop()

print ("\n")

print(f"\n\tThe last game I bought is {last_one}.")
print(f"\n\tOne of the first games I played on 486 computer is {first_one}.") 
# Paul 09.05.2022 'Doom' value is still open for use

'''Paul 09.05.2022 - by 'del' command you can erase any element from the list,
if you know it's index, rembember that using 'del' you no longer
have access to a removed value!'''

print ("\n\n\n\n")

motorcycles2 = ['honda', 'yamaha', 'harley', 'suzuki']

del motorcycles2[0]
print(*motorcycles2, sep = ", ")
del motorcycles2[2]
print(*motorcycles2, sep = ", ")
del motorcycles2[1]
print(*motorcycles2, sep = ", ")

''' Paul 09.05.22 another command you can use is pop() method, that allows you
work with removed item. "You can POP the last item from a pile".
You can use pop() to indicate any item from the list,
but REMEMBER YOU WILL NOT HAVE FURTHER ACCESS TO IT IN THE LIST!'''

print ("\n")

motorcycles3 = ['honda', 'yamaha', 'harley', 'suzuki', 'motorynka']
poped_motorcycle = motorcycles3.pop()

print(*motorcycles3, sep = ", ")
print(poped_motorcycle)

''' Paul 09.05.2022 - and now for something completely different - 
a remove() method, that search items according their value.
Loop if value is more than once.'''

print("\n")

best_movies = ['terminator 2', 'predator', 'lord of rings trilogy', 'twilight']
print (*best_movies, sep= ", ")

shitty_one = 'twilight' # we assigne variable to a 'twilight' (no)value
best_movies.remove( shitty_one ) # then tell Python to remove that value from the list
print(*best_movies, sep = ", ")

print("\n")

shitty_one_msg = f"I removed {shitty_one.title()}, because it's shit, and can't be put inside best movies."
# and use it to tell WHY we got rid of that one
print (shitty_one_msg)
