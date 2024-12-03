def quick_sort_strings(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        menores = [x for x in arr if x < pivot]
        iguais = [x for x in arr if x == pivot]
        maiores = [x for x in arr if x > pivot]
        return quick_sort_strings(menores) + iguais + quick_sort_strings(maiores)

# Exemplo de uso
lista_palavras = ["laranja", "banana", "maçã", "uva", "kiwi"]
lista_palavras_ordenada = quick_sort_strings(lista_palavras)
print("Lista ordenada:", lista_palavras_ordenada)
