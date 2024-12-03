import time

# Função Shell Sort genérica
def shell_sort(arr, gaps):
    n = len(arr)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = temp
                j -= gap
            arr[j] = temp
    return arr

# Sequência de intervalos de Shell
def shell_sequence(n):
    gap = n // 2
    gaps = []
    while gap > 0:
        gaps.append(gap)
        gap //= 2
    return gaps

# Sequência de intervalos de Knuth
def knuth_sequence(n):
    h = 1
    gaps = []
    while h < n:
        gaps.insert(0, h)  # Insere no início da lista
        h = 3 * h + 1
    return gaps

# Sequência de intervalos de Hibbard
def hibbard_sequence(n):
    k = 1
    gaps = []
    while (1 << k) - 1 < n:
        gaps.insert(0, (1 << k) - 1)  # Insere no início da lista
        k += 1
    return gaps

# Função para medir o tempo de execução
def measure_time(arr, gaps):
    start = time.time()
    shell_sort(arr.copy(), gaps)
    end = time.time()
    return end - start

# Criando uma lista grande e desordenada
import random
lista_grande = random.sample(range(1, 1000000), 10000)

# Sequências de intervalos
shell_gaps = shell_sequence(len(lista_grande))
knuth_gaps = knuth_sequence(len(lista_grande))
hibbard_gaps = hibbard_sequence(len(lista_grande))

# Medindo os tempos de execução
tempo_shell = measure_time(lista_grande, shell_gaps)
tempo_knuth = measure_time(lista_grande, knuth_gaps)
tempo_hibbard = measure_time(lista_grande, hibbard_gaps)

print(f"Tempo de execução (Shell Sequence): {tempo_shell:.6f} segundos")
print(f"Tempo de execução (Knuth Sequence): {tempo_knuth:.6f} segundos")
print(f"Tempo de execução (Hibbard Sequence): {tempo_hibbard:.6f} segundos")
