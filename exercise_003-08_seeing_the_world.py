places = ['norway', 'usa', 'san giovani rotondo italy', 'canada', 'japan', 'thailand', 'bora-bora', 'the maldives', 'philiphines', 'greece']
print(f'Places we want to go:')
print(places)

print('\nUse .sorted() method:')
print(sorted(places))

print('\nStill intact, because of .sorted() method:')
print(places)

print('\nReverse and then print:')
places.reverse()
print(places)

print('\nAnd reverse again:')
places.reverse()
print(places)

print('\nNow .sort() and then print:')
places.sort()
print(places)

print('\nAnd at last .sort() in reverse:')
places.sort(reverse = True)
print(places)