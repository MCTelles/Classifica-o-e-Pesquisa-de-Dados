def counting_sort(arr):
    if len(arr) == 0:
        return arr  # Retorna se o array estiver vazio

    # Encontra o valor máximo e mínimo no array
    max_val = max(arr)
    min_val = min(arr)

    # Inicializa a contagem de acordo com o intervalo [min_val, max_val]
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # Conta a ocorrência de cada elemento no array
    for num in arr:
        count_arr[num - min_val] += 1

    # Altera count_arr para armazenar a posição real de cada elemento no output_arr
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Constrói o array de saída
    for num in reversed(arr):
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1

    # Copia os elementos ordenados de volta para o array original
    for i in range(len(arr)):
        arr[i] = output_arr[i]

# Exemplo de uso
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Array ordenado:", arr)
