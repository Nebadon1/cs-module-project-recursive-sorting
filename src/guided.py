
def partition(arr):
    left = []
    right = []
    pivot = []


    
    for num in arr[1:]:
        if num > pivot:
            right.append(num)
        else:
            left.append(num)
        return left, pivot, right

    #iterate over the rest of the array 
    # if the element is greater tha the pivot, in the right
    #else, in the left 




def quicksort(arr):
    if len(arr)==0:
        retrun arr
    #partition here into left, pivot, and right 
    #divide
    left, pivot, right = partition(arr)
    
    #and conquer 
    return quicksort(left) + pivot + quicksort(right)

