# Exercise 005-07 Favorite games:

games_list = []

games_list.append('Doom')
games_list.append('Warcraft II')
games_list.append('Cadillacs and Dinosaurs ARCADE')
games_list.append('TekWar')
games_list.append('Worms')
games_list.append('Quake')
games_list.append('Super Mario Bros')
games_list.append('Another World')
games_list.append('Quake 2')
games_list.append('Aliens vs Predator')
games_list.append('Half-Life')
games_list.append('Fallout 2')
games_list.append('Heroes of Might and Magic III')
games_list.append('Half-Life 2')
games_list.append('Jedi Knight')
games_list.append('Rune')
games_list.append('Warcraft III')
games_list.append('Fallout: New Vegas')
games_list.append('Alien: Isolation')
games_list.append('The Last of Us')
games_list.append('God of War IV')

print("Print raw list:")
print(games_list)

print('\n"if" with additional variables:')

tlou_game = 'The Last of Us'
if tlou_game in games_list:
    print(f"I just love {tlou_game}! Best game ever!")

alien_game = 'Alien: Isolation'
if alien_game in games_list:
    print(f"Another extreme good game is {alien_game}!")

another_game = 'Another World'
if another_game in games_list:
    print(f"Ah... {another_game}... This one is super nostalgic.")

fallout_game = 'Fallout 2'
if fallout_game in games_list:
    print(f"{fallout_game} took hours, weeks and months from my life!")

half_game = 'Half-Life'
if half_game in games_list:
    print(f"{half_game} is on of the best science-fiction" 
          f"old school FPS! Ahhh those vibes!")

fifa_game = "Fifa 11"
if fifa_game in games_list:
    print("Ah great game!")
else:
    print("Yeah like I care about Fifa and such games - it's not on my list.")

warcraft_game = 'Warcraft II'
if warcraft_game in games_list:
    print("Zug zug!")

heroes_game = 'Heroes of Might and Magic III'
if heroes_game in games_list:
    print(f"Rampart was my favorite in {heroes_game}!")

print('\n"if" without additional variables:')

if 'Quake' in games_list:
    print(f"Ah, {games_list[5]}... I've played it on 486 with Win95 :D")
if 'Quake 2' in games_list:
    print(f"And {games_list[8]}, hours played in internet cafe with my"
          f" friends.")
if 'Cadillacs and Dinosaurs ARCADE' in games_list:
    print(f'{games_list[2]} is a cool oldie XD')
if 'Doom' in games_list:
    print(f"Old, one of the first of its kind - {games_list[0]}!")
if 'Rune' in games_list:
    print(f"{games_list[15]} - I've got a clan for this one, cool old PC game!")
