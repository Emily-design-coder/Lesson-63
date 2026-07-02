print("=== Bitwise Operations ===")

a, b = 5, 8
print("Before:", a, b)
a = a + b
b = a - b
a = a - b
print("After:", a, b)

x, y = 10, 20
x ^= y
y ^= x
x ^= y
print("XOR Swap:", x, y)

n = 6
print("n << 1 =", n << 1)
print("n << 2 =", n << 2)

a, b = -5, 8
print("Different signs:", (a ^ b) < 0)

dividend, divisor = 17, 5
quotient = 0

while dividend >= divisor:
    dividend -= divisor
    quotient += 1

print("Quotient:", quotient)
print("Remainder:", dividend)