secret_code = 10
access_key = 6

def bits(n):
    return format(n, "04b")

print("Secret Code:", secret_code, "Binary:", bits(secret_code))
print("Access Key :", access_key, "Binary:", bits(access_key))

print("\nAND (&)")
print(secret_code & access_key, bits(secret_code & access_key))

print("\nOR (|)")
print(secret_code | access_key, bits(secret_code | access_key))

print("\nNOT (~)")
not_secret = (~secret_code) & 0b1111
print(not_secret, bits(not_secret))

print("\nXOR (^)")
print(secret_code ^ access_key, bits(secret_code ^ access_key))

print("\nLeft Shift (<< 1)")
print(secret_code << 1, format(secret_code << 1, "05b"))

print("\nRight Shift (>> 1)")
print(secret_code >> 1, bits(secret_code >> 1))

toggle = secret_code ^ 1
print("\nToggle Last Bit:", toggle)

if toggle == secret_code - 1:
    print(secret_code, "is Odd")
else:
    print(secret_code, "is Even")

print("\nNumber of 1 bits:", secret_code.bit_count())

print("\nProgram completed successfully!")