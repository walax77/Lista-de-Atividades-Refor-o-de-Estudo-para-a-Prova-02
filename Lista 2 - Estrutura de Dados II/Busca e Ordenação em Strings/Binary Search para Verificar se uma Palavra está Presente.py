def binary_search_strings(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Exemplo de uso
lista_palavras_ordenada = ["banana", "kiwi", "laranja", "maçã", "uva"]
palavra = "maçã"
resultado = binary_search_strings(lista_palavras_ordenada, palavra)
if resultado != -1:
    print(f"A palavra '{palavra}' foi encontrada no índice: {resultado}")
else:
    print(f"A palavra '{palavra}' não foi encontrada na lista.")
