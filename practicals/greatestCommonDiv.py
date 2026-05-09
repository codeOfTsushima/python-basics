# 

def calgcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
        return abs(a)
    
print(f"calc GCD: {calgcd(48,18)}")