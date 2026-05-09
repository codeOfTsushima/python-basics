word = input()
vowels = "a,e,i,o,u"
vowelcount = 0
for char in word.lower():
    
    if char in vowels:
        vowelcount +=1
print(f"Total vowels: {vowelcount}")
    
    