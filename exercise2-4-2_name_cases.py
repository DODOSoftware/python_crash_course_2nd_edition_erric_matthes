# kropka po nazwie zmiennej 'name' wskazuje pyhtonowi, że metoda 'title' ma zostać do niej zastosowana. metoda 'title' zmienia pierwsze litery na duże, a podwójny nawias wskazje metodom dodatkowe informacje - metoda 'title' nie wymaga dodatkowych informacji. Zmiany wielkości liter można również uzyskać przez metody 'upper' oraz 'lower'.

name = "john wick"
print ( name.title() )
print ( name.upper() )
print ( name.lower() )

print ( "My name is " + name )
print ( "My name is " + name.title() )
print ( "My name is " + name.upper() )
print ( "My name is " + name.title() + ", and you're about to die for my doggo.")

age = "37"

print ( "My name is " + name.title() + " and I'm " + age + " years old.")

# Paul 07.05.2022 - f-strings are better to use