import hashlib
password = input("Enter Password:")
hash_target = hashlib.sha256(password.encode()).hexdigest()
print("Target Hash: ", hash_target)