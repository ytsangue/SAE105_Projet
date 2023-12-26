# Projet n°2 : aider un enseignant à faire le bilan

En fin d’année il est demandé aux enseignants de préparer une fiche de service présentant le
bilan de leurs interventions réalisées pendant l’année. L’objectif de ce projet est d’afficher,
la liste des modules dans lesquels un enseignant donné est intervenu, en détaillant le nombre
d’heures de CM, TD et TP.  
### Cahier des charges :  
- le nom de l’enseignant doit être paramétrable;  
- les DS comptent comme un CM;  
- le résultat sera affiché :  
    - sous forme d’un tableau, au format csv ou xlsx ou pdf;  
    - ET sous forme d’un histogramme donnant pour chaque module le bilan CM/TD/TP (format libre, par exemple .png).  

Etape 2 : pré-traitement  
Le fichier [ADECal.ics](https://github.com/ytsangue/SAE105_Projet/blob/main/ADECal.ics) devra subir un pré-traitement pour être converti au format [ADECal.csv](https://github.com/ytsangue/SAE105_Projet/blob/main/ADECal.csv)


```python
from csv_ical import Convert

convert = Convert()
convert.ICS_FILE_LOCATION = 'ADECal.ics'
convert.CSV_FILE_LOCATION = 'ADECal.csv'

convert.read_ical(convert.ICS_FILE_LOCATION)

convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)
```
