# #Return
    # def pr(n):
    #     return n*4
    # print(pr(5))

#recursion (function calls its self to preform the task)

# x=int(input("x:"))
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x* factorial(x-1))
# print(factorial(x))
    
y=int(input("y:"))
def sum(y):
    if y<=1:
        return 1
    else:
        return( y + sum(y-1))
print(sum(y))