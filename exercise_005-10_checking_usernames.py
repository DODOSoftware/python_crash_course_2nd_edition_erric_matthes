current_users = ['general Kenobi', 'Kofi', 'Rapek', 'john Wick', 'Ender']
new_users = ['Kofi', 'Rapek', 'Wild John', 'Mel Gibson', 'Ding Dong']

for new_user in new_users:
    if new_user in current_users:
        print(f"Your name {new_user} is in use, choose other name!")
    else:
        print(f"Hello there {new_user}!")

''' Paul 20.05.2022 still wanted to check for .lower() usernames and stuck.