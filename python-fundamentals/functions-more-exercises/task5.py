""""
Task 5 - Multiplication Sign
"""
ints=[int(input()),int(input()),int(input())]
if 0 in ints:
    print("zero")
else:
    negative = lambda a: True if a<0 else False
    negative_amount = lambda a: len(list(filter(negative,a)))
    find_sign = lambda a: "negative" if negative_amount(a)%2!=0 else "positive"
    print(find_sign(ints))
