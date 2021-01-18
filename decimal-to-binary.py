decimal = int(input("Give me a decimal number"))

b = []

while decimal/2 >= 0.5:
    if decimal%2 == 1:
        b.append('1')
        decimal = decimal/2 - 0.5
    elif decimal%2 == 0:
        b.append('0')
        decimal = decimal/2
    elif decimal/2 == 0.5:
        b.append('1')

binary_in_order = []
for i in range(len(b)):
    binary_in_order.append(b[-1-i])

print(binary_in_order)

