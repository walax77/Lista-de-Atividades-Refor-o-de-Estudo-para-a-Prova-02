def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Iteração {i+1}: {arr}")
    return arr

# Exemplo de uso
lista = [64, 25, 12, 22, 11]
print("Lista original:", lista)
selection_sort(lista)
print("Lista ordenada:", lista)

# Iteração 1: [11, 25, 12, 22, 64]
# Iteração 2: [11, 12, 25, 22, 64]
# Iteração 3: [11, 12, 22, 25, 64]
# Iteração 4: [11, 12, 22, 25, 64]
# Iteração 5: [11, 12, 22, 25, 64]

