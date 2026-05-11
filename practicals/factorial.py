def factorial(n):
    if n< 0:
        return "No fact"
    elif n==0:
        return 1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial

num = int(input())

result = factorial(num)
print(result)
