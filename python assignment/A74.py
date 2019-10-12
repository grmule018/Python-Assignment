import hashlib
my_string = input("Enter any string to hash: ")
hash_object = hashlib.md5(my_string.encode())
print(hash_object)
