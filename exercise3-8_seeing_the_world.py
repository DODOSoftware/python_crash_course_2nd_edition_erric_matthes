

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print ( '\n\n' )
# Paul 09.05.2022 - sorting lists by .sort() method - easy and PERMANENT

cars = [ 'bmw', 'subaru', 'volvo', 'hyundai', 'toyota', 'opel', 'skoda', 'dodge', 'fiat', 'volkswagen', 'audi', 'ford', 'citroen', 'mercedes']
print ( '\nOriginal unsorted list (with lower case, because sorting with capitals is more complicated):')
print ( cars )

print ( '\n\nSorting permanently with .sort() method normal and in reverse:\n' )

cars.sort()
print ( cars )

cars.sort( reverse = True )
print ( cars )

# Paul 09.05.2022 - sorting list temporarily with .sorted() method

print ( '\n\nSorting temporarily with .sorted() method:\n' )

cars = [ 'bmw', 'subaru', 'volvo', 'hyundai', 'toyota', 'opel', 'skoda', 'dodge', 'fiat', 'volkswagen', 'audi', 'ford', 'citroen', 'mercedes']
# ^^ Paul 09.05.2022 - must've create list again, because used method .sort() on the first original list.

print ( '- Here is the original list again:')
print ( cars )

print ( '- Here is .sorted() list:')
print ( sorted(cars) )

print ( '- And original list again:' )
print ( cars )

print ( '\nSorting list in reverse (without sorting alphabetically - just plain reverse as it is):')
cars.reverse()
print ( cars )

print ( '\nSo I will put it in alphabeticall order first, and then reverse perhaps?:')
cars.sort() # Paul 09.05.2022 - at this point I was trying to write two methods at once, but no success...
cars.reverse()
print ( cars ) # Paul 09.05.2022 - yup, it worked fine I guess

print ( '\nThe .reverse() method is permanent, but you can undo it, just by again using it...' )
cars.reverse()
print ( cars )

print ( '\nIdentify lenght of the list by using len() function:' )
print ( len( cars ) ) # Paul 09.05.2022 - len() function should be printed between ( )


# Paul 09.05.2022 - I'm glad, that I kinda... sorted it out... #extremedrydadjoke