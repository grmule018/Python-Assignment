def triplets(x,y,z):
    if x==y==z:
        return(x+y+z)*3
    else:
        return x+y+z
print(triplets(1,2,3))
print(triplets(3,3,3))
