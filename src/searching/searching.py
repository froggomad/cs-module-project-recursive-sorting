# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end): 
  
    # base case
        if end < start:
            return -1

        mid = (end + start) // 2

        # found 
        if arr[mid] == target: 
            return mid 

        # target smaller than mid, check left
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        # larger, check right
        else: 
            return binary_search(arr, target, mid + 1, end)
  
def descending_binary_search(arr, target, start, end):
    # base case
        if end < start:
            return -1

        mid = (end + start) // 2

        # found 
        if arr[mid] == target: 
            return mid 

        # target smaller than mid, check right
        elif arr[mid] > target:
            return descending_binary_search(arr, target, mid + 1, end)
        # larger, check left
        else:
            return descending_binary_search(arr, target, start, mid - 1)            

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    #check if descending
    descending = arr[0] > arr[1]
    if descending:
        return descending_binary_search(arr, target, 0, len(arr)-1)
    else:
        return binary_search(arr, target, 0, len(arr)-1)

arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr2 = [9,8,7,5,3,2,1,0,-2,-3,-4,-6,-8,-9]
arr3 = [0,1,2,3,4,5,6,7]
arr4 = [7,6,5,4,3,2,1,0]
arr5 = [-1,-2,-3,-4,-5,-6,-7]
arr6 = [-7,-6,-5,-4,-3,-2,-1]
result = agnostic_binary_search(arr6, -2)
print(result)