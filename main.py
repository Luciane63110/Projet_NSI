'''
Imports
'''
import sqlite3 
from pathlib import Path
'''
Initialise les fichiers SQL
'''
def main():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor() #Execute les requêtes SQL (cursor.execute)
    base_dir = Path(__file__).parent #Initialise le chemin d'accès
    sql_files = [
        base_dir / "anime_data" / "anime.sql", #Chemin complet : chemin d'accès -> dossier -> fichier
        base_dir / "users_data" / "users.sql"  #Même chose 
    ] #Chemin d'accès comple pour les fichiers SQL
    conn.commit()
    conn.close()
if __name__ == "__main__":
    main()

def create_user():
  username = input("Choisissez votre nom d'utilisateur : ")
  psw = input("Choisissez votre mot de passe : ")
  if len(username) > 20 or len(psw) > 20:
    username, psw = None, None
    print("20 caractères maximum pour le pseudo et les mot de passe")
