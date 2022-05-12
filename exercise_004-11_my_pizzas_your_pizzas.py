# Exercise 004-11 My pizzas, your pizzas:

my_pizzas = ['neapolitanian', 'chicago', 'sicilian']

friend_pizzas = my_pizzas[:]

print ('My pizzas:')
print (my_pizzas)

print ('\nFirend pizzas:')
print (friend_pizzas)

my_pizzas.append('greek')
friend_pizzas.append('new york style')

print ('\nNow my pizzas are:')
for my_pizza in my_pizzas:
	print (my_pizza)

print ('\nNow friend pizzas are:')
for friend_pizza in friend_pizzas:
	print (friend_pizza)