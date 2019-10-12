def gcd(a, b):
    gcd = 1
    if a % b ==0:
        return b
    for x in range(int(b / 2), 0, -1):
        if a % x == 0 and b % x == 0:
            gcd = x
            break
    return gcd
print(gcd(12, 17))
print(gcd(4, 6))
