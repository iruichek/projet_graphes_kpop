from flask import Flask, render_template, request
import networkx as nx
import matplotlib.pyplot as plt
from data import groupes, agences, collaborations, artistes_externes

app = Flask(__name__)

# Création du graphe
G = nx.Graph()

# Ajouter groupes et membres
for groupe, membres in groupes.items():
    G.add_node(groupe, type="groupe")
    for membre in membres:
        G.add_node(membre, type="artiste")
        G.add_edge(groupe, membre, relation="membre_de")

# Ajouter agences et groupes
for agence, groupes_agence in agences.items():
    G.add_node(agence, type="agence")
    for groupe in groupes_agence:
        G.add_edge(agence, groupe, relation="manage")

# Ajouter collaborations explicites
for a1, a2 in collaborations:
    G.add_node(a1, type="artiste")
    G.add_node(a2, type="artiste")
    G.add_edge(a1, a2, relation="collaboration")

# --- AJOUTER LES ARÊTES "collaboration" ENTRE TOUS LES MEMBRES DU MÊME GROUPE ---
for groupe, membres in groupes.items():
    for i in range(len(membres)):
        for j in range(i + 1, len(membres)):
            membre1 = membres[i]
            membre2 = membres[j]
            G.add_edge(membre1, membre2, relation="collaboration")
# -------------------------------------------------------------------------------

# Ajouter artistes externes
for artiste in artistes_externes:
    G.add_node(artiste, type="artiste_externe")

# Liste de tous les artistes (type "artiste" uniquement)
tous_les_artistes = [n for n, attr in G.nodes(data=True) if attr["type"] == "artiste"]

def connexions_directes(nom):
    if nom not in G:
        return []
    # Renvoie voisins liés par une relation "collaboration"
    return [n for n in G.neighbors(nom) if G.edges[n, nom].get("relation") == "collaboration"]

def amis_en_commun(a, b):
    if a not in G or b not in G:
        return []
    amis_a = set(connexions_directes(a))
    amis_b = set(connexions_directes(b))
    return list(amis_a.intersection(amis_b))

def distance_entre(a, b):
    try:
        return nx.shortest_path_length(G, a, b)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    artiste_unique = None
    collaborations_directes = []
    artiste1 = None
    artiste2 = None
    amis_communs = []
    distance = None

    if request.method == "POST":
        # Récupérer artiste pour collaboration simple
        artiste_unique = request.form.get("artiste_unique")
        if artiste_unique:
            collaborations_directes = connexions_directes(artiste_unique)

        # Récupérer artistes pour comparaison
        artiste1 = request.form.get("artiste1")
        artiste2 = request.form.get("artiste2")
        if artiste1 and artiste2:
            amis_communs = amis_en_commun(artiste1, artiste2)
            distance = distance_entre(artiste1, artiste2)

    return render_template("index.html",
                           groupes=groupes,
                           artistes=tous_les_artistes,
                           artiste_unique=artiste_unique,
                           collaborations_directes=collaborations_directes,
                           artiste1=artiste1,
                           artiste2=artiste2,
                           amis_communs=amis_communs,
                           distance=distance)

@app.route("/graph")
def afficher_graphe():
    plt.figure(figsize=(10,8))

    pos = nx.spring_layout(G)

    nx.draw(
        G, pos,
        with_labels=True,
        node_color="lightblue",
        node_size=2000,
        font_size=8
    )

    plt.title("Réseau des artistes K-pop")
    plt.show()

    return "Le graphe a été affiché dans une fenêtre."                          

if __name__ == "__main__":
    app.run(debug=True)
