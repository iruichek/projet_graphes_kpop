# 🎵 Réseau Social K-pop

Une application web interactive pour explorer les relations entre artistes, groupes et agences K-pop, modélisées sous forme de **graphe**.

---

## 📌 Description

Ce projet représente un **réseau social K-pop** en utilisant la théorie des graphes. Il permet de visualiser et d'analyser les connexions entre artistes (collaborations, appartenance à un groupe, gestion par une agence) via une interface web Flask.

---

## 🧠 Type de graphe utilisé

### Graphe non orienté (`nx.Graph`)
Les relations sont **symétriques** : si Jungkook collabore avec Jimin, Jimin collabore aussi avec Jungkook. Il n'y a pas de direction dans les arêtes.

### Graphe hétérogène (multi-types de nœuds)
Le graphe contient **4 types de nœuds** distincts :

| Type | Exemples | Rôle |
|------|----------|------|
| `groupe` | BTS, BLACKPINK | Relie une agence à ses membres |
| `artiste` | Jungkook, Jennie | Nœud central, impliqué dans les collaborations |
| `agence` | HYBE, SM Entertainment | Nœud hiérarchique supérieur |
| `artiste_externe` | IU, Zico | Artiste hors groupe principal |

### Arêtes typées (attribut `relation`)
Chaque arête possède un attribut `relation` qui précise sa nature :
- `membre_de` — entre un artiste et son groupe
- `manage` — entre une agence et un groupe
- `collaboration` — entre deux artistes ayant travaillé ensemble

---

## 📐 Concepts de théorie des graphes appliqués

| Concept | Fonction | Description |
|---------|----------|-------------|
| **Voisinage filtré** | `connexions_directes()` | Retourne les voisins liés uniquement par `collaboration` |
| **Voisins communs** | `amis_en_commun()` | Intersection des voisins de deux artistes |
| **Plus court chemin (BFS)** | `distance_entre()` | `nx.shortest_path_length()` — degrés de séparation |
| **Centralité par degré** | `artistes_les_plus_connectes()` | `G.degree()` — les hubs du réseau |
| **Disposition force-dirigée** | Route `/graph` | `nx.spring_layout()` — visualisation matplotlib |

---

## 🌐 Fonctionnement du site

### Route `GET / POST /`
Page principale avec deux formulaires d'analyse :
- **Analyse individuelle** : sélectionner un artiste → obtenir la liste de ses collaborations directes
- **Analyse comparative** : choisir deux artistes → obtenir leurs amis en commun + leur distance dans le réseau

### Route `GET /graph`
Affiche une visualisation du graphe complet via `matplotlib` avec un layout `spring_layout`.

---

## 📁 Structure du projet
```
projet-kpop/
├── app.py          # Serveur Flask + construction du graphe + routes
├── graphe.py       # Module autonome d'analyse du graphe
├── data.py         # Données : groupes, agences, collaborations, artistes_externes
└── templates/
    └── index.html  # Interface web (Jinja2)
```

---

## 🚀 Installation et lancement
```bash
# Installer les dépendances
pip install flask networkx matplotlib

# Lancer l'application web
python app.py

# Tester le module graphe seul
python graphe.py
```

Ouvrir dans un navigateur : [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠️ Technologies utilisées

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/) — serveur web
- [NetworkX](https://networkx.org/) — manipulation et analyse de graphes
- [Matplotlib](https://matplotlib.org/) — visualisation
