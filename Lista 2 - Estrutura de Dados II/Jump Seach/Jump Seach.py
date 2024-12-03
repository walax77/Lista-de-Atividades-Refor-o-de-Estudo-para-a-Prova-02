import math
import time

# Implementação do Binary Search
def binary_search(lista, elemento):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

# Implementação do Jump Search
def jump_search(lista, elemento):
    n = len(lista)
    passo = int(math.sqrt(n))  # Tamanho ideal do salto
    prev = 0

    # Encontrar o bloco onde o elemento está presente
    while lista[min(passo, n)-1] < elemento:
        prev = passo
        passo += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Realizar busca linear dentro do bloco
    for i in range(prev, min(passo, n)):
        if lista[i] == elemento:
            return i
    return -1

# Função para comparar os tempos de execução
def comparar_buscas(tamanhos):
    for tamanho in tamanhos:
        lista = list(range(tamanho))
        elemento = tamanho - 1  # Elemento que está no final da lista

        # Medir tempo do Jump Search
        inicio = time.time()
        jump_search(lista, elemento)
        tempo_jump = time.time() - inicio

        # Medir tempo do Binary Search
        inicio = time.time()
        binary_search(lista, elemento)
        tempo_binary = time.time() - inicio

        print(f"Tamanho da lista: {tamanho}")
        print(f"Tempo Jump Search: {tempo_jump:.6f} segundos")
        print(f"Tempo Binary Search: {tempo_binary:.6f} segundos")
        print("")

# Tamanhos das listas a serem testadas
tamanhos = [100, 1000, 10000, 100000]

comparar_buscas(tamanhos)
