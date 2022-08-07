""""
Task 4 - Caesar Cipher
"""
text = input()
new = []
for letter in text:
    new.append(chr(ord(letter)+3))
print("".join(new))