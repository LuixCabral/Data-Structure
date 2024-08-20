class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_Vertice(self, node):
        if node not in self.grafo:
            self.grafo[node] = []

    def adicionar_Aresta(self, node_origem, node_destino):
        if node_origem not in self.grafo:
            self.adicionar_Vertice(node_origem)
        if node_destino not in self.grafo:
            self.adicionar_Vertice(node_destino)
        self.grafo[node_origem].append(node_destino)

    def printar_grafo(self):
        for vertice in self.grafo:
            print(f'{vertice}: {", ".join(map(str, self.grafo[vertice]))}')

# Exemplo de uso
grafo = Grafo()
grafo.adicionar_Vertice("A")
grafo.adicionar_Vertice("B")
grafo.adicionar_Aresta("A", "B")
grafo.adicionar_Aresta("B", "C")
grafo.adicionar_Aresta("A","C")
grafo.adicionar_Aresta("C","A")
grafo.printar_grafo()
