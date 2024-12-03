def merge_sort_strings(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        merge_sort_strings(esquerda)
        merge_sort_strings(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

# Exemplo de uso
lista_strings = ["laranja", "banana", "maçã", "uva", "kiwi"]
merge_sort_strings(lista_strings)
print("Lista ordenada:", lista_strings)
