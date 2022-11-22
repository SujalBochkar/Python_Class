# #what is value of a
# a=int (input("what is value of a?"))
# if a >=90:
#     print("exellent")
# elif a < 90 and a > 80:
#     print("good")
# else:
#     print("improve")


# a =int(input("Enter a number to check odd or even: "))
# if a%2 == 0:
#     print("Its an even number")
# else :
#     print("Its an odd number")

# a = int(input("Enter a number to check its prime or not: "))
# count = 0
# for i in range(2,a):
#     if a%i == 0 :
#         count = count + 1
# if count == 0 :
#     print("Its a prime number")
# else :
#     print("Its a not a prime number")

# a = str(input())
# print(a[: : -1])
    

a = (input())
b = 0
for i in a :
    b = b + (int(i)**3)
    print(b)
if b==a:
    print("Its an amstrong number")
else: 
    print("Its not an amstrong number")


