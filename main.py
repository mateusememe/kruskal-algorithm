from graph import Graph
g = Graph()
##grafo 1
# g.add_edge(0, 1, 8)
# g.add_edge(0, 2, 5)
# g.add_edge(1, 2, 9)
# g.add_edge(1, 3, 11)
# g.add_edge(2, 3, 15)
# g.add_edge(2, 4, 10)
# g.add_edge(3, 4, 7)

##grafo2
g.add_edge("a", "b", 1)
g.add_edge("a", "d", 4)
g.add_edge("b", "c", 2)
g.add_edge("b", "d", 6)
g.add_edge("d", "g", 4)
g.add_edge("b", "e", 4)
g.add_edge("c", "e", 5)
g.add_edge("c", "f", 6)
g.add_edge("d", "e", 3)
g.add_edge("e", "g", 7)
g.add_edge("e", "f", 8)
g.add_edge("f", "g", 3)
g.kruskal()