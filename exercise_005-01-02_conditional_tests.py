# Exercise 005-01 Conditional testing - write a series of conditional tests:
car = 'subaru'
if car == 'subaru':
    print(f'If car is {car.title()} I predict True!')
if car == 'toyota':
    print(f'\nIf car is a {car.title()} I predict False!')
    # Paul 14.05.2022 no print for you Toyota, sorry.

swimmingpool = ['towel', 'flip-flops', 'cap', 'goggles', 'trunks']

print('\n== True with "for" loop:') # Paul 14.05.2022 == True
for swim_item0 in swimmingpool:
    if swim_item0 == 'towel':
        print(f'We have {swim_item0}.')
for swim_item1 in swimmingpool:
    if swim_item1 == 'flip-flops':
        print(f'We have {swim_item1}.')
for swim_item2 in swimmingpool:
    if swim_item2 == 'cap':
        print(f'We have {swim_item2}.')
for swim_item3 in swimmingpool:
    if swim_item3 == 'goggles':
        print(f'We have {swim_item3}.')
for swim_item4 in swimmingpool:
    if swim_item4 == 'trunks':
        print(f'We have {swim_item4}.')

print('\n== False with "for" loop:') # Paul 14.05.2022 == False
for swim_item0 in swimmingpool:
    if swim_item0 == 'soap':
        print(f'We have {swim_item0}.')
for swim_item1 in swimmingpool:
    if swim_item1 == 'mattress':
        print(f'We have {swim_item1}.')
for swim_item2 in swimmingpool:
    if swim_item2 == 'swimming sleeves':
        print(f'We have {swim_item2}.')
for swim_item3 in swimmingpool:
    if swim_item3 == 'diving mask':
        print(f'We have {swim_item3}.')
for swim_item4 in swimmingpool:
    if swim_item4 == 'fins':
        print(f'We have {swim_item4}.')

print('\n!= False without loop:') # Paul 14.05.2022 != False
swim_item5 = 'soap'
if swim_item5 != 'soap':
    print('haha False')
swim_item6 = 'mattress'
if swim_item6 != 'mattress':
    print('haha False')
swim_item7 = 'swimming sleeves'
if swim_item7 != 'swimming sleeves':
    print('haha False')
swim_item8 = 'diving mask'
if swim_item8 != 'diving mask':
    print('haha False')
swim_item9 = 'fins'
if swim_item9 != 'fins':
    print('haha False')

print('\n!= True without loop:') # Paul 14.05.2022 != True
swim_item5 = 'soap'
if swim_item5 != 'cake':
    print("haha it's not a cake!")
swim_item6 = 'mattress'
if swim_item6 != 'lamp':
    print("haha it's not a lamp!")
swim_item7 = 'swimming sleeves'
if swim_item7 != 'painting':
    print("haha it's not a painting!")
swim_item8 = 'diving mask'
if swim_item8 != 'candle':
    print("haha it's not a candle!")
swim_item9 = 'fins'
if swim_item9 != 'book':
    print("haha it's not a book!")

print('\nin True:') # Paul 15.05.2022 in True:
if 'towel'in swimmingpool:
    print(f'We have towel.')
if 'flip-flops':
    print(f'We have flip-flops.')
if 'cap' in swimmingpool:
    print(f'We have cap.')
if 'goggles' in swimmingpool:
    print(f'We have goggles.')
if 'trunks' in swimmingpool:
    print(f'We have trunks.')

print('\nnot in True:') # Paul 14.05.2022 not in True:
swim_item10 = 'soap'
if swim_item10 not in swimmingpool:
    print(f"We don't have {swim_item10}!")
swim_item11 = 'mattress'
if swim_item11 not in 'mattress':
    print(f"We don't have {swim_item11}!")
swim_item12 = 'swimming sleeves'
if swim_item12 == 'swimming sleeves':
    print(f"We don't have {swim_item12}!")
swim_item13 = 'diving mask'
if swim_item13 == 'diving mask':
    print(f"We don't have {swim_item13}!")
swim_item14 = 'fins'
if swim_item14 == 'fins':
    print(f"We don't have {swim_item14}!")

# Exercise 005-02 More conditional tests:

print('\nMore conditional tests:')
# Paul 14.05.2022 please don't mind what values contain...

rabbit_1 = 'Rapek'
rabbit_2 = 'Kofi'
if rabbit_1.lower() == 'rapek':
    print('\nOur first mini rabbit is called Rapek.')
if rabbit_2.lower() == 'kofi':
    print('Our second mini rabbit is called Kofi.')
if rabbit_1.lower() != 'kofi':
    print('\nRapek was first, not Kofi.')
if rabbit_2.lower() != 'rapek':
    print('Kofi is our second mini rabbit, she is in lion type.')

if (rabbit_1.lower() == 'rapek') and (rabbit_2.lower() == 'kofi'):
    print('\nWe have two of them, Rapek "and" Kofi.')

if (rabbit_1.lower() == 'rapek') or (rabbit_2.lower() == 'kofi'):
    print('We still have two of them, even I use "or".')


print('\nPrint "and" and "or" tests with lists:')

dogs = ['belgian malinois', 'dutch shepherd dog', 'german shepherd', 'swiss shepherd', 'french shepherd dog bauceron', 'american pit bull terier']
fav_dog = 'belgian malinois'

if fav_dog in dogs:
    print('I love belgian malinois dogs.')
if 'chihuahua' not in dogs:
    print("I don't like small dogs like chihuahua really...")
if 'shepherd' in dogs:      # Paul 14.05.2022 How to run test for a single word?
    print('Hey! We have shepherd dogs in list also!')
else:                       # Paul 14.05.2022 I'll use "else" for now...
    print("We have shepherd dogs in list also, but I don't know how to chceck for silnge word yet.")

print('\nSimple numerical tests, starting with "if-else":')

first_value = 26
second_value = 30
third_value = first_value + second_value

if first_value == 26:
    print('== First value equals 26.')
else:
    print('== First value does not eqaul 26.')

if first_value != 26:
    print('!= First value does not eqaul 26!')
else:
    print('!= First value equals 26!')

if third_value == 56:
    print('first value + second value = 56')
else:
    print('first value + second value =/= 56')

if first_value > second_value:
    print('> First value is greater than second value.')
else:
    print('> First value is lesser than second value.')

if first_value < second_value:
    print('< First value is lesser than second value!')
else:
    print('< First value is greater than second value!')

if first_value <= 17:
    print("You're too young to drink alcohol.")
else:
    print("Your age is valid to drink alcohol.")

if second_value >= 20:
    print("Some message, dunno...")
else:
    print("Other message...")

banned_user = "Ewunia"
if banned_user.lower() == 'ewunia':
    print("\nYou're banned from here!")
else:
    print("Nah, you're still banned XD")