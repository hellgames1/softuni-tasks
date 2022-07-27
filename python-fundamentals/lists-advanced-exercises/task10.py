""""
Task 10 - Pokemon don't go
"""
pokemons = list(map(int,input().split()))
removed = []
while True:
    index = int(input())
    if index < 0:
        index = 0
        val = pokemons[0]
        removed.append(pokemons[0])
        pokemons[0] = pokemons[len(pokemons)-1]
    elif index > len(pokemons)-1:
        index = len(pokemons)-1
        val = pokemons[index]
        removed.append(pokemons[index])
        pokemons[index] = pokemons[0]
    else:
        val = pokemons[index]
        removed.append(pokemons[index])
        pokemons.pop(index)
    for index, pokemon in enumerate(pokemons):
        if pokemon <= val:
            pokemons[index] += val
        else:
            pokemons[index] -= val
    if len(pokemons) == 0:
        break
print(sum(removed))