def MergeSort(arr):
    # Caso base: se a lista tem 1 ou 0 elementos, ela já está ordenada
    if len(arr) <= 1:
        return arr
    
    # Encontrar o índice do meio da lista
    meio = len(arr) // 2

    # Dividir a lista em duas sublistas: esquerda e direita
    esquerda = arr[:meio]
    direita = arr[meio:]

    # Ordenar recursivamente cada sublista
    esquerdaArranjada = MergeSort(esquerda)
    direitaArranjada = MergeSort(direita)

    # Mesclar as duas sublistas ordenadas
    return merge(esquerdaArranjada, direitaArranjada)

def merge(esquerda, direita):
    i = j = 0
    resultado = []

    # Mesclar as sublistas enquanto houver elementos em ambas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adicionar os elementos restantes da sublista esquerda, se houver
    resultado.extend(esquerda[i:])
    # Adicionar os elementos restantes da sublista direita, se houver
    resultado.extend(direita[j:])
    
    return resultado

# Lista de exemplo
abab = [30, 45, 21, 20, 6, 715, 100, 65, -30]

# Inteiro alvo para a soma
inteiro = 0

# Flag para indicar se encontramos um par que soma ao inteiro
found = False

# Percorrer cada elemento da lista
for i in range(len(abab)):
    for j in range(i + 1, len(abab)):
        if abab[i] + abab[j] == inteiro:
            print("deu green")
            found = True
            break
    if found:
        break

# Caso não tenha encontrado nenhum par
if not found:
    print("Nenhum par encontrado")
