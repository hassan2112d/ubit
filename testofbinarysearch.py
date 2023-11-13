
def binarysearch(hello,n):

    low,high = 0,len(hello)
    
    while low <= high:
        mid = (low + high)//2

        if hello[mid] == n :
            return mid
        elif hello[mid] < n:
            low = mid+1
        else:
            high = mid-1
    return -1


hello = [4,6,8,9,12,16,18,24,27,45,65]

n = 27

result = binarysearch(hello,n)

if result != -1:
    print("Founded at " + str(result))
else:
    print("Not founded")