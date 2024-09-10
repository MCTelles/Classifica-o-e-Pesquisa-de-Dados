def heapify_min(arr, n, i):
    smallest = i  # Inicializa o menor como a raiz
    left = 2 * i + 1  # Filho à esquerda
    right = 2 * i + 2  # Filho à direita

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]

        heapify_min(arr, n, smallest)

def heap_sort_min(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify_min(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify_min(arr, i, 0) 

arr_min = [12, 11, 13, 5, 6, 7]
heap_sort_min(arr_min)
print("Array ordenado com Heap Mínimo:", arr_min)
