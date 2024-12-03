import time
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_iterative(arr):
    size = len(arr)
    stack = [0] * (size)
    top = -1

    top = top + 1
    stack[top] = 0
    top = top + 1
    stack[top] = size - 1

    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        p = partition(arr, low, high)

        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

# Função para medir o tempo de execução
def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    end = time.time()
    return end - start

# Listas de exemplo
lista_quase_ordenada = list(range(1000)) + [1000]
lista_desordenada = random.sample(range(1001), 1001)

# Medindo tempos de execução com o Quick Sort iterativo
tempo_quase_ordenada = measure_time(quick_sort_iterative, lista_quase_ordenada.copy())
tempo_desordenada = measure_time(quick_sort_iterative, lista_desordenada.copy())

print(f"Quick Sort iterativo - Lista quase ordenada: {tempo_quase_ordenada:.6f} segundos")
print(f"Quick Sort iterativo - Lista desordenada: {tempo_desordenada:.6f} segundos")
