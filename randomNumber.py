import random
num = random.randint(1, 10)
guess = int(input("guess a number between 1 and 10"))
if guess == num:
    print("correct, You guessed it right!")
elif guess < num:
    print("too low, The number was", num)
else:
    print("too high, The number was", num)
