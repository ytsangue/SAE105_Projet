def calculer_duree(liste):
    """
    Calcule la durée en heures entre deux dates dans une liste.
    """
    format_date = "%Y-%m-%d %H:%M:%S%z"
    
    # Extraire les dates de début et de fin de la liste
    date_debut = liste[1]
    date_fin = liste[0]

    # Extraire les heures et les minutes des dates de début et de fin
    heures_debut, minutes_debut = map(int, date_debut.split()[1].split(':')[:2])
    heures_fin, minutes_fin = map(int, date_fin.split()[1].split(':')[:2])

    # Calculer la différence en heures et minutes
    difference_heures = heures_fin - heures_debut
    difference_minutes = minutes_fin - minutes_debut

    # Convertir la différence en heures
    duree_en_heures = difference_heures + difference_minutes / 60

    return duree_en_heures

def main():
    # Liste fournie avec les dates
    ma_liste = ['Réseaux opérateurs', '2021-09-22 12:00:00+00:00', '2021-09-22 14:00:00+00:00', 'RT2App\nRT2Hamming\nRT2Dijkstra\nDEJUSSIEU JEAN LOUIS\n(Exported :05/01/2022 11:04)', 'RT-Amphi,RT-Salle-TD4']

    # Calculer la durée
    duree_en_heures = calculer_duree(ma_liste)

    # Afficher le résultat
    print(f"La durée est de {duree_en_heures} heures.")

if __name__ == "__main__":
    main()
