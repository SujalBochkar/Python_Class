import random
print(random.random())

#slicing
b = "sujal bochkar"
print(b[3:-1])

# capalization
c="hello"
print(c.upper())

#replace
d="heelow"
print(d.replace("e","l"))

#concatenation
x="\"computer\""
y="engineering"
sum=x+" "+y 
print(sum)

# include
a=10
print(f"there are {a} items")

items=["pen","books",1,20]
print(items)
print(len(items))
print(type(items))

import random
randomlist=[]
for i in range (0,5):
    n=random.randint(1,10)
    randomlist.append(n)
print(randomlist)

