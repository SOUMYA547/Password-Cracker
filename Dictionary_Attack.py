import hashlib

hash_target = input("Enter hash here:")

with open("wordlist.txt") as file:
    for word in file:
        word = word.strip()
        word_hash = hashlib.sha256(word.encode()).hexdigest()

        if word_hash == hash_target:
            print("Password Found: ", word)
            exit()

    print("Password not found in dictionary")