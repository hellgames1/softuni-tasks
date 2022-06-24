""""
Task 4 - Odd and Even Sum
"""
digits = [int(x) for x in list(input())]
odd_even_sum = lambda a: f"Odd sum = {sum([x for x in a if x%2!=0])}, Even sum = {sum([x for x in a if x%2==0])}"
print(odd_even_sum(digits))