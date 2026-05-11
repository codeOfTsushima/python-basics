char = input()
if len(char) == 1:
    ascii_val = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_val}")
else:
    print("Enter one charecter")