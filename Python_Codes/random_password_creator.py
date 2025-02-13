import secrets
import string

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

Alphabet = letters + digits + punctuation

size = int(input("Password Size: "))

arr = []

for i in range(size):
    arr.append(secrets.choice(Alphabet))

print("".join(arr))
print(len(arr))