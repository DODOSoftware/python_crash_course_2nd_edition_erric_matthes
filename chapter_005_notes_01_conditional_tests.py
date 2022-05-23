# Chapter 005 NOTES == != ...

'''

    ==      if matched: True

    !=      if matched: False! if doesn't match: True! Simple logic right?

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

# NOTE: Conditional test is an expression, that can be evaluated
# as True of False, whether the code in an "if" statement should
# be executed. If test evaluates True, then Python executes the code
# within "if", if test evaluates False, then Python ignores the code
# of the "if" statement.

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
# Paul 13.05.2022 using .lower() function if case is not the case
# in equality test. It also doesn't change the value of the original variable.
print(car)

# NOTE: e.g. when site user is submitted, code will change existing "John"
# into .lower() and reject any variation of it, like "john", "johN", etc.

required_toppings = ['mushrooms', 'onion', 'cheddar cheese']
if required_toppings != 'anchoveis':
    print('\nClient requested anchoveis.')
# Paul 13.05.2022 exclamation point and equal sign represent "not" phrase.
# If there is no match in "required_toppings" for "anchevois", than Python
# will return with True, and execute program. If there would be match,
# then return would be False. Python checks if those
# values DO NOT MATCH EACH OTHER (True).


print('\nNumerical comparisons:')

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

print('\nChecking multiple conditions with "and":')
# Paul 13.05.2022 - both True simultaneously.

age_0 = 21
age_1 = 21
if (age_0 >= 21) and (age_1 >= 21):
    # Paul 13.05.2022 ^ IMO parentheses looks good.
    print('Both are age 21 or more.')

age_0 = 34
age_1 = 17
if (age_0 >= 21) and (age_1 >= 21):
    print('Both are age 21 or more.')  # one of them it's not over 21.

print('\nChecking multiple conditions with "or":')
# Paul 14.05.2022 True if either or both of tests passes.

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