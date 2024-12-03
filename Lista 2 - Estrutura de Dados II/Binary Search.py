def binary_search(lista, elemento):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1  # Elemento não encontrado

# Exemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
elemento = 7
indice = binary_search(lista_ordenada, elemento)
if indice != -1:
    print(f"Elemento encontrado no índice: {indice}")
else:
    print("Elemento não encontrado na lista.")
