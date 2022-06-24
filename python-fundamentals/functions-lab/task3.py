""""
Task 3 - Calculations
"""
def calc(operator,first,second):
    ops = {"subtract" : "-",
           "add" : "+",
           "divide": "/",
           "multiply": "*"}
    exec("result=int("+first+ops[operator]+second+")",ops)
    return ops["result"]
print(calc(input(),input(),input()))