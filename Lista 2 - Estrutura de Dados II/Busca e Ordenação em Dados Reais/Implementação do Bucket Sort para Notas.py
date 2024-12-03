def bucket_sort_grades(grades):
    bucket_count = 10  # Usando 10 baldes para intervalos de 10 notas cada
    buckets = [[] for _ in range(bucket_count)]
    comparisons = 0

    # Distribuir as notas nos baldes
    for grade in grades:
        index = min(grade // 10, bucket_count - 1)  # Encontra o índice do balde apropriado
        buckets[index].append(grade)

    # Ordenar cada balde individualmente
    for bucket in buckets:
        bucket.sort()

    # Concatenar todos os baldes em uma lista ordenada
    sorted_grades = []
    for bucket in buckets:
        sorted_grades.extend(bucket)
    
    return sorted_grades

# Exemplo de uso
notas = [88, 70, 55, 78, 99, 80, 67, 92, 45, 83]
notas_ordenadas = bucket_sort_grades(notas)
print("Notas ordenadas:", notas_ordenadas)
