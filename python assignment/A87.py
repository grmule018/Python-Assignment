import os
os.chdir("E:/12121")
def get_file_size(path):
    if not os.path.isfile(path):
        raise TypeError("not file")
    return os.stat(path).st_size
print("The size of p1.txt is :",get_file_size("p1.txt"),"bytes")
