month = int(input("Enter month"))
match month:
    case 12|1|2:
        print("It's the winter season")
    case 3|4|5:
        print("It's the summer season")
    case 6|7|8:
        print("It's the Monsoon season")
    case 9|10|11:
        print("It's the Autumn season")
    case _:
        print("Invalid")
        