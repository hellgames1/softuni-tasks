""""
Task 4 - number classification
"""
nums = [int(a) for a in input().split(", ")]
positives = [a for a in nums if a>=0]
negatives = [a for a in nums if a<0]
evens = [a for a in nums if a%2==0]
odds = [a for a in nums if a%2!=0]
print("Positive: ",end="")
print(*positives,sep=", ")
print("Negative: ",end="")
print(*negatives,sep=", ")
print("Even: ",end="")
print(*evens,sep=", ")
print("Odd: ",end="")
print(*odds,sep=", ")