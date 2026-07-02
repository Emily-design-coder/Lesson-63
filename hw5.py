print("Bitwise Operations")

n = 16
print("n =", bin(n))
print("n-1 =", bin(n - 1))
print("n & (n-1) =", bin(n & (n - 1)))

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

def is_power_of_4(n):
    if not is_power_of_2(n):
        return False
    pos = 0
    while n > 1:
        n >>= 1
        pos += 1
    return pos % 2 == 0

def is_power_of_8(n):
    if not is_power_of_2(n):
        return False
    pos = 0
    while n > 1:
        n >>= 1
        pos += 1
    return pos % 3 == 0

def binary_power(base, exp):
    ans = 1
    while exp:
        if exp & 1:
            ans *= base
        base *= base
        exp >>= 1
    return ans

print("Power of 2:", is_power_of_2(16))
print("Power of 4:", is_power_of_4(16))
print("Power of 8:", is_power_of_8(64))
print("3^5 =", binary_power(3, 5))