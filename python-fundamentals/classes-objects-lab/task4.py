""""
Task 4 - Zoo
"""
class Zoo:
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.animals = 0
    def add_animal(self,species,name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.animals += 1
    def get_info(self,species):
        if species == "mammal":
            print(f"Mammals in {self.name}: {', '.join(self.mammals)}")
        elif species == "fish":
            print(f"Fishes in {self.name}: {', '.join(self.fishes)}")
        elif species == "bird":
            print(f"Birds in {self.name}: {', '.join(self.birds)}")
        print(f"Total animals: {self.animals}")
zoo = Zoo(input())
count = int(input())
for i in range(count):
    command = list(input().split())
    zoo.add_animal(command[0],command[1])

zoo.get_info(input())