first_name = "jan"
last_name = "kowalski"
full_name = f"{first_name} {last_name}"
lower_case = full_name.lower()
upper_case = full_name.upper()
title_case = full_name.title()
capitalize_case = full_name.capitalize()

print(lower_case)
print(upper_case)
print(title_case)
print(capitalize_case)
# Paul 07.05.2022 - capitalize make only first letter capital!

print(last_name[0:4])  # SLICING, I LIKE SLICING >:D

print(f"\nThe len() function will figure out length of a string."
      f"In that case, the length of 'kowalski' variable is {len(last_name)}.\n")
