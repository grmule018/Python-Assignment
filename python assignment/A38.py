def test_data(x, y):
    formula = x * x + 2 * x * y + y * y
    print("({} + {}) ^ 2 = {}".format(x,y,formula))
test_data(4, 3)
