# Execrise 3-1 Names list

names = ['jan kowlaski', 'tomasz kwiatkowski', 'michaal glowala', 'szymon przecier', 'jan jankowski', 'everest pierskowski', 'ostatni ostatniewski']

print(names)
print(*names, sep = ", ")

# If you will just print list, it will be printed raw.

print(f'\n{ names[0].title()}')
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(names[5].title())
print(names[6].title())

print(f"\n{names[-1].title()}")
print(names[-2].title())
print(names[-3].title())
print(names[-4].title())
print(names[-5].title())
print(names[-6].title())
print(names[-7].title())

# Execise 3-2 Greetings message

greet_1 = f"\nGreetings you old goat {names[0].title()}!"
greet_2 = f"\nGreetings you old goat {names[1].title()}!"
greet_3 = f"\nGreetings you old goat {names[2].title()}!"
greet_4 = f"\nGreetings you old goat {names[3].title()}!"
greet_5 = f"\nGreetings you old goat {names[4].title()}!"
greet_6 = f"\nGreetings you old goat {names[5].title()}!"
greet_7 = f"\nGreetings you old goat {names[6].title()}!"

print (greet_1, greet_2, greet_3, greet_4, greet_5, greet_6, greet_7)

print(greet_1)
print(greet_2)
print(greet_3)
print(greet_4)
print(greet_5)
print(greet_6)
print(greet_7)


# exercise 3-3 My own list of favorite games ever

fav_games = ['the last of us part 1', 'fallout 2', 'fallout: new vegas', 'alien: isolation', 'half-life', 'half-life 2', 'warcraft 2 (zonk-zonk!)', 'metro redux', 'god of war 4', 'god of war: ragnarok', 'the last of us part 2']

games_i_would_like_to_play_again = f"\nThis is the list of games I would like to play (mostly again):\n{fav_games[0].title()},\n{fav_games[1].title()},\n{fav_games[2].title()},\n{fav_games[3].title()},\n{fav_games[4].title()},\n{fav_games[5].title()},\n{fav_games[6].title()},\n{fav_games[7].title()},\n{fav_games[8].title()},\n{fav_games[9].title()},\n{fav_games[10].title()}."

best_of_all = f"\nMy UNDISPUTED best of all times game, that got me a while to get back to reality, is { fav_games[0].upper() }!\n"
last_one = f"The last game that I've played was {fav_games[-1].title()}."
not_played = f"Game that I have not played yet from list above is {fav_games[-2].title()}."

print(games_i_would_like_to_play_again)
print(best_of_all)
print(last_one)
print(not_played)
print(*fav_games, sep = ", ")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

bicycles = ['trekking', 'cannondale', 'redline', 'mountain bike', 'specialized']

print(f"\n\n\n\n\n\n\n{bicycles[-1].title()}")
''' index -1 is very useful, becuase you often want to access last item from
the list not knowing how long the list is.'''

print(bicycles[-2].title())
print(bicycles[-3].title())
print(bicycles[-4].title())
print(bicycles[-5].title())
print(*bicycles, sep = ", ")

# Paul 02.05.2022 index position start at 0, not at 1
# Paul 03.05.2022 [-1] will print the last position on the list, [-2] second from the end, and so forth...

bicycles[3] = "rower gorski" # Paul 03.05.2022 - I found it myself >:D

print ( f"\n{ bicycles[-2].upper() } list number [-2] works when earlier I modyfied list from 'mountain bike' to 'rower gorski!" )

msg_1 = f"\n\tI want to have { bicycles[0].upper() } bicycle." # Paul 03.05.2022 - f"bla bla bla {BLEBLE-method}, bla bla bla."
msg_2 = f"\t\tI want to have { bicycles[1].upper() } bicycle."
msg_3 = f"\t\t\tI want to have { bicycles[2].upper() } bicycle."
msg_4 = f"\t\t\t\tI want to have { bicycles[3].upper() } bicycle."
msg_5 = f"\t\t\t\t\tI want to have { bicycles[4].upper() } bicycle."

print ( msg_1 )
print ( msg_2 )
print ( msg_3 )
print ( msg_4 )
print ( msg_5 )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #v

bicycles2 = ['trekking', 'cannondale', 'redline', 'mountain bike', 'specialized']

bicycles2[1] = "wtf is this second bike?"

message2 = f"\n{ bicycles2[0] }, { bicycles2[1] }, { bicycles2[2] }, { bicycles2[3] }, { bicycles2[4] }"
message1 = message2.upper()

print ( message1 )
print ( *bicycles2, sep = ", " )
print ( *message1, sep = " " ) # noice XD