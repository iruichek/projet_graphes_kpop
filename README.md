# projet_graphes_kpop
🎵 Réseau Social K-pop
Une application web interactive pour explorer les relations entre artistes, groupes et agences K-pop, modélisées sous forme de graphe.

📌 Description
Ce projet représente un réseau social K-pop en utilisant la théorie des graphes. Il permet de visualiser et d'analyser les connexions entre artistes (collaborations, appartenance à un groupe, gestion par une agence) via une interface web Flask.

🧠 Type de graphe utilisé
Graphe non orienté (nx.Graph)
Les relations sont symétriques : si Jungkook collabore avec Jimin, Jimin collabore aussi avec Jungkook. Il n'y a pas de direction dans les arêtes.
Graphe hétérogène (multi-types de nœuds)
Le graphe contient 4 types de nœuds distincts :
TypeExemplesRôlegroupeBTS, BLACKPINKRelie une agence à ses membresartisteJungkook, JennieNœud central, impliqué dans les collaborationsagenceHYBE, SM EntertainmentNœud hiérarchique supérieurartiste_externeIU, ZicoArtiste hors groupe principal
Arêtes typées (attribut relation)
Chaque arête possède un attribut relation qui précise sa nature :

membre_de — entre un artiste et son groupe
manage — entre une agence et un groupe
collaboration — entre deux artistes ayant travaillé ensemble


📐 Concepts de théorie des graphes appliqués
ConceptFonctionDescriptionVoisinage filtréconnexions_directes()Retourne les voisins liés uniquement par collaborationVoisins communsamis_en_commun()Intersection des voisins de deux artistesPlus court chemin (BFS)distance_entre()nx.shortest_path_length() — degrés de séparationCentralité par degréartistes_les_plus_connectes()G.degree() — les hubs du réseauDisposition force-dirigéeRoute /graphnx.spring_layout() — visualisation matplotlib

🌐 Fonctionnement du site
Route GET / POST /
Page principale avec deux formulaires d'analyse :

Analyse individuelle : sélectionner un artiste → obtenir la liste de ses collaborations directes
Analyse comparative : choisir deux artistes → obtenir leurs amis en commun + leur distance dans le réseau

Route GET /graph
Affiche une visualisation du graphe complet via matplotlib avec un layout spring_layout.

📁 Structure du projet
projet-kpop/
├── app.py          # Serveur Flask + construction du graphe + routes
├── graphe.py       # Module autonome d'analyse du graphe
├── data.py         # Données : groupes, agences, collaborations, artistes_externes
└── templates/
    └── index.html  # Interface web (Jinja2)

🚀 Installation et lancement
bash# Installer les dépendances
pip install flask networkx matplotlib

# Lancer l'application web
python app.py

# Tester le module graphe seul
python graphe.py
Ouvrir dans un navigateur : http://127.0.0.1:5000

🛠️ Technologies utilisées

Python 3
Flask — serveur web
NetworkX — manipulation et analyse de graphes
Matplotlib — visualisation
