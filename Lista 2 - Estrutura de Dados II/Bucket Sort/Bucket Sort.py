def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribuindo os elementos nos "baldes"
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    # Ordenando cada balde individualmente
    for bucket in buckets:
        bucket.sort()

    # Concatenando todos os baldes em um único array ordenado
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Exemplo de uso
lista = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Lista original:", lista)
lista_ordenada = bucket_sort(lista)
print("Lista ordenada:", lista_ordenada)
