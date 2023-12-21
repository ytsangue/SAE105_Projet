def calculer_duree(date_debut, date_fin):
    """
    Calcule la durée en heures entre deux dates.
    """
    format_date = "%Y-%m-%d %H:%M:%S%z"
    
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
    # Les dates à partir de la liste fournie
    date_debut = '2021-09-22 12:00:00+00:00'
    date_fin = '2021-09-22 14:00:00+00:00'

    # Calculer la durée
    duree_en_heures = calculer_duree(date_debut, date_fin)

    # Afficher le résultat
    print(f"La durée est de {duree_en_heures} heures.")

if __name__ == "__main__":
    main()
