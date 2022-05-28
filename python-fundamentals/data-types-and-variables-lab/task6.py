""""
Task 6 - Next Happy Year
"""
year = int(input())
while True:
    year += 1
    nums = [0,0,0,0,0,0,0,0,0,0]
    isHappy = True
    for char in str(year):
        if nums[int(char)] == 0:
            nums[int(char)] = 1
        else:
            isHappy = False
            break
    if isHappy:
        print(year)
        break