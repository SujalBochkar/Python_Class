# Polymorphism
    # print(len("Sujal Bochkar"))
    # print(len([10,20,30]))

# def sum(x,y,z=0):
#     return x+y+z
# print(sum(1,9))
# print(sum(1,9,6))

# class India ():
#     def capital(self):
#         print("New Delhi is the capital of India")

#     def language(self):
#         print("Multiple languages are spoken in India")

# class USA():
#     def capital(self):
#         print("Washington DC")

#     def language(self):
#         print("Engilsh")

# obj1= India()
# obj2=USA()
# obj1.capital()
# obj1.language()
# obj2.capital()
# obj2.language()


class Bird:
    def Intro(self):
        print("This is a bird class")

    def flight(self):
        print("Birds fly")

class Parrot(Bird):
    def flight(self):
        print("Parrot can fly")

class Ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")

obj1 = Bird()
obj1.Intro()
obj1.flight()
print("\n")

obj2 = Parrot()
obj2.Intro()
obj2.flight()
print("\n")

obj3 = Ostrich()
obj3.Intro()
obj3.flight()
print("\n")

