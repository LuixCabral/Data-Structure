class grafo:
    def __init__(self) -> None:
        self.arestas = []
        self.vertices = []
    def adicionarVertices(self,vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            return True
        else:
            return False
        
    def adicionarArestas(self,aresta):
        if aresta not in self.arestas:
            self.arestas.append(aresta)
            return True
        else:
            return False
        
class vertice:
    def __init__(self, valor):
        self.valor = valor

class aresta:
    def __init__(self,v1,v2):
        self.vertice1 = v1
        self.vertice2 = v2

v1 = vertice("A")
v2 = vertice("B")

a1 = aresta(v1,v2)

g1 = grafo()

g1.adicionarVertices(v1)
g1.adicionarVertices(v2)
g1.adicionarArestas(a1)

