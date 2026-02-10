class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name

p1 = Person("Alex")
p2 = Person("Tom")

print(p1.species)
print(p2.species)