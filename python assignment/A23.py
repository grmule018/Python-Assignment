def copy(str,n):
    length = 2
    if length > len(str):
        length = len(str)
    substr = str[:2]##Get first two char in spc
    result = ""
    for i in range(n):
        result = result + substr
    return result
print(copy("wxyz",2))
print(copy("s",4))
