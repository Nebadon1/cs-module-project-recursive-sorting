# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
   # elements = arrA + arrB
    #merged_arr = sorted(elements)
    
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
   # Your code here
    a_end = len(arrA)
    b_end = len(arrB)

    a_idx = 0
    b_idx = 0
    main_idx = 0

    while a_idx < a_end and b_idx < b_end:
        if arrA[a_idx] <= arrB[b_idx]:
            merged_arr[main_idx] = arrA[a_idx]
            a_idx += 1
            main_idx += 1
        else:
            merged_arr[main_idx] = arrB[b_idx]
            b_idx += 1
            main_idx +=1

    while a_idx < a_end:
            merged_arr[main_idx] = arrA[a_idx]
            a_idx += 1
            main_idx += 1

    while b_idx < b_end:
            merged_arr[main_idx] = arrB[b_idx]
            b_idx += 1
            main_idx += 1
    return merged_arr

   


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
 ### Break the array down recursively
 # Base case: when the list gets down to the lengths of 1
     if len(arr) > 1:
    
         left = merge_sort(arr[0: len(arr) // 2])
         right = merge_sort(arr[len(arr) // 2:])
         arr = merge(left, right)   # merge() defined later
     return arr

 # Merge them back together 
    # Your code here
#    arr_size = len(arr)
#
#        if arr_size < 2:
#            return arr
#
#    mid = arr_size // 2
#
#    sortedLeft = merge_sort(arr[:mid])
#    sortedRight = merge_sort(arr[mid:arr_size+1])
#
#    return merge(sortedLeft, sortedRight)

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
#    if (l < r):
#       # Same as (l + r) / 2, but avoids overflow 
#       # for large l and r 
#       m = l + (r - 1) 
#       # Sort first and second halves 
#       merge_sort_in_place(arr, l, m)
#       merge_sort_in_place(arr, m + 1, r)
#       merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
