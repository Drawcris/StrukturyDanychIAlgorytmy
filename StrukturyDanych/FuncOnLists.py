from functools import reduce

numbers =  [1,45,672,7265,16]

sorted(numbers, key=lambda x: x % 10)


codes = ['JPID', 'JJJPPP', 'XXX', 'JDU']

reduce(lambda x,y: x if len(x) > len(y) else y, codes)


capitals =['Rome', 'Paris', 'Madrid']
cities = ['Rome', 'Napoli', 'Rimini', 'Paris', 'Barcelona', 'Madrid', 'Marceille']

not_in_capitals = list(filter(lambda city: city not in capitals, cities))
print(not_in_capitals)


