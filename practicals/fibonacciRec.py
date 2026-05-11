def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

nums = int(input())
if nums<= 0:
    print("Enter positive integer")
else:
    print("Fibonacci series")
    for i in range(nums):
        print(fibonacci(i), end = " ")