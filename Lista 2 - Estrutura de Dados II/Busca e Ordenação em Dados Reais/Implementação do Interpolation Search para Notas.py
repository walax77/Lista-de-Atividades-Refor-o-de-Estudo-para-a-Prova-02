def interpolation_search_grades(grades, target):
    l, r = 0, len(grades) - 1

    while l <= r and target >= grades[l] and target <= grades[r]:
        if l == r:
            if grades[l] == target:
                return l
            return -1

        # Posição de interpolação
        pos = l + ((r - l) // (grades[r] - grades[l]) * (target - grades[l]))

        if grades[pos] == target:
            return pos
        if grades[pos] < target:
            l = pos + 1
        else:
            r = pos - 1
    
    return -1

# Exemplo de uso
nota_procurada = 78
indice_nota = interpolation_search_grades(notas_ordenadas, nota_procurada)
if indice_nota != -1:
    print(f"Nota {nota_procurada} encontrada no índice: {indice_nota}")
else:
    print("Nota não encontrada.")
