graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


def dfs(grafico, inicio):
    visitados = set()
    ordem_percorrida = []

    def dfs_auxiliar(node):
        # Marca o nó atual como visitado e depois adiciona á ordem a ser percorrida
        visitados.add(node)
        ordem_percorrida.append(node)

        # Itera sobre os vizinhos do nó atual
        for vizinho in grafico[node]:
            if vizinho not in visitados:
                dfs_auxiliar(vizinho)

    dfs_auxiliar(inicio)
    # Retorna a ordem percorrida pelo algoritmo DFS
    return ordem_percorrida

node_inicio = '5'
ordem_de_percorrida = dfs(graph, node_inicio)
print("Ordem Percorrida:", ordem_de_percorrida)