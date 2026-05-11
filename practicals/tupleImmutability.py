Ele = input()
num = tuple(map(int, Ele.split()))

try:
    num[0] =10    
except TypeError as e:
    print(f"Error Enccountered: {e}")

