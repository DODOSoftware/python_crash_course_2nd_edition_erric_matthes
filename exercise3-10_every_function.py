
# Paul 10.05.2022 - please don't mind excessive comments - it's just an exercise purpose :)

polish_rivers = [ 'wisla', 'odra', 'warta', 'bug', 'narew', 'san', 'notec', 'pilica', 'wieprz', 'dunajec', 'bobr', 'lyna', 'nysa luzycka', 'wkra', 'brda', 'prosna', 'drweca', 'wislok','wda', 'drawa', 'nysa klodzka', 'poprad', 'pasleka', 'rega', 'bzura', 'wisloka', 'obra', 'lega', 'biebrza', 'wierzyca', 'nida', 'gwda', 'czarna hancza', 'liwiec', 'orzyc', 'wieprza', 'barycz', 'parseta', 'slupia', 'kamienna', 'ner', 'mala panew', 'raba', 'omulew', 'kwisa', 'ina', 'krzna', 'wełna', 'radomka', 'skrwa', 'elk', 'wel', 'radunia', 'szkwa', 'netta', 'suprasl', 'nurzec', 'olawa' ]

print ( '\nSORTING\n' )

# Paul 10.05.2022 - 1. Print unsorted raw list.
print ( 'unsorted raw:')
print ( polish_rivers )

# Paul 10.05.2022 - 2. Sort with .sorted()
print ( '\n.sorted():' )
print ( sorted( polish_rivers ) )

# Paul 10.05.2022 - 3. Sort in reverse with .sorted()
print ( '\n.sorted() with reverse:')
print ( sorted( polish_rivers, reverse = True ) )

# Paul 10.05.2022 - 4. Printing in .reverse()
print ( '\n.reverse():')
polish_rivers.reverse()
print ( polish_rivers )

# Paul 10.05.2022 - 5. Undo the .reverse() by doing it again
print ( '\n.reverse() again:')
polish_rivers.reverse()
print ( polish_rivers )

# Paul 10.05.2022 - 6. Sorting permanently with .sort()
print ( '\n.sort():' )
polish_rivers.sort()
print ( polish_rivers )

# Paul 10.05.2022 - 7. Sorting permanently in reverse with .sort( reverse = True )
print ( '\n.sort( reverse = True ):' )
polish_rivers.sort( reverse = True )
print ( polish_rivers )

# Paul 10.05.2022 - New list for adding, removing and modyfing.
print ( '\nNEW LIST\n')

print ( 'Home Gym equipment list - print raw:' ) # Paul 10.05.2022 - created emtpy list and adding by .append()
home_gym_eq = [ ]
print ( home_gym_eq )

print ( '\nHome Gym equipment .append():' )
home_gym_eq.append( 'barbell' )
home_gym_eq.append( 'weights set' )
home_gym_eq.append( 'rotary torso machine' )
home_gym_eq.append( 'dumbbell double set 2-26kg' )
home_gym_eq.append( 'ab crunch machine' )
home_gym_eq.append( 'kettlebell double set 8-30kg' )
home_gym_eq.append( 'adjustable bench' )
home_gym_eq.append( 'smith machine' )
home_gym_eq.append( 'semi squat rack' )
print ( home_gym_eq )

# Paul 10.05.2022 - modyfing items
home_gym_eq[5] = 'kettlebell double set 8-45kg'
home_gym_eq[8] = 'full squat/power rack double set'
home_gym_eq[0] = '3 barbells set'
home_gym_eq[1] = 'double weight plates set with stands'

print ( '\nModyfied items:' )
print ( home_gym_eq )

# Paul 10.05.2022 - inserting new equipment
home_gym_eq.insert( -1, 'water punching heavy bag' )
home_gym_eq.insert( -2, 'punhcing speed bag' )
home_gym_eq.insert( -3, 'double trx set with anchors in ceiling and walls' )
home_gym_eq.insert( -4, 'gymnastic rings' )
home_gym_eq.insert( 0, 'hex bar' )
home_gym_eq.append( 'exercise bag' )
home_gym_eq.append( 'weight vest' )
home_gym_eq.append( 'big mirrors set' )
home_gym_eq.append( 'gymnastic bar' )
home_gym_eq.append( 'jumping boxes set' )
home_gym_eq.append( 'rubber flooring' )
home_gym_eq.append( 'pull-ups machine' )
home_gym_eq.append( 'set of ding-dongs' ) # Paul 10.05.2022 - for del purposes XD
home_gym_eq.append( 'coordination ladder' )
home_gym_eq.append( 'jumping rope' )
home_gym_eq.append( 'slick floor pads and proper flooring to it' )
home_gym_eq.append( 'gym ladder' )
home_gym_eq.append( 'cable crossover' )
home_gym_eq.append( 'battle ropes' )
home_gym_eq.append( 'ceiling at least at 3.5m' )
home_gym_eq.append( 'couch' )
home_gym_eq.append( 'ceiling gym rope' )
home_gym_eq.append( 'slack line' )
home_gym_eq.append( 'squat wedge' )
home_gym_eq.append( 'double deadlift platforms' )
home_gym_eq.append( 'crash cushions' )
home_gym_eq.append( 'row machine' )
home_gym_eq.append( 'rubber fitness balls' ) #Paul 10.05.2022 - must .append() before .insert(len()), it seems that it override it at the end.
home_gym_eq.insert( len( home_gym_eq ), '4 camera set with live tv screen - important!' ) # Paul 10.05.2022 - inserting at the end with len()
home_gym_eq.insert( 4, 'exercise mats' )
home_gym_eq.insert( 5, 'eliptical' )
home_gym_eq.insert( 2, 'magnetic treadmill' )
home_gym_eq.insert( 3, 'assult bike' )
home_gym_eq.insert( 8, 'electronic clock' )
home_gym_eq.insert( 6, 'rubby rubby bands XD' )


print ( '\nInserted and appended items at once:')
print ( home_gym_eq )

how_many = f'\nHow many equipments are planned: { len( home_gym_eq ) }.'
print ( how_many )

# Paul 10.05.2022 - time to .pop() some useless things, to give it some shape.
pop2 = home_gym_eq.pop(11)

print ( '\nPrint poped "ab crunch machine" list:')
print ( home_gym_eq )

# Paul 10.05.2022 - remove()
print ( '\nRemoved "rotary torso machine", "smith machine", "pull-ups machine" and del "set of ding-dongs":')

shitty0 = 'ab crunch machine'
shitty1 = 'rotary torso machine'
shitty2 = 'smith machine'
shitty3 = 'pull-ups machine'

home_gym_eq.remove( 'rotary torso machine' )
home_gym_eq.remove( 'smith machine' )
home_gym_eq.remove( 'pull-ups machine' )
del home_gym_eq[23]
print ( home_gym_eq )

how_many_after = f'\nHow many equipments after adjustments are made: { len( home_gym_eq ) }.'
print ( how_many_after )

but_why = f"\nWhy? I tell you why - it's because { shitty0 }, { shitty1 }, { shitty2 } and { shitty3 } are fucking useless shit. That's why."
print ( but_why )