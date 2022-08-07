""""
Task 1 - Count Chars in a String
"""
dicti = {}
for let in input():
    if let!=" ":
        if let in dicti.keys():
            dicti[let]+=1
        else:
            dicti[let]=1
for let,num in dicti.items():
    print(f"{let} -> {num}")