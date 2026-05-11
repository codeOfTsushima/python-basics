user_input = input("Enter numbers separated by space: ")

num = list(map(int, user_input.split()))

firstel = num[0]
lastel = num[-1]
print(f"First element{firstel}")
print(f"Last element{lastel}")

sublistMid = num[2:5]
subliststart = num[:3]

print(f"Subist from 2 to 5 {sublistMid}")
print(f"Sub list from 3 end {subliststart}")