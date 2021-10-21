class Graph:
    def __init__(self):
        self.edges = [] #(a, b, weight)
        self.vertexes = [] #(v, possibleRoot)
 
    def add_edge(self, V1, V2, weight):
        self.edges.append([V1, V2, weight])
        if self.searchVertex(V1) == -1:
            self.vertexes.append([V1, V1])
        if self.searchVertex(V2) == -1:
            self.vertexes.append([V2, V2])
 
    def searchVertex(self, value):
        i = 0
        for v in self.vertexes:
            if v[0] == value:
                return i
            i += 1 
        return -1
 
    def kruskal(self):
        print("\n\n-> Arestas Iniciais:\n")
        for i in range(len(self.edges)):
            print(self.edges[i])
        cost = 0
        for v in self.vertexes:
            v[1] = v[0]
        result = []
        self.edges = sorted(self.edges, key=lambda edge: edge[2])
        sizeResult = len(self.vertexes)-1
        i=0
        while len(result) < sizeResult and i < len(self.edges):
            a, b, weight = self.edges[i]
            iA = self.searchVertex(a)
            iB = self.searchVertex(b)
            Va, Pa = self.vertexes[iA]
            Vb, Pb = self.vertexes[iB]
            if Pa != Pb:
                result.append(self.edges[i])
                cost += self.edges[i][2]
                if Va == Pa and Vb == Pb:
                    self.vertexes[iB][1] = Va
                else:
                    for v in self.vertexes:
                        if v[1] == Pb:
                            v[1] = Pa
            i += 1
        print("\n-> Resultado:")
        for i in range(len(result)):
            print(result[i])
        print("\nCusto = ",cost,"\n")
            
 
 
