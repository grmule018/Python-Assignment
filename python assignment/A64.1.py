import os.path,time
os.chdir("E:/Ganesh.py")
print("Last modified:",time.ctime(os.path.getmtime("abc.txt")))
print("Created:",time.ctime(os.path.getctime("abc.txt")))
