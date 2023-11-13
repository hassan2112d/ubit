

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
hello = [4,2,20,5,9,12,14,18,6]
selection_sort(hello)
print("Sorted array:", hello)
     


