motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
motorcycles.append('ducati')
print(motorcycles)

next_motorcycles = []
print(next_motorcycles)
next_motorcycles.append('honda')
next_motorcycles.append('yamaha')
next_motorcycles.append('suzuki')
print(next_motorcycles)

next_motorcycles.insert(0, 'ducati')
print(next_motorcycles)

del next_motorcycles[0]
print(next_motorcycles)
del next_motorcycles[1]
print(next_motorcycles)

one_more_motorcycles = ['honda', 'yamaha', 'suzuki']
print(one_more_motorcycles)

popped_motorcycle = one_more_motorcycles.pop()
print(one_more_motorcycles)
print(popped_motorcycle)

one_more_motorcycles.append('ducati')
one_more_motorcycles.append('harley')
print(one_more_motorcycles)
one_more_motorcycles.remove('yamaha')
print(one_more_motorcycles)