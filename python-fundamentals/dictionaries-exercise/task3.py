""""
Task 3 - Capitals
"""

dicti={a:b for a,b in zip(input().split(", "),input().split(", "))}
for let,num in dicti.items():
    print(f"{let} -> {num}")