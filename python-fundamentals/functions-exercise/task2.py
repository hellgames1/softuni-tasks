""""
Task 2 - Add and Subtract
"""
sum_numbers = lambda a,b: a+b
subtract = lambda c,d: c-d
add_and_subtract = lambda i,j,k: subtract(sum_numbers(i,j),k)
print(add_and_subtract(int(input()),int(input()),int(input())))