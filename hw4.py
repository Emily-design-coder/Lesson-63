print("XOR Operations Assignment")

print("Step 2: XOR Identity and Equality")

a = 12
b = 12

print("a =", a)
print("b =", b)
print("a ^ a =", a ^ a)
print("a ^ 0 =", a ^ 0)

if (a ^ b) == 0:
    print("a and b are equal")
else:
    print("a and b are not equal")

print()

print("Step 3: XOR Cancellation")

numbers = [4, 7, 4, 9, 7]

result = 0
for num in numbers:
    result ^= num

print("List:", numbers)
print("Unique number after XOR cancellation:", result)

print()

print("Step 4: Find One Odd-Occurring Number")

numbers = [2, 3, 2, 4, 4, 5, 5]

odd = 0
for num in numbers:
    odd ^= num

print("List:", numbers)
print("Odd-occurring number:", odd)

print()

print("Step 5: XOR of Two Odd-Occurring Numbers")

numbers = [2, 3, 2, 4, 4, 5, 5, 7]

xor_of_two = 0
for num in numbers:
    xor_of_two ^= num

print("List:", numbers)
print("Combined XOR:", xor_of_two)

print()

print("Step 6: Split Using the Rightmost Set Bit")

rightmost_set_bit = xor_of_two & -xor_of_two

print("Rightmost set bit:", rightmost_set_bit)

group1 = []
group2 = []

for num in numbers:
    if num & rightmost_set_bit:
        group1.append(num)
    else:
        group2.append(num)

print("Group 1:", group1)
print("Group 2:", group2)

print()

print("Step 7: Identify Both Odd-Occurring Numbers")

odd1 = 0
odd2 = 0

for num in group1:
    odd1 ^= num

for num in group2:
    odd2 ^= num

print("First odd-occurring number:", odd1)
print("Second odd-occurring number:", odd2)

print()
