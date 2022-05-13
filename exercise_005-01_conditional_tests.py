

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print('\nSimple "if" (True/False) in the loop "for":')

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
values DO NOT MATCH EACH OTHER (True/False).'''

