dimensions = (200, 50)
# print(type(dimensions))
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 400
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 70)
print('\nModified dimensions:')

for dimension in dimensions:
    print(dimension)
print('\n')

# Ex.1 Sweden table
menu = ('pizza', 'pasta', 'sushi', 'borsh', 'steak')
for dish in menu:
    print(dish)

# menu[2] = 'udon' Impossible
menu = ('pizza', 'salad', 'kebab', 'borsh', 'steak')
for dish in menu:
    print(dish)
