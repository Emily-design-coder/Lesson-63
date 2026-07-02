print("Power Set and Bit Difference")

items = ["A", "B", "C"]
n = len(items)
total_subsets = 2 ** n

print("Masks:")
for mask in range(total_subsets):
    print(mask, bin(mask))

print("\nSubsets:")
for mask in range(total_subsets):
    subset = []
    for j in range(n):
        if mask & (1 << j):
            subset.append(items[j])
    print(subset)

def bit_difference(a, b):
    count = 0
    while a > 0 or b > 0:
        if (a & 1) != (b & 1):
            count += 1
        a >>= 1
        b >>= 1
    return count

print("\nBit Difference:", bit_difference(10, 7))
