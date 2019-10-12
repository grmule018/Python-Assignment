import os.path,time
os.chdir("F:/shubham")
print("Last modified:",time.ctime(os.path.getmtime("Ganesh.txt")))
print("Created:",time.ctime(os.path.getctime("Ganesh.txt")))
