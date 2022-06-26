""""
Task 3 - Word Filter
"""
filter_evenlength = lambda x: [a for a in x if len(a)%2==0]
words = input().split(" ")
print(*filter_evenlength(words),sep="\n")