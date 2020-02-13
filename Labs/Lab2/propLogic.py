from logic import TruthTable
prop1 = input("Enter proposition 1: ")
prop2 = input("Enter proposition 2: ")

checker = None #Python has no booleans :(

myTable = TruthTable([prop1, prop2])

for result in myTable.table: #Compare elements in list
    if(result[1][1] != result[1][0]):
        checker = True

if(checker):
    print("The propositions are not equivalent")
else:
    print("The propositions are equivalent")
        

