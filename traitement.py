import csv
table=[]
with open('ADECal.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        table.append(row)

#suppression des \n
for chaine in table:
    chaine[3] = chaine[3].replace('\n',',')

#liste des modules par enseignant
modules = list()
prof = input("Entrez le nom d'un.e enseignant.e : ")
prof = prof.upper()
for element in table:
    if prof in element[3]:
        modules.append(element[0])
print(modules)