""""
Task 2 - Messaging
"""
nums = input().split(" ")
message = list(input())
indexes=[]
output=""
for num in nums:
    current=0
    for char in num:
        current+=int(char)
    indexes.append(current)
for index in indexes:
    counter=0
    for i in range(index):
        counter+=1
        if counter>=len(message):
            counter=0
    output+=message[counter]
    message.pop(counter)
print(output)