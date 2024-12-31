import mysql.connector
from mysql.connector import Error

# Configuration de la connexion à la base de données
config = {
    'host': 'fdb1029.awardspace.net',  # Remplacez par l'hôte de votre serveur
    'user': '4565581_hacking',         # Remplacez par votre nom d'utilisateur
    'password': 'hackerforever2610',   # Remplacez par votre mot de passe
    'database': '4565581_hacking'      # Remplacez par le nom de votre base de données
}

try:
    # Essayer de se connecter à la base de données
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Connecté avec succès à la base de données !")
        # Vous pouvez afficher des informations supplémentaires si nécessaire :
        db_info = connection.get_server_info()
        print(f"Version du serveur MySQL : {db_info}")

except Error as e:
    print(f"Erreur lors de la connexion : {e}")

finally:
    # Assurez-vous de fermer la connexion si elle a été établie
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connexion à la base de données fermée.")

