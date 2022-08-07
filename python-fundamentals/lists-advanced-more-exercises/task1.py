""""
Task 1 - Social Distribution
"""
from sys import maxsize
population = list(map(int,input().split(", ")))
minw = int(input())
if sum(population) < minw * len(population):
    print("No equal distribution possible")
else:
    while True:
        poorest = (maxsize, -1)
        richest = (-maxsize, -1)
        for ind, person in enumerate(population):
            if person < poorest[0]:
                poorest = (person, ind)
            if person > richest[0]:
                richest = (person, ind)
        if poorest[0] < minw:
            diff = minw - poorest[0]
            population[poorest[1]] += diff
            population[richest[1]] -= diff
        else:
            break
    print(population)