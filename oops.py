# object oriented programming
# Abstraction   removing or hiding then extra data
# Encapsulation  bring all under the same roof
# polymorphism   multi tasking
# Inheritence   aquring the property from the defined ones
# 1 class   
# 2 object
 
#! class defination
# class car:
#     h = 10
# maruti=car() object creation
# print(maruti.h)  passing value

# init helps the initialize
# object attribute 
# 1.and is called everytime an obeject created form ia class by using self keyword you can easily 
# 2. by using self keyword you can easily acces all the objects defined within the class including function


# class student:
#     def __init__(st, name, reg):  #(self) - st
#         st.name = name
#         st.reg = reg
# obj = student("Sujal", 12217305)
# print(obj.name)
# print(obj.reg)

class student:
    def __init__(st, name, reg):  #(self) - st
        st.name = name
        st.reg = reg

    def pr(self):
        print("Hello my name ",self.name)

obj = student("Sujal", 12217305)
obj.pr()