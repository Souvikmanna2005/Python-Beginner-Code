def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Example
data = [10, 25, 30, 45, 50]
key = int(input('Enter key:'))

result = linear_search(data, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
