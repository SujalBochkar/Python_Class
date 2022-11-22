x = int(input("Enter the integer greater thean 1: "))
rev=0
while (x>0):
    remainder = x % 10
    rev = (rev*10) + remainder
    x=x//10
print(rev)