""""
Task 8 - Vehicle
"""
class Vehicle:
    def __init__(self,typ,model,price,owner=None):
        self.typ = typ
        self.model = model
        self.price = price
        self.owner = owner
    def buy(self,money:int,owner:str):
        if money >= self.price:
            if self.owner is None:
                self.owner = owner
                return f"Successfully bought a {self.typ}. Change: {(money-self.price):.2f}"
            else:
                return "Car already sold"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        else:
            self.owner = None

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.typ} is on sale: {self.price}"
        else:
            return f"{self.model} {self.typ} is owned by: {self.owner}"