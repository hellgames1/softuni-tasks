""""
Task 5 - Legendary Farming
"""
inventory={"shards":0,"fragments":0,"motes":0}
done=False
while not done:
    command_list = input().split()
    for i in range(0,len(command_list),2):
        itemtype=command_list[i+1].lower()
        if itemtype in inventory.keys():
            inventory[itemtype]+=int(command_list[i])
        else:
            inventory[itemtype]=int(command_list[i])
        if inventory["shards"]>=250:
            print("Shadowmourne obtained!")
            inventory["shards"]-=250
            done=True
            break
        if inventory["fragments"]>=250:
            print("Valanyr obtained!")
            inventory["fragments"]-=250
            done=True
            break
        if inventory["motes"]>=250:
            print("Dragonwrath obtained!")
            inventory["motes"]-=250
            done=True
            break
for item,quant in inventory.items():
    print(f"{item}: {quant}")