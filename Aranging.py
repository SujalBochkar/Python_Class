numList = []

number = int(input("Please enter the length of the list"))
for i in range(1, number+1):
    value = int(input("Please enter the elements" %i))
    numList.append(value)

for i in range(number):
    for j in range (i+1 , number):
        if (numList[i] > numList[j]):
            temp = numList[i]
            numList[i] = numList[j]
            numList[j] = temp
print(numList)



