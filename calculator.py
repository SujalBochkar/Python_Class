#simple calculator
def add(x,y):
    return x+y 
def sub(x,y):
    return x-y 
def mul(x,y):
    return x*y 
def div(x,y):
    return x/y 

print("Select the opertaion that you want to perform")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divide")
 
choice = (input("choose 1/2/3/4:"))
n1 = float(input("Enter the first number:  "))
n2 = float(input("Enter the second number: "))

if choice == '1':
    print(add(n1,n2))
elif choice == '2':        
    print(sub(n1,n2))
elif choice == '3':
    print(mul(n1,n2))
elif choice == '4':
    print(div(n1,n2))
else :
    print("Enter Correct option")