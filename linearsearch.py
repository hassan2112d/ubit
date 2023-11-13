def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

listt = [6, 2, 3, 7, 9, 11]

n = 9

result = linearsearch(listt, n)

if result != -1:
    print("Found at " + str(result))  # Convert the index to a string
else:
    print("Not Found")
