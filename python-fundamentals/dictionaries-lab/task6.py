""""
Task 6 - Odd Occurrences
"""
stri = input().split()
strs = {}
for st in stri:
    if st.lower() in strs.keys():
        strs[st.lower()] += 1
    else:
        strs[st.lower()] = 1
for st in strs:
    if strs[st] % 2 == 1:
        print(st,end=" ")
