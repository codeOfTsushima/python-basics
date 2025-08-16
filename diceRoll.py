import random
while True:
     Choice=input("wanna roll the dice?(y/n):")
     no=random.randint(1,6)
     if Choice=='y':
        print("Your Number is:",no)
     else:
         break