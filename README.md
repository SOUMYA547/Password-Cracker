# 🔐 Password Cracker (Learning Project)

This project demonstrates **offline password cracking techniques** for **educational and cybersecurity learning purposes only**.  
It helps understand why **weak passwords are insecure** and why **strong hashing practices are necessary**.

---

## 📌 Project Objective
- To demonstrate how **offline password hashes** can be cracked
- To understand **brute-force** and **dictionary attacks**
- To learn the importance of **secure password policies**

---

## ⚠️ Disclaimer
This project is intended solely for **educational purposes**.  
It works only on **offline hashes** and must **not** be used against real systems, accounts, or networks.

---

## 🛠️ Technologies Used
- Python 3
- hashlib module
- Wordlists (text files)

---

## 📂 Project Files Description

| File Name | Description |
|---------|------------|
| `Hash_Function_Target.py` | Generates SHA-256 hash of a given password |
| `Brute_Force_Attack.py` | Attempts to crack the hash using the brute-force method |
| `Dictionary_Attack.py` | Cracks hash using wordlist-based dictionary attack |
| `File_Password_Cracker.py` | Cracks password hashes from a file |
| `wordlist.txt` | Common password dictionary |
| `passlist.txt` | Additional password list |
| `test.zip` | Sample password-protected file (for learning) |
| `test1.txt` | Sample text file |

---

## 🔑 How It Works

### 1️⃣ Hash Generation
- A plaintext password is converted into a **SHA-256 hash**
- This simulates a leaked password database

### 2️⃣ Brute-Force Attack
- Tries all possible character combinations
- Effective only for **short and weak passwords**
- Very slow for long passwords

### 3️⃣ Dictionary Attack
- Uses a predefined list of common passwords
- Much faster than brute-force
- Exploits human password habits

### 4️⃣File Password Cracker

Uses a predefined password wordlist
- Attempts to unlock password-protected files (offline)
- Demonstrates why weak file passwords are insecure
- Works only on self-created test files
---
