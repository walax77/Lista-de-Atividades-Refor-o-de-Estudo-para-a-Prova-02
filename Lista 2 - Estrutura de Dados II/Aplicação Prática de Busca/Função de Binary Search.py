def binary_search_isbn(biblioteca, isbn):
    l, r = 0, len(biblioteca) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if biblioteca[mid]["isbn"] == isbn:
            return biblioteca[mid]
        elif biblioteca[mid]["isbn"] < isbn:
            l = mid + 1
        else:
            r = mid - 1
    return None

# Exemplo de uso
isbn_procurado = "9788535911100"
livro_encontrado = binary_search_isbn(biblioteca_ordenada, isbn_procurado)
if livro_encontrado:
    print(f"Livro encontrado: {livro_encontrado['titulo']} com ISBN {livro_encontrado['isbn']}")
else:
    print("Livro não encontrado.")
