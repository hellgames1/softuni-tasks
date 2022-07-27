""""
Task 8 - Decipher This!
"""
message = input().split()
output = []
for word in message:
    firstletter = ""
    wordfinished = ""
    for letter in word:
        if letter.isnumeric():
            firstletter += letter
        else:
            wordfinished += letter
    wordfinished = (wordfinished[::-1] + chr(int(firstletter)))[::-1]
    wordfinished = list(wordfinished)
    wordfinished[1], wordfinished[len(wordfinished)-1] = wordfinished[len(wordfinished)-1], wordfinished[1]
    output.append("".join(wordfinished))
print(*output,sep=" ")