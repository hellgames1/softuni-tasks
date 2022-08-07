""""
Task 2 - A Miner Task
"""
dicti={}
while True:
    command = input()
    if command=="stop":
        break
    quant = int(input())
    if command in dicti.keys():
        dicti[command] += quant
    else:
        dicti[command] = quant
for let,num in dicti.items():
    print(f"{let} -> {num}")