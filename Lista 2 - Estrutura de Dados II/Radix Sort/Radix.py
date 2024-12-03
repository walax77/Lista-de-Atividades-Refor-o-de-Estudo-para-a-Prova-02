def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Exemplo de uso com diferentes tamanhos
lista_2_digitos = [23, 45, 12, 34, 56, 78, 90]
lista_5_digitos = [12345, 67890, 54321, 98765, 10234]
lista_10_digitos = [9876543210, 1234567890, 1029384756, 5647382910]

print("Lista original (2 dígitos):", lista_2_digitos)
radix_sort(lista_2_digitos)
print("Lista ordenada (2 dígitos):", lista_2_digitos)

print("Lista original (5 dígitos):", lista_5_digitos)
radix_sort(lista_5_digitos)
print("Lista ordenada (5 dígitos):", lista_5_digitos)

print("Lista original (10 dígitos):", lista_10_digitos)
radix_sort(lista_10_digitos)
print("Lista ordenada (10 dígitos):", lista_10_digitos)
