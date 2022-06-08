# Chapter 006 NOTES - Dictionaries continuation, looping a dictionary.
# Looping through a dictionary - you can loop through all key-values pairs, and
# keys or values itself.

# Looping through all key-value pairs:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
print("Loop through whole dictionary:")
for key, value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

# Paul 04.06.2022 you can choose any names for your two, new variables, for
# example go with abbreviations of words "key" and "value":
print("\nWith abbreviations:")
for k, v in user_0.items():
    print(f"\nK:{k}")
    print(f"V:{v}")

# Or any other variables names you choose:
print("\nAnything and everything:")
for anything, everything in user_0.items():
    print(f"\nAnything:{anything}")
    print(f"Everything:{everything}")

# Paul 04.06.2022 The .items() method returns a list of key-value pairs,
# adding it in the second part of 'for' statement will allow looping
# through entire dictionary in effect. Looping through entire dictionary works
# particularly well for dictionaries that contain same kind of information.

favorite_languages = {
                      'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }
print("\n")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is: {language.title()}")

# Paul 08.06.2022 Looping through the keys in the dictionary with .key()
# method, and then default (same as .keys()):
print("\nPrinting with .keys() method:")
for name in favorite_languages.keys():
    print(name.title())
print("\nPrinting with default:")
for name in favorite_languages:
    print(name.title())

# You can choose the .keys() method when e.g. you want your code to be
# easier to read, or you can omit it if you want.

# Now it's time to loop to get keys we wanted, and print other message (pull
# out the interesting keys, not the whole):

friends = ['jen', 'phil']

print("\n")
for name in favorite_languages.keys():
    print(f"Hello, {name.title()}!")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tHello {name.title()}! I see that you also love "
              f"{language.title()}.")
# "We check whether the name we’re working with is in the list friends. If it
# is, we determine the person’s favorite language using the name of the
# dictionary and the current value of name as the key."

# Now we check if there is interesting us key:
if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

# .keys() method is not only for looping, in reality it returns all the
# keys in the dictionary.

print("\nLooping through a dictionary in a alphabetic order:")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

print("\nLooping through a dictionary, reverse=True:")
for name in sorted(favorite_languages.keys(), reverse=True):
    print(f"{name.title()}, thank you for taking the poll!")
