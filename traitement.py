import csv
import re
import matplotlib.pyplot as plt

table = []
with open('ADECal/ADECal.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for ligne in reader:
        table.append(ligne)

# Suppression des \n
for chaine in table:
    chaine[3] = chaine[3].replace('\n', ',')

prof = input("Entrez le nom d'un enseignant : ")
prof = prof.upper()

def calcule_duree_prof(t: list) -> float:
    """
    Calcule la durée en heures d'un cours à partir des données d'une ligne du fichier CSV.

    Parameters:
        t (list): Liste contenant les données d'une ligne du fichier CSV.

    Returns:
        float: Durée du cours en heures.
    """
    format_date = "%Y-%m-%d %H:%M:%S%z"
    date_debut = t[1]
    date_fin = t[2]
    heures_debut, minutes_debut = map(int, date_debut.split()[1].split(':')[:2])
    heures_fin, minutes_fin = map(int, date_fin.split()[1].split(':')[:2])
    difference_heures = heures_fin - heures_debut
    difference_minutes = minutes_fin - minutes_debut
    duree_en_heures = difference_heures + difference_minutes / 60
    return duree_en_heures

def calculer_heures_module(table: list, prof: str)-> tuple:
     """
    Calcule le total d'heures par type de cours (CM, TD, TP) et génère un dictionnaire contenant les heures par module.

    Parameters:
        table (List[List[str]]): Liste contenant les données du fichier CSV.
        prof (str): Nom de l'enseignant.

    Returns:
        Tuple[dict, float, float, float]: Un tuple contenant le dictionnaire des heures par module,
        le total d'heures de CM, le total d'heures de TD, et le total d'heures de TP.
    """
    module_heures = {}
    heures_CM = 0
    heures_TD = 0
    heures_TP = 0

    for element in table:
        if prof in element[3]:
            module_heures[element[0]]= module_heures.get(element[0],0) + calcule_duree_prof(element)
            if re.search("Amphi",element[4]) or re.search("DS",element[0]):
                heures_CM += calcule_duree_prof(element)
            elif re.search("Labo",element[4]):
                heures_TP += calcule_duree_prof(element)
            elif re.search("TD",element[4]) or re.search("CAO",element[4]):
                heures_TD += calcule_duree_prof(element)

    return module_heures, heures_CM, heures_TD, heures_TP

resultats = calculer_heures_module(table, prof)

heures_ = {'Heures Total de CM': resultats[1], 'Heures Total de TD': resultats[2], 'Heures Total de TP': resultats[3]}

Different_Heures = list(heures_.keys())
Nombre_heures = list(heures_.values())

modules = list(resultats[0].keys())
heures = list(resultats[0].values())

#Histogramme 
plt.bar(modules, heures)
plt.title("Bilan des heures par module")
plt.xlabel("Modules")
plt.ylabel("Nombre d\'heure")
plt.xticks(rotation=30, ha='right')
plt.grid()
plt.show()

#Creation du bilan dans un fichier csv 
with open('bilan_heures_combined.csv', 'w', newline='') as csvfile:
    fieldnames = ['Module', 'Heures']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    # Écriture des données du premier dictionnaire
    for module, heures in resultats[0].items():
        writer.writerow({'Module': module, 'Heures': heures})
    # Écriture d'une ligne vide
    writer.writerow({})
    # Écriture des données du deuxième dictionnaire
    for module, heures in heures_.items():
        writer.writerow({'Module': module, 'Heures': heures})
