numberList = []
oddNums = []
for i in range(0, 10):
    num = int(input("Enter a number: "))
    numberList.append(num)

for num in numberList:
    if(num%2 != 0):
        oddNums.append(num)
if oddNums:
    print(max(oddNums)) #max returns max number in the list
else:
    print("No odd numbers were entered") 


