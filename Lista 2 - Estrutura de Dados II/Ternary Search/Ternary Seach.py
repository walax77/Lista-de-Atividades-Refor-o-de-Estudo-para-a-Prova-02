def ternary_search(arr, l, r, x):
    if r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            return ternary_search(arr, l, mid1 - 1, x)
        elif x > arr[mid2]:
            return ternary_search(arr, mid2 + 1, r, x)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)

    return -1

# Exemplo de uso
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
result = ternary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print(f"Elemento encontrado no índice: {result}")
else:
    print("Elemento não encontrado na lista.")
