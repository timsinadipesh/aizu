"""
uses binary search to find the total number
of elements that are found in both sets
"""

def binary_search(arr, target):
    left_ind, right_ind = 0, len(arr) - 1

    while left_ind <= right_ind:
        mid = (left_ind + right_ind) // 2

        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            right_ind = mid - 1
        else:
            left_ind = mid + 1
         
    return False

n = int(input())
arr1 = list(map(int, input().split(" ")))
q = int(input())
arr2 = list(map(int, input().split(" ")))

common_elements = set()

for element in arr2:
    element_found = binary_search(arr1, element)
    if element_found:
        common_elements.add(element)

print(len(common_elements))
