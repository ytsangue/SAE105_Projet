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

#nombre heures total par prof
heures = 0
prof = input("Entrez le nom d'un.e enseignant.e : ")
prof = prof.upper()

def calculer_duree(liste):
    format_date = "%Y-%m-%d %H:%M:%S%z"
    date_debut = liste[1]
    date_fin = liste[2]
    heures_debut, minutes_debut = map(int, date_debut.split()[1].split(':')[:2])
    heures_fin, minutes_fin = map(int, date_fin.split()[1].split(':')[:2])
    difference_heures = heures_fin - heures_debut
    difference_minutes = minutes_fin - minutes_debut
    duree_en_heures = difference_heures + difference_minutes / 60
    return duree_en_heures

def main():
    # Liste fournie avec les dates
    ma_liste = table

    # Calculer la durée
    duree_en_heures = calculer_duree(ma_liste)

    # Afficher le résultat
    print(f"La durée est de {duree_en_heures} heures.")
    return duree_en_heures

main()


'''for element in table:
    if prof in element[3]:
        heures = calculer_duree(element)
print("Nombre d'heures de ",prof," : ",heures)'''
