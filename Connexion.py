# Import et init
import csv
import hashlib
FICHIER = "utilisateurs.csv"
# Masqule mdp
def hash_password(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest() # Et steuplé j'ai galèré à trouver ça ne le change pas mais en gros le mot de passe est caché
# Main defe 
def connexion():
    compte_existant = input("Déjà un compte (o/n) : ").lower() # Demande si compte existant (lower = met en miniscule)
    if compte_existant == "n": # Si non
        # Création d'un compte
        pseudo = input("Entrer votre nom d'utilisateur : ")
        mot_de_passe = input("Entrer votre mot de passe : ")
        if len(mot_de_passe) <= 7: # Sécurité
            print("Mot de passe trop court (8 caractères minimum).")
            return connexion() # Récucu
        with open(FICHIER, "r", newline="", encoding="utf-8") as f:
            utilisateurs = list(csv.DictReader(f, delimiter=";")) # Init le pseudo pour le fichier
        if any(u["pseudo"] == pseudo for u in utilisateurs): # Si le pseudo existe déjà
            print("Ce pseudo existe déjà.")
            return connexion() # Récucu
        with open(FICHIER, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["pseudo", "mot_de_passe", "admin"],
                delimiter=";"
            ) # Infos
            writer.writerow({
                "pseudo": pseudo,
                "mot_de_passe": hash_password(mot_de_passe),
                "admin": "non" # Non par défaut
            }) # Met les infos dans le fichier
        print("Compte créé avec succès !") # Confirmation
    elif compte_existant == "o": # Si compte existant
        # Connexion
        pseudo = input("Entrer votre nom d'utilisateur : ")
        mot_de_passe = input("Entrer votre mot de passe : ")
        with open(FICHIER, "r", newline="", encoding="utf-8") as f:
            utilisateurs = csv.DictReader(f, delimiter=";") # Init
            for utilisateur in utilisateurs:
                if utilisateur["pseudo"] == pseudo: # Username check...
                    if utilisateur["mot_de_passe"] == hash_password(mot_de_passe): #...Puis mdp check
                        print("Connexion réussie !")
                        if utilisateur["admin"] == "oui":
                            print("Bienvenue administrateur !")
                        else:
                            print("Bienvenue", pseudo)
                        return # Random bullshit
                    else:
                        print("Mot de passe incorrect.")
                        return
                print("Pseudo incorrect.")
                return connexion()
    else:
        print("Réponse invalide.")
        return connexion() # Récucu
#connexion()