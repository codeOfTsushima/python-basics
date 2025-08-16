first=0
Second=1
no=int(input("ethra fibonacci venam?"))
if no<=0:
    print("enter positive integer")
else:
    print (first)
    print (Second)
    for i in range(2,no):
        third=first+Second
        first=Second
        Second=third
        print (third)
