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