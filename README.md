---
SAE15 Traitement des données   

<p align="center">
  <img src="https://file.diplomeo-static.com/file/00/00/01/44/14465.svg" alt="First Image" width="300" style="margin-right: 20px;" />
  <img src="https://www.hostblog.fr/wp-content/uploads/2021/06/dut-reseaux-telecommunication-840x400.jpg" alt="Second Image" width="300" style="margin-left: 20px;" />
</p>




 TP Projet TSANGUE Yohann-GRANVSIR-CLERC                                    
 
---
# Projet n°2 : aider un enseignant à faire le bilan  

En fin d’année il est demandé aux enseignants de préparer une fiche de service présentant le                    
 

bilan de leurs interventions réalisées pendant l’année. L’objectif de ce projet est d’afficher,
la liste des modules dans lesquels un enseignant donné est intervenu, en détaillant le nombre
d’heures de CM, TD et TP.  
## Cahier des charges :  
- le nom de l’enseignant doit être paramétrable;  
- les DS comptent comme un CM;  
- le résultat sera affiché :  
    - sous forme d’un tableau, au format csv ou xlsx ou pdf;  
    - ET sous forme d’un histogramme donnant pour chaque module le bilan CM/TD/TP (format libre, par exemple .png).  
---
### Etape 1 : pré-traitement  
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
### Etape 2 : traitement des données  
Le fichier [ADECal.csv](https://github.com/ytsangue/SAE105_Projet/blob/main/ADECal.csv)
 contenant les événements du fichier [ADECal.ics](https://github.com/ytsangue/SAE105_Projet/blob/main/ADECal.ics) sera traité en utilisant
Python, afin de répondre aux objectifs du sujet choisi.





<p align="center">
  Copyright &copy; 2024-present <a href="https://github.com/ytsangue/SAE105_Projet" target="_blank">SAE 15 </a>
</p>
