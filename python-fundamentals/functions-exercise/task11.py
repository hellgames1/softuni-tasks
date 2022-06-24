""""
Task 11 - Loading Bar
"""
value = int(input())
load_message = lambda a: f'{a}% [{("".join(["%" if x <= a//10 else "." for x in range(1,11)]))}]\nStill loading...' if a//10<10 else f"100% Complete!\n[%%%%%%%%%%]"
print(load_message(value))