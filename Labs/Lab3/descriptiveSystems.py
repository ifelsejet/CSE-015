from logic import TruthTable


tempList = []
tempList2 = []
boolean = 1
while boolean:
  prop1 = input('Enter a proposition: ')
  prop2 = input('Would you like to enter more (Y/N): ')
  tempList.append(prop1)
  if prop2 == 'N':
    boolean = 0

myTable = TruthTable(tempList)

print("Your program uses propositional variables " + str(myTable.vars) + ":")

for i in myTable.vars:
  propTemp = input("Enter meaning of " + str(i) + ": ")
  tempList2.append(propTemp)
for i in myTable.table:
  temp = 0
  for j in range(len(tempList)):
    if i[1][j] == 1:
      temp = temp + 1
  if(temp == len(tempList)):
    print("Your description is consistent when:")
    for j in range(len(tempList)):
      if(i[0][j]==0):
        print("It is not the case that "+str(tempList2[j]))
      if(i[0][j]==1):
        print("It is the case that "+str(tempList2[j]))
