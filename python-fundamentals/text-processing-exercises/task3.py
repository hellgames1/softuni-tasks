""""
Task 3 - Extract File
"""
path = input().split("\\")
file = path[len(path)-1].split(".")
print(f"File name: {file[0]}\nFile extension: {file[1]}")