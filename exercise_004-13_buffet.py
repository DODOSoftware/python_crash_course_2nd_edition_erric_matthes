# Exercise 004-13 Buffet:

buffet_foods = ('rice', 'chicken', 'fries', 'rancid meat', 'frog eyes')
for buffet_food in buffet_foods:
	print(buffet_food.title())

print('\n')

buffet_foods = ('rice', 'chicken', 'fries', 'red meat', 'salad')
for buffet_food in buffet_foods:
	print(buffet_food.title())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

diemnsions = (200, 50) # Paul 12.05.2022 for tuple use (), and really a coma...
print('\n\nA tuple:')
print(diemnsions[0])
print(diemnsions[1])

mt = (3,) # one element in tuple

# Paul 12.05.2022 looping through tuple
print('\nOriginal diemnsions:')
for diemnsion in diemnsions:
	print(diemnsion)

# Paul 12.05.2022 redefine entire tuple

diemnsions = [400, 100] # redefine
print(f'\nNew dimensions printed as list: {diemnsions}.')

print('\nNew diemnsions loop:')
for diemnsion in diemnsions:
# and loop it (kto k**** wymyślił słowo "iteracja"?!)
	print(diemnsion)

# Paul 13.05.2022 - about time to make lenght line 80 characters in my editor.
# Paul 13.05.2022 - check for tab = 4 spaces