def merge_sort_strings(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_strings(L)
        merge_sort_strings(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Exemplo de uso
lista_palavras = ["laranja", "banana", "maçã", "uva", "kiwi"]
merge_sort_strings(lista_palavras)
print("Lista ordenada:", lista_palavras)
