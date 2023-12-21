import csv
import re
import matplotlib.pyplot as plt

table = []
with open('ADECal.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)

# Suppression des \n
for chaine in table:
    chaine[3] = chaine[3].replace('\n', ',')

prof = input("Entrez le nom d'un.e enseignant.e : ")
prof = prof.upper()

def calcule_duree_prof(liste):
    format_date = "%Y-%m-%d %H:%M:%S%z"
    date_debut = liste[1]
    date_fin = liste[2]
    heures_debut, minutes_debut = map(int, date_debut.split()[1].split(':')[:2])
    heures_fin, minutes_fin = map(int, date_fin.split()[1].split(':')[:2])
    difference_heures = heures_fin - heures_debut
    difference_minutes = minutes_fin - minutes_debut
    duree_en_heures = difference_heures + difference_minutes / 60
    return duree_en_heures

ma_liste = table
module_heures = {}
heures_CM = 0
heures_TD = 0
heures_TP = 0

for element in table:
    if prof in element[3]:
        module_heures[element[0]]= module_heures.get(element[0],0) + calcule_duree_prof(element)
        if re.search("Amphi",element[4]) or re.search("DS",element[0]):
            heures_CM = int(heures_CM + calcule_duree_prof(element))
        elif re.search("Labo",element[4]):
            heures_TP = int(heures_TP + calcule_duree_prof(element))
        elif re.search("TD",element[4]):
            heures_TD = int(heures_TD + calcule_duree_prof(element))

print(module_heures)
print("Heures CM :",heures_CM)
print("Heures TD :",heures_TD)
print("Heures TP :",heures_TP)

modules = list(module_heures.keys())
heures = list(module_heures.values())

#Histogramme 
plt.bar(modules, heures)
plt.title("Bilan des heures par module")
plt.xlabel("Modules")
plt.ylabel("Nombre d\'heure")
plt.xticks(rotation=30, ha='right')
plt.grid()

#Creation du bilan dans un fichier csv 
with open('bilan_heures_par_module.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Module', 'Heures'])
    for module, heure in zip(modules, heures):
        writer.writerow([module, heure])
        
plt.show()
