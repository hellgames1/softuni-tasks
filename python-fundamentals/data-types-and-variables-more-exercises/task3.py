""""
Task 3 - Decrypting Messages
"""
key = int(input())
count = int(input())
new = ""
for i in range(count):
    letter = input()
    new += chr(ord(letter) + key)
print(new)