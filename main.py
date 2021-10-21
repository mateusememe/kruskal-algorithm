"""
Desenvolvido por:
    Mateus Mendonça e Vinicius Santana

"""

from graph import Graph

g = Graph()
# Grafo Exemplo do slide

g.add_edge("A", "B", 1)
g.add_edge("A", "D", 4)
g.add_edge("B", "C", 2)
g.add_edge("B", "D", 6)
g.add_edge("C", "E", 5)
g.add_edge("C", "F", 6)
g.add_edge("D", "G", 4)
g.add_edge("D", "E", 3)
g.add_edge("B", "E", 4)
g.add_edge("E", "F", 8)
g.add_edge("E", "G", 7)
g.add_edge("F", "G", 3)
g.kruskal()



## Grafo 2 (primeiro do ultimo slide)
""" g.add_edge("a", "b", 2)
g.add_edge("a", "c", 3)
g.add_edge("c", "d", 1)
g.add_edge("b", "d", 2)
g.add_edge("d", "e", 2)
g.add_edge("d", "f", 4)
g.add_edge("e", "g", 2)
g.add_edge("g", "h", 3)
g.add_edge("g", "f", 2)
g.add_edge("h", "f", 1)
g.kruskal() """