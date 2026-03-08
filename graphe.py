import networkx as nx
from data import groupes, agences, collaborations, artistes_externes

# -----------------------------
# 1. Création du graphe
# -----------------------------

G = nx.Graph()

# -----------------------------
# 2. Ajouter les groupes et artistes
# -----------------------------

for groupe, membres in groupes.items():
    G.add_node(groupe, type="groupe")
    for membre in membres:
        G.add_node(membre, type="artiste")
        G.add_edge(groupe, membre, relation="membre_de")

# -----------------------------
# 3. Ajouter les agences
# -----------------------------

for agence, groupes_agence in agences.items():
    G.add_node(agence, type="agence")
    for groupe in groupes_agence:
        G.add_edge(agence, groupe, relation="manage")

# -----------------------------
# 4. Ajouter les collaborations
# -----------------------------

for a1, a2 in collaborations:
    G.add_node(a1, type="artiste")
    G.add_node(a2, type="artiste")
    G.add_edge(a1, a2, relation="collaboration")

# -----------------------------
# 5. Ajouter artistes externes
# -----------------------------

for artiste in artistes_externes:
    G.add_node(artiste, type="artiste_externe")

# -----------------------------
# 6. Fonctions d'analyse
# -----------------------------

def connexions_directes(nom):
    """Retourne les connexions directes d'un nœud"""
    if nom not in G:
        return []
    return list(G.neighbors(nom))


def distance_entre(a, b):
    """Retourne la distance minimale entre deux nœuds"""
    try:
        return nx.shortest_path_length(G, a, b)
    except nx.NetworkXNoPath:
        return None
    except nx.NodeNotFound:
        return None


def artistes_les_plus_connectes(top=5):
    """Retourne les artistes les plus connectés"""
    degres = G.degree()
    artistes = [
        (n, d) for n, d in degres
        if G.nodes[n]["type"] in ["artiste", "artiste_externe"]
    ]
    artistes.sort(key=lambda x: x[1], reverse=True)
    return artistes[:top]


# -----------------------------
# 7. Tests (exécution directe)
# -----------------------------

if __name__ == "__main__":
    print("Nombre total de nœuds :", G.number_of_nodes())
    print("Nombre total de relations :", G.number_of_edges())

    print("\nConnexions directes de Jungkook :")
    print(connexions_directes("Jungkook"))

    print("\nDistance entre BTS et IU :")
    print(distance_entre("BTS", "IU"))

    print("\nArtistes les plus connectés :")
    for artiste, degre in artistes_les_plus_connectes():
        print(f"- {artiste} ({degre} connexions)")
