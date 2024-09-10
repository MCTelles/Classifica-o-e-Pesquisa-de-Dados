def heapify_max(arr, n, i):
    largest = i  # Inicializa o maior como a raiz
    left = 2 * i + 1  # Filho à esquerda
    right = 2 * i + 2  # Filho à direita

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  

        heapify_max(arr, n, largest)

def heap_sort_max(arr):
    n = len(arr)


    for i in range(n // 2 - 1, -1, -1):
        heapify_max(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_max(arr, i, 0)

arr_max = [12, 11, 13, 5, 6, 7]
heap_sort_max(arr_max)
print("Array ordenado com Heap Máximo:", arr_max)
