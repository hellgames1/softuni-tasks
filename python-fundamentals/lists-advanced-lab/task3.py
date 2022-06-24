""""
Task 3 - To-do List
"""
ordered_list = [""]*10
while True:
    command = input()
    if command == "End":
        break
    com = command.split("-")
    ordered_list[int(com[0])-1]=com[1]
final_list = [x for x in ordered_list if x!=""]
print(final_list)