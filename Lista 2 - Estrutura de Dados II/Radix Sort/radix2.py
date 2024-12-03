def counting_sort_bin(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 2

    for i in range(n):
        index = arr[i] // exp
        count[index % 2] += 1

    for i in range(1, 2):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 2] - 1] = arr[i]
        count[index % 2] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort_bin(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_bin(arr, exp)
        exp *= 2

# Exemplo de uso com números binários
lista_bin = [23, 45, 12, 34, 56, 78, 90]
print("Lista original:", lista_bin)
radix_sort_bin(lista_bin)
print("Lista ordenada (binária):", lista_bin)
