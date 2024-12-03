def binary_search(lista, elemento, esquerda, direita):
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def exponential_search(lista, elemento):
    if lista[0] == elemento:
        return 0

    # Encontrar o intervalo onde o elemento pode estar
    indice = 1
    while indice < len(lista) and lista[indice] <= elemento:
        indice *= 2

    # Realizar Binary Search no intervalo encontrado
    return binary_search(lista, elemento, indice // 2, min(indice, len(lista) - 1))

# Exemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
elemento = 13
indice = exponential_search(lista_ordenada, elemento)
if indice != -1:
    print(f"Elemento encontrado no índice: {indice}")
else:
    print("Elemento não encontrado na lista.")
