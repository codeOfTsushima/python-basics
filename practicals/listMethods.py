InpEle = input()
num = list(map(int, InpEle.split()))

num.append(50)
print(f"After append: {num}")

num.insert(2,15)
print(f"After insertion: {num}")

num.pop(2)
print(f"After pop: {num}")

num.remove(40)
print(f"After removing: {num}")

num.sort()
print(f"After sorting elements{num}")

