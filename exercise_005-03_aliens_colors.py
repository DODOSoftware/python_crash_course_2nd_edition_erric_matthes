# Exercise 005-03 Aliens colors:

alien_color = 'yellow'

if alien_color == 'green':
    print("You've earned 5 points!")
elif alien_color == 'yellow':
    print("You've earned 10 points!")
elif alien_color == 'red':
    print("You've killed alien leader and earned 15 points!")
'''There are at least two ways to do it:
first is standard and simple "if"
second is with "if-elif".'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print('\nSimple "if-else" statements again:')
print('\n"if conditional test True:\n\tdo something\nelse:\n\tdo something else."')
        # Paul 14.05.2022 rememeber about indentation!

age = 17
if age >= 18:
    print("\nYou're old enough to to vote!")
    print("Have you registered to vote yet?")
    print("Click here for register!")
    print("Come on do it! Come on!")
    print("GO TO DA CHOPPA! COME ON!")
    # Paul 14.05.2022 ^ famous Arnold Shwarzenegger quote.
else:
    print("\nSorry, you're not enough old to vote.")
    print("Please register as soon as you turn 18 years old!")
    print("And while waiting enjoy your youth!")

print('\nStarting "if-elif-else" statements:\n')

print("Amusement Park admission cost:")

age = 67

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

print("\nKeep it shorter with 'price' viarable:")
# Paul 14.05.2022 shorter, more efficient, output message easier to change.
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

print('\nMultiple "elif" blocks:')
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
# Paul 14.05.2022 65 years old or older.
print(f"Your admission cost is ${price}.")

print('\nOmitting the "else" block:') # <---
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

'''NOTE: With added "elif" at the end it is bit clearer to read. With this change
every block of codemust pass a specific test in order to be executed. The "else"
block is matched if any other match with "if" and "elif" is not met. That can 
sometimes include valid or even malicious data, so if you have specific final
condition that you're testing for, consider using "elif" and omit the "else"
block. That give you extra confidence that your code will run only under the
correct conditions.

"if-elif-else" as soon Python finds one test that passes, it skips others.'''

print("\nTesting MULTIPLE conditions, without 'elif' and 'else':")

requested_toppings = ['mushrooms', 'extra cheese', 'tomato', 'olives']

if 'mushrooms' in requested_toppings:
    print('Addinig mushrooms.')
if 'olives' in requested_toppings:
    print('Addinig olives.')
if 'salami' in requested_toppings:
    print('Addinig salami.')
if 'extra cheese' in requested_toppings:
    print('Addinig extra cheese.')
if 'ham' in requested_toppings:
    print('Addinig ham.')
if 'sausage' in requested_toppings:
    print('Addinig sausage.')
if 'corn' in requested_toppings:
    print('Addinig corn.')
if 'big paste' in requested_toppings:
    print('Addinig big paste.')
if 'beef' in requested_toppings:
    print('Addinig beef.')
if 'tomato' in requested_toppings:
    print('Addinig tomato.')

print('\nFinished making your pizza!')

'''NOTE: This will evaluate all conditions of interest! If you want only one
block of code run, use an "if-elif-else" chain. If more than one block needs
to be run, use a series of independent "if" statements.'''