# TP Projet SAE15 Traitement des donnée                                   

 Le projet de SAE15 consiste à analyser le fichier [ADECal.ics](https://github.com/ytsangue/SAE105_Projet/blob/main/ADECal.ics) 
 (disponible sur [Plubel](https://plubel-prod.u-bourgogne.fr/course/view.php?id=5152)) extrait de ADE et contenant l’intégralité des cours organisés l’année dernière dans le département
R&T de l’IUT, avec un cahier des charges spécifique. Ce cahier des charge est indiqué dans la description de chaque sujet de projet dans les pages suivantes.
La réalisation du projet comporte plusieurs étapes :  

## Etape 1 : choix du sujet
### Projet n°2 : aider un enseignant à faire le bilan  
   
En fin d’année il est demandé aux enseignants de préparer une fiche de service présentant le                    
bilan de leurs interventions réalisées pendant l’année. L’objectif de ce projet est d’afficher,
la liste des modules dans lesquels un enseignant donné est intervenu, en détaillant le nombre
d’heures de CM, TD et TP.  
   
#### Cahier des charges :  
   
   - le nom de l’enseignant doit être paramétrable;  
   - les DS comptent comme un CM;  
   - le résultat sera affiché :  
       - sous forme d’un tableau, au format csv ou xlsx ou pdf;  
       - ET sous forme d’un histogramme donnant pour chaque module le bilan CM/TD/TP (format libre, par exemple .png).  

## Etape 2 : pré-traitement  

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

## Etape 3 : traitement des données  

Le fichier [ADECal.csv](https://github.com/ytsangue/SAE105_Projet/blob/main/ADECal.csv)
 contenant les événements du fichier [ADECal.ics](https://github.com/ytsangue/SAE105_Projet/blob/main/ADECal.ics) sera traité en utilisant
Python, afin de répondre aux objectifs du sujet choisi.

<p align="right">
   <img src="https://www.hostblog.fr/wp-content/uploads/2021/06/dut-reseaux-telecommunication-840x400.jpg" width="300"" />
</p>

<p align="center">
  Copyright &copy; 2024-present <a href="https://github.com/ytsangue/SAE105_Projet" target="_blank">SAE 15 </a>
</p>
