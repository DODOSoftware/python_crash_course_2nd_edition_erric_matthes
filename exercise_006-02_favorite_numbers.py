# Exercise 006-2 Favorite numbers:

fav_number = {'hannah': 7,
              'paul': 7,
              'john': 4,
              'marry': 5,
              }

print(f"Hannah's favorite number is {fav_number['hannah']}!")
print(f"Paul's favorite number is {fav_number['paul']}!")
print(f"John's favorite number is {fav_number['john']}!")
print(f"Marry's favorite number is {fav_number['marry']}!")

print("\nSetting variables first:")

john_fav = fav_number['john']
hannah_fav = fav_number['hannah']
marry_fav = fav_number['marry']
paul_fav = fav_number['paul']
print(f"Hannah's favorite number is {hannah_fav}!")
print(f"Paul's favorite number is {paul_fav}!")
print(f"John's favorite number is {john_fav}!")
print(f"Marry's favorite number is {marry_fav}!")

# Paul 04.06.2022 As above, but first setting input into the dictionary value,
# with the simplest equations:

hannah_input = 10 - 3
paul_input = 14 - 7
john_input = 108 - 104
marry_input = 250 - 245
fav_number = {'hannah': hannah_input,
              'paul': paul_input,
              'john': john_input,
              'marry': marry_input,
              }

print("\nPlaying with variables into values:")

print(f"Hannah's favorite number is {fav_number['hannah']}!")
print(f"Paul's favorite number is {fav_number['paul']}!")
print(f"John's favorite number is {fav_number['john']}!")
print(f"Marry's favorite number is {fav_number['marry']}!")
