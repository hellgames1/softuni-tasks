""""
Task 2 - Take/Skip Rope
"""
stri = input()
nums = []
takelist = []
skiplist = []
nonums = []
for ind, letter in enumerate(stri):
    if letter.isnumeric():
        nums.append(int(letter))
    else:
        nonums.append(letter)
for ind, num in enumerate(nums):
    if ind % 2 == 0:
        takelist.append(int(num))
    else:
        skiplist.append(int(num))
nonums = "".join(nonums)
result=""
for i in range(len(takelist)):
    result += nonums[:takelist[i]]
    nonums = nonums[takelist[i]+skiplist[i]:]
print(result)