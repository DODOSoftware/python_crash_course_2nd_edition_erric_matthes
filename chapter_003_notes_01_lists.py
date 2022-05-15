# Chapter 003 NOTES lists, index 

bicycles = ['trekking', 'cannondale', 'redline', 'mountain bike', 'specialized']

print(f"\n\n\n\n\n\n\n{bicycles[-1].title()}")
''' index -1 is very useful, becuase you often want to access last item from
the list not knowing how long the list is.'''

print(bicycles[-2].title())
print(bicycles[-3].title())
print(bicycles[-4].title())
print(bicycles[-5].title())
print(*bicycles, sep = ", ")

# Paul 02.05.2022 index position start at 0, not at 1
# Paul 03.05.2022 [-1] will print the last position on the list, [-2] second from the end, and so forth...

bicycles[3] = "rower gorski" # Paul 03.05.2022 - I found it myself >:D

print ( f"\n{ bicycles[-2].upper() } list number [-2] works when earlier I modyfied list from 'mountain bike' to 'rower gorski!" )

msg_1 = f"\n\tI want to have { bicycles[0].upper() } bicycle." # Paul 03.05.2022 - f"bla bla bla {BLEBLE-method}, bla bla bla."
msg_2 = f"\t\tI want to have { bicycles[1].upper() } bicycle."
msg_3 = f"\t\t\tI want to have { bicycles[2].upper() } bicycle."
msg_4 = f"\t\t\t\tI want to have { bicycles[3].upper() } bicycle."
msg_5 = f"\t\t\t\t\tI want to have { bicycles[4].upper() } bicycle."

print ( msg_1 )
print ( msg_2 )
print ( msg_3 )
print ( msg_4 )
print ( msg_5 )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

bicycles2 = ['trekking', 'cannondale', 'redline', 'mountain bike', 'specialized']

bicycles2[1] = "wtf is this second bike?"

message2 = f"\n{ bicycles2[0] }, { bicycles2[1] }, { bicycles2[2] }, { bicycles2[3] }, { bicycles2[4] }"
message1 = message2.upper()

print ( message1 )
print ( *bicycles2, sep = ", " )
print ( *message1, sep = " " ) # noice XD