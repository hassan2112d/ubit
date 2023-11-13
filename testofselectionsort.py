
def selection_sort(arr):
    for i in range(len(arr)):
        min = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j 

        arr[i] , arr[min] = arr[min] , arr[i]
    

hello = [4,2,20,5,9,12,14,18,6]
selection_sort(hello)

print("Sorted array:", hello)
