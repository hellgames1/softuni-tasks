""""
Task 4 - Josephus Permutation
"""
people = input().split(" ")
k = int(input())
counter=1
index=0
print("[",end="")
output=""
while True:
    if counter == k:
        output+=people[index]+","
        people.pop(index)
        index-=1
        counter=0
    counter+=1
    index+=1
    if len(people)==0:
        break
    if index==len(people):
        index=0
print(output[:-1]+"]")