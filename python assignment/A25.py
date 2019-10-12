def chk_values(group,num):
    if num in group:
        return True
    return False
print(chk_values([1,5,8,3],3))
print(chk_values([1,5,8,3],-1))
