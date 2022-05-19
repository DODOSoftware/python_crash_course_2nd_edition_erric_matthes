# Exercise 005-08 Hello Admin:

registered_users = []

registered_users.append('Dodo')
registered_users.append('admin')
registered_users.append('Hania')
registered_users.append('Pawel')
registered_users.append('Tygrys')
registered_users.append('Rapek')
registered_users.append('Kofi')

for registered_user in registered_users:
    if registered_user.lower() == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {registered_user.title()}, nice to see you again!")

# Exercise 005-09 No users:

print("\nChecking if list is empty:")
'''Paul 19.05.2022 again variables need to be defined realier in the code! '''




''' SOMETHING'S NOT WORKING HERE! 

registered_users = []

if registered_user in registered_users:
    for registered_user in registered_users:
        if registered_user.lower() == 'admin':
            print('Hello Admin, would you like to see a status reports?')
        else:
            print(f"Hello {registered_user.title()}, nice to see you again!")
else:
    print("There are no registered users!")