# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

import math


"""test code"""
# def merge_sort(arr):
#     last = len(arr)
#     mid = math.floor(len(arr)/2)
#     if len(arr) <= 1:
#         return arr
    
#     if len(arr) > 2:
#         left_arr = [i for i in arr[:mid]]        
#         right_arr = [i for i in arr[mid:last]]        
#         return [left_arr, right_arr]
#     elif len(arr) == 2:
#         left_arr = [arr[0]]
#         right_arr = [arr[1]]
#         return [left_arr, right_arr]
        
#     return None
# # run 1 goal: [13, 27, 5, 18] [7, 3,19,22,16]

# arr = [13, 27, 5, 18, 7, 3, 19, 22, 16]
# print(f"input arr: {arr}")
# arr2 = merge_sort(arr) # both sides
# print(f"first split: {arr2}")
# arr3 = merge_sort(arr2[0]) #result of left side
# print(f"split left of first: {arr3}")
# arr4 = merge_sort(arr2[1]) #result of right side
# print(f"split right of first: {arr4}")

# arr5 = merge_sort(arr4[0])
# print(f"split left of 2nd: {arr5}")
# arr6 = merge_sort(arr4[1])
# print(f"split right of 2nd: {arr6}")
# arr7 = merge_sort(arr6[0])
# print(f"split left of 3rd: {arr7}")
# arr8 = merge_sort(arr6[1])
# print(f"split right of 3rd: {arr8}")

# print(arr5, arr7)