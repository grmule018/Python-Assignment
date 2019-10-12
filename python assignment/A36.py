def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
           raise TypeError("Oops! Enter Only Integer Type")
    else:
           return a + b
print(add_numbers(10, 20))

