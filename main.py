import csv

# Charger le catalogue
with open("catalogue_anime.csv", "r", encoding="utf-8-sig", newline="") as fichier:
    lecteur = list(csv.DictReader(fichier, delimiter=";"))

def afficher_info(nom):
    for i in range(len(lecteur)):
        if lecteur[i]['titre'].lower() == nom.lower():
            print(f"Titre : {lecteur[i]['titre']}\nGenre : {lecteur[i]['genre']}\nAuteur : {lecteur[i]['auteur']}"
                  f"\nnom_manga : {lecteur[i]['nom_manga']}\nsource_originale : {lecteur[i]['source_originale']}"
                  f"\nstatut : {lecteur[i]['statut']}\nnb_episode : {lecteur[i]['nb_episode']}"
                  f"\nnb_episode_total : {lecteur[i]['nb_episode_total']}\naffiche_url : {lecteur[i]['affiche_url']}"
                  f"\naffiche_html : {lecteur[i]['affiche_html']}\nlien_source : {lecteur[i]['lien_source']}\nmal_id : {lecteur[i]['mal_id']}"
                  f"\nnb_notes : {lecteur[i]['nb_notes']}\nmoy_note : {lecteur[i]['moy_note']}\nnb_commentaires : {lecteur[i]['nb_commentaires']}")

print(lecteur[2]['commentaires'][0]["pseudo"])