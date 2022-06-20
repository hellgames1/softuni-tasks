""""
Task 8 - Seize the Fire
"""
inp = input().split("#")
fires=[]
effort=0
water = int(input())
total_fire=0
for fire in inp:
    temp = fire.split(" = ")
    fires.append([temp[0],int(temp[1])])
print("Cells:")
for fire in fires:
    if (fire[0]=="High" and 81 <= fire[1] <= 125) or (fire[0]=="Medium" and 51 <= fire[1] <= 80) or (fire[0]=="Low" and 1 <= fire[1] <= 50):
        if water >= fire[1]:
            water-=fire[1]
            total_fire+=fire[1]
            effort += fire[1]*0.25
            print(f" - {fire[1]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")