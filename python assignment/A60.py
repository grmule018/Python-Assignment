from math import sqrt as sq
print("To calculate hypotenus of a triangle")
adj = float(input("Enter the adjacent side length:"))
opp = float(input("Enter the opposite side length:"))
hypotenus = sq(adj**2 + opp**2)
print(hypotenus)
