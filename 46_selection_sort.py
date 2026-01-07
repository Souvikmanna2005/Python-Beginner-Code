def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap smallest with first unsorted position
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example
data = [64, 25, 12, 22, 11]
selection_sort(data)
print("Sorted array:", data)
