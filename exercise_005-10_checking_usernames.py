current_users = ['general Kenobi', 'Kofi', 'Rapek', 'john Wick', 'Ender']
new_users = ['Kofi', 'Rapek', 'Wild John', 'Mel Gibson', 'Ding Dong']

current_users_lower = [x.lower() for x in current_users]
#Paul 20.05.2022 new list in lower case!

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Your name {new_user} is in use, choose other name!")
    else:
        print(f"Hello there {new_user}, your name is available!")

''' Paul 20.05.2022 checking in lower case needed to make another list
-> current_users_lower to work with, and then loop for in, with .lower()'''