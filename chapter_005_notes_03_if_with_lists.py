# Chapter 005 NOTES using 'if' statement with lists:

'''

print('From earlier notes::')

cars = ['audi', 'toyota', 'bmw', 'opel']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

'''

print('USING "if" STAEMENTS WITH LISTS - searching for special values:\n')

print('1. Making your pizza:')
request_toppings = ['muschrooms', 'olives', 'onions', 'green peppers', 'extra cheese']
for request_topping in request_toppings:
    print(f'\t- adding {request_topping}.')
print('\nFinished making your pizza!')

print('\n2. Making your pizza (without one of the toppings):')
request_toppings = ['muschrooms', 'olives', 'onions', 'green peppers', 'extra cheese']
for request_topping in request_toppings:
    if request_topping == 'green peppers':
        print("\t- sorry, we're out of green peppers right now!")
    else:
        print(f'\t- adding {request_topping}.')
print('\nFinished making your pizza!')

# Paul 19.05.2022 LONGER WAY WITH ==

print('\n3. Treatments in physio - THE LONGER WAY WITH ==:\n')
prescribed_treatments = ['laser treatment', 'ultrasound', 'exercises']
for prescribed_treatment in prescribed_treatments:
    if prescribed_treatment == 'laser treatment':
        print(f"Sorry, we don't do here sham treatments as {prescribed_treatment}.")
    elif prescribed_treatment == 'ultrasound':
        print(f"Sorry, we don't do here sham treatments as {prescribed_treatment}.")
    else:
        print(f"You'll have measured for you {prescribed_treatment}, and that's all you need really.")

''' Paul 17.05.2022 using != kept it much shorter, and I'm really happy with
the result. Maybe I'll make a programmer rank after all? All in all it makes
me happy to learning it :) '''

print('\n4. Shorter with != in treatments in physiotherapy:\n')
prescribed_treatments = ['laser treatment', 'ultrasound', 'exercises']
for prescribed_treatment in prescribed_treatments:
    if prescribed_treatment != 'exercises':
        print(f"Sorry, we don't do here sham treatments as {prescribed_treatment}.")
    else:
        print(f"YOU'LL HAVE MEASURED {prescribed_treatment.upper()}, AND THAT'S ALL YOU NEED REALLY.")

print("\n5. Checking if list is empty:")

# Paul 17.05.2022 WATCH FOR INDENETATION!
request_toppings = []
if request_topping in request_toppings:           # 'if'    - NOT idented
    for request_topping in request_toppings:       # 'for'   - indented!
        print(f'\t- adding {request_topping}.')     # 'print' - double indented!
    print("Finished making your pizza!")           # 'print' - indented!
else:                                             # 'else'  - NOT indented
    print("You're sure you want a plain pizza?")   # 'print' - indented!

'''In this example, before we start a 'for' loop, we do a quick check,
'if' requested toppings list is not empty. If requested_toppings passess the
conditional test, Python runs 'for' loop from earlier example. If conditional
test Fail, Python prints a message to the customer.'''
print('\n6. Car parts:')
car_parts = ['bumper', 'brake booster', 'silencer', 'radiator fan', 'coil spring']
for car_part in car_parts:
    print(car_part)

car_parts = []
if car_part in car_parts:
    for car_part in car_parts:
        print(f"Added {car_part} to a cart.")
    print("Go to register.")
    print("Continue buying.")
else:
    print("\nThere are no items in the cart.")

''' Paul 17.05.2022 it appears that you need to specify variable first, and than
add if-else for empty lists.'''

print("\n7. Compose your own pizza:")

availible_toppings = ('muschrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese')
# Paul 19.05.2022 using tuple, for availible toppings are constant in this pizza place
request_toppings = ['muschrooms', 'french fries', 'extra cheese']
for request_topping in request_toppings:
    if request_topping in availible_toppings:
        print(f"- Adding {request_topping}.")
    else:
        print(f"- Sorry, we don't offer {request_topping} on the pizza.")

print("\nFinished making your pizza!")