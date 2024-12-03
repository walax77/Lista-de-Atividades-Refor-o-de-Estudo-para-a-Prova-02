def interpolation_search(lista, elemento):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita and elemento >= lista[esquerda] and elemento <= lista[direita]:
        if esquerda == direita:
            if lista[esquerda] == elemento:
                return esquerda
            return -1
        
        # Probing the position with respect to the value
        pos = esquerda + ((direita - esquerda) // (lista[direita] - lista[esquerda]) * (elemento - lista[esquerda]))

        if lista[pos] == elemento:
            return pos
        if lista[pos] < elemento:
            esquerda = pos + 1
        else:
            direita = pos - 1

    return -1  # Elemento não encontrado

# Exemplo de uso
lista_uniforme = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
elemento = 70
indice = interpolation_search(lista_uniforme, elemento)
if indice != -1:
    print(f"Elemento encontrado no índice: {indice}")
else:
    print("Elemento não encontrado na lista.")
