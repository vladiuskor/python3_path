# Ex.1 Count to 20
for value in range(1, 21):
    print(value)

print('\n')

# Ex.2 Cont to 1_000_000
# for value in range(1, 1000001):
#     print(value)

# Ex.3 Sum 1 000 000 numbers
# mill_list = []
# for value in range(1, 1000001):
#     mill_list.append(value)
#
# print(min(mill_list))
# print(max(mill_list))
# print(sum(mill_list))

# Ex.4 Odd numbers
for value in range(1, 21, 2):
    print(value)

print('\n')

# Ex.5  Print the numbers from 1 to 20 that are divisible by 3.
for value in range(3, 30, 3):
    print(value)

print('\n')

# Ex.6 Cube
print('Cube')
for value in range(1, 11):
    print(value ** 3)

# Ex.7 Cube list
cube_list = []
for value in range(1, 11):
    cube_value = value ** 3
    cube_list.append(cube_value)

print(cube_list)