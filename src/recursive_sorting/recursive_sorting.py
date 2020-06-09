# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = arrA + arrB
    merged_arr = sorted(elements)
    
    #elements = len(arrA) + len(arrB)
   # merged_arr = [0] * elements
   # Your code here
    return merged_arr

   



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
 # Break the array down recursively
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        arr = merge(left, right)
 # Base case: when the list gets down to the lengths of 1
 # Merge them back together 
    # Your code here

    return arr


#implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
                start += 1
        else:
            value = arr[start2]
            index = start2
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
        while (index != start):
            arr[index] = arr[index - 1]
            index -= 1
              
            arr[start] = value
  
            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1
    return arr

def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r):
       # Same as (l + r) / 2, but avoids overflow 
       # for large l and r 
       m = l + (r - 1) 
       # Sort first and second halves 
       merge_sort_in_place(arr, l, m)
       merge_sort_in_place(arr, m + 1, r)
       merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
