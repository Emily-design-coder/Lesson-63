switch_value = 45

def show_bits(num):
    return bin(num)[2:]

binary = show_bits(switch_value)

on_switches = binary.count("1")
off_switches = binary.count("0")

temp = switch_value
count = 0

while temp > 0:
    if temp & 1:
        count += 1
    temp = temp >> 1

temp = switch_value
position = 0

while temp > 0:
    if temp & 1:
        break
    temp = temp >> 1
    position += 1

print("Bit Masks:")
for i in range(len(binary)):
    mask = 1 << i
    print("Position", i, "=", show_bits(mask))

print("\nSwitch Status:")
for i in range(len(binary)):
    mask = 1 << i
    if switch_value & mask:
        print("Switch", i, "is ON")
    else:
        print("Switch", i, "is OFF")

print("\nFinal Summary")
print("Switch Value:", switch_value)
print("Binary:", binary)
print("ON Switches:", on_switches)
print("OFF Switches:", off_switches)
print("Bitwise Count:", count)
print("First ON Switch Position:", position)