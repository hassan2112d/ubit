
def binarysearch(arr,target):

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Target not found

sum = [2,7,9,10,23,45,65,73,83,95,111,123]

n = 83

result = binarysearch(sum,n)

if result != -1:
    print(f"Element {n} found at index {result}.")
else:
    print(f"Element {n} not found in the list.")
