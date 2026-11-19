import csv

# Charger le catalogue
with open("catalogue_anime.csv", "r", encoding="utf-8-sig", newline="") as fichier:
    lecteur = list(csv.DictReader(fichier, delimiter=";"))

def afficher_info(nom):
    for i in range(len(lecteur)):
        if lecteur[i]['titre'].lower() == nom.lower():
            print(f"Titre : {lecteur[i]['titre']}\nGenre : {lecteur[i]['genre']}\nAuteur : {lecteur[i]['auteur']}\nnom_manga : {lecteur[i]['nom_manga']}\nsource_originale : {lecteur[i]['source_originale']}\nsource_originale : {lecteur[i]['source_originale']}\nstatut : {lecteur[i]['statut']}\nnb_episode : {lecteur[i]['nb_episode']}\nnb_episode_total : {lecteur[i]['nb_episode_total']}\nsaisons : {lecteur[i]['saisons']}\affiche_url : {lecteur[i]['affiche_url']}\naffiche_html : {lecteur[i]['affiche_html']}")
afficher_info("Mushoku Tensei")