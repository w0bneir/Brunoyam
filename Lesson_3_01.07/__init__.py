# class Animal(object):
#     height = 0
#     weight = 0
#     color = ""
#     area = ""
#     def __init__(self,a,b,c,d):
#         self.height = a
#         self.weight = b
#         self.color = c
#         self.area = d
#         print("Я родился")
#     def __del__(self):
#         print("Я закончился")
#     def __str__(self):
#         return "Вот так"
#     def eat(self):
#         print("Eating")
#     def step(self):
#         print("Stepping")
# c1 = Animal(1,2,3,4)
# print(f"c1 {c1.height}, {c1.weight}, {c1.color}, {c1.area}")
# print(c1)
class Animal():
    def __init__(self, type, height, weight, habitat, domesticated):
        self.type = type
        self.height = height
        self.weight = weight
        self.habitat = habitat
        self.domesticated = domesticated
    def hab(self):
        if self.habitat == "carnivorous":
            return "Dont afraid herbivores"
        if self.habitat == "herbivore":
            return "Afraid carnivorouses"
    def dom(self):
        if self.domesticated == True:
            return "dependent on the person"
        else:
            return "dont dependent on the person"
cat = Animal("Cat", 23, 6, "carnivorous", True)
print(cat.hab())