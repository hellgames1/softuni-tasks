""""
Task 12 - Factorial Division
"""
num1 = int(input())
num2 = int(input())
def fact(number):
    product = number
    for i in range(number-1,0,-1):
        product = product*i
    return product
factorial_division = lambda a,b: fact(a)/fact(b)
print(f"{factorial_division(num1,num2):.2f}")