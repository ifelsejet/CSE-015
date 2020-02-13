from logic import TruthTable
myTable = TruthTable(['p and q']) #Error Here
myTable.display()
myTable2 = TruthTable(['q and p']) #Error Here

print(myTable.table)
print(myTable2.table)
