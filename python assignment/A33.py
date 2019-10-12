def three_values(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(three_values(3, 1, 3))
print(three_values(2, 4, 6))
