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