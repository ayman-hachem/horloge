from datetime import datetime, timedelta
import time
import keyboard

# Demander à l'utilisateur de spécifier l'heure pour l'alarme
heure_alarme_input = input("Entrez l'heure de l'alarme (format HH:MM) : ")
heure_alarme_specifique = datetime.strptime(heure_alarme_input, "%H:%M")

while True:
    # Vérifier si la touche 's' a été pressée
    if keyboard.is_pressed('s'):
        print("Arrêt du programme.")
        break
    
    # Obtenir l'heure actuelle
    heure_actuelle = datetime.now()
    heure_formatte = heure_actuelle.strftime("%H:%M:%S")
    print("Heure actuelle :", heure_formatte)

    # Vérifier si l'heure actuelle correspond à l'heure spécifique
    if heure_actuelle.time() >= heure_alarme_specifique.time():
        print("Alarme!!!")
        # Réinitialiser l'heure d'alarme pour le prochain jour
        heure_alarme_specifique += timedelta(days=1)

    # Attendez une seconde avant de mettre à jour l'heure
    time.sleep(1)
