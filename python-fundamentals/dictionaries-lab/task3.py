""""
Task 3 - Statistics
"""
dictionary = {}
while True:
    command = input()
    if command == "statistics":
        break
    com = command.split(": ")
    if com[0] in dictionary:
        dictionary[com[0]] += int(com[1])
    else:
        dictionary[com[0]] = int(com[1])
print("Products in stock:")
[print(f"- {product}: {quantity}") for (product, quantity) in dictionary.items()]
print(f"Total Products: {len(dictionary.keys())}\nTotal Quantity: {sum(dictionary.values())}")