# Exercise 005-08 Hello Admin:

users = []

users.append('Dodo')
users.append('admin')
users.append('Hania')
users.append('Pawel')
users.append('Tygrys')
users.append('Rapek')
users.append('Kofi')

for user in users:
    if user.lower() == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, nice to see you again!")

# Exercise 005-09 No users:

print("\nChecking if list is empty:")
'''Paul 19.05.2022 again variables need to be defined realier in the code! '''

users = []

if users is not None:
    for user in users:
        if user.lower() == 'admin':
            print('Hello Admin, would you like to see a status reports?')
        else:
            print(f"Hello {user.title()}, nice to see you again!")
else:
    print("There are no registered users!")