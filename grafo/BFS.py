graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

fila = []
Nodes_Visitados = []

def bfs(Nodes_Visitados, graph, node): 
  Nodes_Visitados.append(node)
  fila.append(node)

  while fila:         
    m = fila.pop(0) 
    print (m, end = " ") 

    for visinhos in graph[m]:
      if visinhos not in Nodes_Visitados:
        Nodes_Visitados.append(visinhos)
        fila.append(visinhos)

bfs(Nodes_Visitados, graph, '5')