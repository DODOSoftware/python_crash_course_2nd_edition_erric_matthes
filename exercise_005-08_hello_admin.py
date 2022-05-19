# Exercise 005-08 Hello Admin

registered_users = []

registered_users.append('Dodo')
registered_users.append('admin')
registered_users.append('Hania')
registered_users.append('Pawel')
registered_users.append('Tygrys')
registered_users.append('Rapek')
registered_users.append('Kofi')

for user_name in registered_users:
    if user_name.lower() == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user_name.title()}, nice to see you again!")