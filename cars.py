cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)

# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

print("\nHere is sorted list")
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

print(f"\n *--------------------* \n")

cars.reverse()
print(cars)
cars.reverse()
print(cars)

print(cars[len(cars) - 1])
