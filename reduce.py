from functools import reduce
def mult(x, y):
    return x * y

nlsit = [1,2,3,4]

total = reduce(mult, nlsit)
print(total)