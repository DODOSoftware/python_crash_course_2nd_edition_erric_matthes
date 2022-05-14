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

print('\nSimple numerical tests:')

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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

'''

    ==      if match: True

    !=      if match: False! if dosen't match: True! Simple logic right?

    <       strictly less than

    <=      less than or equal

    >       strictly greater than

    >=      greater than or equal

    is      object identity

    is not  negated object identity

'''

print('\n\nSimple "if" (True/False) in the loop "for":')

cars = ['audi', 'bmw', 'subaru', 'toyota', 'skoda']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

'''NOTE: Conditional test is an expression, that can be evalueted
as True of False, wheter the code in an "if" statement should
be executed. If test evaluates True, than Python execute the code
within "if", if test evaluates False, than Python ignores the code
of the "if" statement.'''


print('\nSimple equality ==, and inequality != tests:')

car = 'bmw'
if car == 'bmw':
    print("\nYes, it's BMW.")
    # Paul 13.05.2022 figured it out myself :) Conditional test return True

car = 'audi'
if car == 'bmw':
    print("\nYes, it's BMW.")
# Paul 13.05.2022 conditional test return False

'''NOTE: double == name's 'equality operator'. Equal sign can be read as:
"Set the value of car equal to audi", and double == is read as question
"Is the value of variable equal to bmw?"
NOTE: simple conditional tests checks if value of variable is equal
to the value of interest.'''

car = 'Audi'
if car == 'audi':
    print('\nTrue!')
    # Paul 13.05.2022 testing for equality is cAsE sensitive in Python.

car = 'Audi'
if car.lower() == 'audi':
    print('\nTrue!')
'''Paul 13.05.2022 using .lower() function if case is not the case
in equality test. It also doesn't chage the value of the original viarable.'''
print(car)

'''NOTE: e.g. when site user is submitted, code will change existing "John"
into .lower() and reject any variation of it, like "john", "johN", etc.'''

required_toppings = ['mushrooms', 'onion', 'cheddar cheese']
if required_toppings != 'anchoveis':
    print('\nClient requested anchoveis.')
'''Paul 13.05.2022 exclamation point and equal sign represent "not" phrase.
If there is no match in "reguired_toppings" for "anchevois", than Python
will returns with True, and execute program. If there would be match,
than return would be False. Python checks if those
values DO NOT MATCH EACH OTHER (True).'''


print('\nNumerical comparisions:')

age = 18
if age == 18:
    print('\nValid age')
answer = 17
if answer != 42:
    print('\nThat is not correct answer. Please try again!')

print('\n"if" age, than (LOGIC HERE PLEASE):')

age = 18                           # Paul 13.05.2022 age threshold in PL is 18yo
if age < 18:                       # LESS THAN (YEAH SCIENCE! - J. PINKMAN)
    print('INVALID AGE!')
if age >= 18:                      # GREATER THAN OR EQUAL
    print('VALID AGE!')

print('\nChecking multipe conditions with "and":')
# Paul 13.05.2022 - both True simultaneously.

age_0 = 21
age_1 = 21
if (age_0 >= 21) and (age_1 >= 21): # Paul 13.05.2022 IMO parentheses look good.
    print('Both are age 21 or more.')

age_0 = 34
age_1 = 17
if (age_0 >= 21) and (age_1 >= 21):
    print('Both are age 21 or more.') # one of them it's not over 21.

print('\nChecking multipe conditions with "or":')
# Paul 14.05.2022 True if either or both of tests passes

age_0 = 22
age_1 = 18
if (age_0 >= 21) or (age_1 >= 21):
    print('"or" test passed.')

age_0 = 20
age_1 = 18
if (age_0 >= 21) or (age_1 >= 21):
    print('"or" test passed.')
    # Paul 14.05.2022 - both are not >= 21, test returns False.

print('\nChecking whether a value is IN the list:')
required_toppings = ['mushrooms', 'onions', 'ham', 'olives', 'corn']
if 'mushrooms' in required_toppings:
    print('There are mushrooms in the order.')
if 'pepperoni' in required_toppings:
    print('There is pepperoni in the order.')
    # Paul 14.05.2022 test returns False, so no pepperoni for you!

'''NOTE form the manual: This technique is powerful because you can create
a list of essential values, and then easily check whether the value you're
testing matches on the values in the list.'''

print('\nList of banned people: (not in checking):')
banned_ppl = ['ewa', 'pawel', 'alina', 'mirela', 'maciej', 'jakub', 'bogna']
user = 'hanna'
if user not in banned_ppl:
    print(f"{user.title()} you can post answer now.")

'''Boolean expression = conditional test. True of False.
Boolean values provide an efficient way to track the state of program or
a particular condition that is important to you program.'''