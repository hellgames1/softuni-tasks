""""
Task 7 - Group of 10s
"""
findgroup = lambda a: (a-1)//10+1
nums = list(map(int,input().split(", ")))
maxgroup = findgroup(max(nums))
groups=[]
for i in range(maxgroup):
    groups.append([])
for num in nums:
    groups[findgroup(num)-1].append(num)
for index, group in enumerate(groups):
    print(f"Group of {index+1}0's: ",end="")
    print(group)