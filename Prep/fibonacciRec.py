a = int(input("Enter the nth number"))
def fibonacci(n):
    if n==1:
        return 1
    elif n==0:
        return 0 
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(f"The {a} fibonacci number is {fibonacci(a)}")
