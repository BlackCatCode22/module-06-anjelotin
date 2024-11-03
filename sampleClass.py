class PartyAnimal:

    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("So far...", self.x)


an = PartyAnimal()

print("type is: ", type(an))
print("dir is: ", dir(an))
print("type of an.x is: ", type(an.x))
print("Type", type(an.party))

an.party()
an.party()
an.party()