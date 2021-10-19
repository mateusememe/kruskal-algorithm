from graph import Graph
g = Graph()
#grafo 1
"""
    g.add_edge(0, 1, 8)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 2, 9)
    g.add_edge(1, 3, 11)
    g.add_edge(2, 3, 15)
    g.add_edge(2, 4, 10)
    g.add_edge(3, 4, 7)
"""

##grafo1
g.add_edge("a", "b", 2)
g.add_edge("a", "c", 3)
g.add_edge("c", "d", 1)
g.add_edge("b", "d", 2)
g.add_edge("d", "e", 2)
g.add_edge("d", "f", 4)
g.add_edge("e", "g", 2)
g.add_edge("g", "h", 3)
g.add_edge("g", "f", 2)
g.add_edge("h", "f", 1)
g.kruskal()