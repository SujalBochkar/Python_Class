# inheritance
# class Person:
#     def __init__(self,name,age) :
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name,self.age)

# class Employees(Person):
#     pass

# a = Employees("Sujal","20")
# a.display()

class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

class Employees(Person):
    def __init__(self,name,age,year) :
        super().__init__(name,age) 
        self.year = year
