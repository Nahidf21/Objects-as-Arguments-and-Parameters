class Fruets:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def sort_by(self):
        return self.price

    
lists=[
    Fruets("Mango",10),
    Fruets("Apple", 15),
    Fruets("Banana", 5)
    ]

for f in sorted(lists, key=Fruets.sort_by):

    print(f.name)