def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

hello = [15,25,35,48,27]

n = 27

result = linearsearch(hello,n)

if result != -1:
    print("Found at " + str(result) + " index.")
else:
    print("Not found")




