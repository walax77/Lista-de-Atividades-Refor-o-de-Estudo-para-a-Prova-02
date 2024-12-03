def binary_search(arr, l, r, x):
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
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print(f"Elemento encontrado no índice: {result}")
else:
    print("Elemento não encontrado na lista.")
