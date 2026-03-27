c1 = complex(input())
c2 = complex(input())

new_c1 = complex(c1.imag, c2.real)
new_c2 = complex(c2.imag, c1.real)

print(f"New first Complex number : ({new_c1.real:.0f}{'+' if new_c1.imag >= 0 else ''}{new_c1.imag:.0f}j)")
print(f"New first Complex number : ({new_c2.real:.0f}{'+' if new_c2.imag >= 0 else ''}{new_c2.imag:.0f}j)")

