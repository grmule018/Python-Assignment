import os
path = "F:/shubham/python/81_Py program to concatenate N strings..py"
if os.path.isdir(path):
    print("It is directory")
elif os.path.isfile(path):
    print("It is a normal file")
else:
    print("It is a special file")
