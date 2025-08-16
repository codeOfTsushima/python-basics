import random
num = random.randint(1, 10)
guess = int(input("guess a number between 1 and 10"))
if guess == num:
    print("correct, You guessed it....yayyyy")
elif guess < num:
    print("too low noob, The number was", num)
else:
    print("too high noob, The number was", num)
