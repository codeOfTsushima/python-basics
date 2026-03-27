a = int(input())
if a>0:
    print(f"The number {a} is positive")
    if a % 3 == 0 and a % 5 == 0:
        print(f" And also the number {a} is divisible by both 3 and 5 ")
elif a<0:
    print(f"The number {a} is negative")
else:
    print(f"zero is not applicable")

    