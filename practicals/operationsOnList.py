from functools import reduce

numbs = [1,2,3,4,5,6,7]
print(f"Original list: {numbs}")

squares = list(map(lambda x: x**2, numbs))
print(f"Squares: {squares}")

evens = list(filter(lambda x: x% 2 == 0, numbs))
print(f"Evens {evens}")

sum = reduce(lambda x,y: x+y, numbs )
print(f"Sum {sum}")