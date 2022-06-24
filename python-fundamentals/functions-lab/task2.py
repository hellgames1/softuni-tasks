""""
Task 2 - Grades
"""
def grade(num):
    if 2<=num<3:
        return "Fail"
    elif 3<=num<3.5:
        return "Poor"
    elif 3.5<=num<4.5:
        return "Good"
    elif 4.5<=num<5.5:
        return "Very Good"
    elif 5.5<=num<=6:
        return "Excellent"
print(grade(float(input())))