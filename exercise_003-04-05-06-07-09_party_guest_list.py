# Exercise 3-4 Guest List:


guest_list = ['albert einstein', 'nikola tesla', 'thomas aquinas',
              'platon', 'socrates', 'leonardo da vinci', 'isaac newton']

invitation0 = f"Hereby I invite you Sir {guest_list[0].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation1 = f"Hereby I invite you Sir {guest_list[1].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation2 = f"Hereby I invite you Sir {guest_list[2].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation3 = f"Hereby I invite you Sir {guest_list[3].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation4 = f"Hereby I invite you Sir {guest_list[4].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation5 = f"Hereby I invite you Sir {guest_list[5].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation6 = f"Hereby I invite you Sir {guest_list[6].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!\n"

print(invitation0)
print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)
print(invitation5)
print(invitation6)

guest_number = f"Total guests number: {len(guest_list)}."
print(guest_number)


# Exercise 3-5 Changing Guest List:


pop_newton = guest_list.pop()
msg_newton = f"\nSir {pop_newton.title()} politely must decline, " \
             f"for he's not done with physics laws yet.\n"
print(msg_newton)

guest_list.append('aristotle')
msg_aristotle = f"But Sir {guest_list[6].title()} will gladly take the " \
                f"invitation!\n\n"
print(msg_aristotle)

invitation6 = f"Hereby I invite you Sir {guest_list[6].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!\n"
print(invitation0)
print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)
print(invitation5)
print(invitation6)

guest_number = f"Total guests number: {len(guest_list)}."
print(guest_number)


# Exercise 3-6 More Guests:


bigger_table_msg = "\n\nHey folks, I've found and ordered a bigger table, " \
                   "so we will have room for three more!\n\n"
print(bigger_table_msg)
guest_list.insert(0, "stephen hawking")
guest_list.insert(3, "alfred nobel")
guest_list.insert(len(guest_list), "max planck")
''' Paul 09.05.2022 - 'len(list_name)' command allows you to .insert()
in the last position on the list.'''

invitation0 = f"Hereby I invite you Sir {guest_list[0].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation1 = f"Hereby I invite you Sir {guest_list[1].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation2 = f"Hereby I invite you Sir {guest_list[2].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation3 = f"Hereby I invite you Sir {guest_list[3].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation4 = f"Hereby I invite you Sir {guest_list[4].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation5 = f"Hereby I invite you Sir {guest_list[5].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation6 = f"Hereby I invite you Sir {guest_list[6].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation7 = f"Hereby I invite you Sir {guest_list[7].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation8 = f"Hereby I invite you Sir {guest_list[8].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!"
invitation9 = f"Hereby I invite you Sir {guest_list[9].title()} to a wild " \
              f"Birthday Party, on my birthday 24.01 at Costa Rica beach!\n"

print(invitation0)
print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)
print(invitation5)
print(invitation6)
print(invitation7)
print(invitation8)
print(invitation9)

guest_number = f"Total guests number: {len(guest_list)}."
print(guest_number)


# Exercise 3-7 Shrinking List:


sorry = "\nDear Guests, I'm sincerely in deep sorrow, but I must refuse, " \
        "because book of Python tell me to do it, and invite only two of you." \
        "Now I will pop out almost all of you, but do not despair. " \
        "Please keep in mind that I will try organize our party in full soon. "\
        "We will be in touch, and then everybody will be invited!\n"
print(sorry)

guest_list.pop()  # Paul 09.05.2022 - YEAH, POP'EM ALL!
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()

message = f"Please keep in mind, Dear { guest_list[0].title() } and " \
          f"{ guest_list[1].title() }, that you are still invited!"
print(message)

del guest_list[1], guest_list[0]

print(f"Is any one on the {guest_list}??? No....")
# Paul 09.05.2022 - empty list funny square brackets at last :)

guest_number = f"Total guests number: {len(guest_list)}."
print(guest_number)
