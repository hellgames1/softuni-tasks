""""
Task 6 - Replace Repeating Chars
"""
aaa = list(input())
res = []
exp = 0
ind = 0
while ind < len(aaa):
    let = aaa[ind]
    if let != ">":
        if exp == 0:
            res.append(let)
        else:
            exp -= 1
    else:
        res.append(">")
        exp += int(aaa[ind+1])
    ind += 1

print("".join(res))