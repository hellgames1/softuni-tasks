""""
Task 1 - Data Types
"""
d_type = input()
def action(dtype,inp):
    if dtype=="int":
        return str(int(inp)*2)
    elif dtype=="real":
        return f"{(float(inp)*1.5):.2f}"
    elif dtype=="string":
        return "$"+inp+"$"

print(action(d_type,input()))
