import glob
import os
os.chdir("E:/12121")
files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))
