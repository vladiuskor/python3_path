squares = []
for value in range(1, 11):
    # Not a compact code bellow
    # square = value ** 2
    # squares.append(square)

    # More compact code
    squares.append(value ** 2)

print(squares)

second_squares = [value ** 2 for value in range(1, 11)]
print(second_squares)
