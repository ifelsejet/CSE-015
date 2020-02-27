from logic import TruthTable

tempList = []
boolean = 1
count = 0

while boolean:
    count = count + 1
    prop1 = input('Enter a proposition: ')
    prop2 = input('Would you like to enter more (Y/N): ')
    tempList.append(prop1)
    if prop2 == 'N':
        boolean = 0

myTable = TruthTable(tempList)

for i in myTable.table:
    temp = 0
    for j in range(len(tempList)):
        if i[1][j] == 1:
            temp = temp + 1
    if(temp == len(tempList)):
        boolean = 1

if boolean:
    print ("Your description is consistent.")
else:
    print ("Your description is not consistent.")
