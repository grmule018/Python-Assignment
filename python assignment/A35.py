def chk_no_eql_to_5(x, y):
    if x == y or abs(x-y) == 5 or x + y == 5:
        return True
    else:
        return False
print(chk_no_eql_to_5(7, 2))
print(chk_no_eql_to_5(8, 2))
print(chk_no_eql_to_5(2, 2))
