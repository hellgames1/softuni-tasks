""""
Task 6 - Even Numbers
"""
nums = [int(key) for key in input().split(", ")]
indices = [num for num in range(len(nums)) if nums[num]%2==0]
print(indices)