ele = input()
num = tuple(map(int, ele.split()))

firstEle = num[0]
thirdEle = num[2]
print(f"First element: {firstEle} third element: {thirdEle}")
tupleLength = len(num)
print(f"tuple length: {tupleLength}")

tuplecount = 20
occCount = num.count(tuplecount)
print(f"The element {tuplecount} appears {occCount} times")