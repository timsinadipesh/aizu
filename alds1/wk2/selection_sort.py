"""
sorts an array in ascending order using the selection sort algorithm

input line 1: n, the number of elements in the array
input line 2: n elements of the array, separated by space character

output line 1: the sorted array
output line 2: the number of swaps taken to sort the array
"""

def selection_sort(arr):
    n = len(arr)
    count_swap = 0

    # go through each element in the array
    for i in range(n):
        # assume the current element is the minimum
        min_index = i

        # go through rest of the elements in the array
        # compare them with the current minimum element
        # update the minimun index if a smaller element is found
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap the found minimum element with the element at current index
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            count_swap += 1

    return arr, count_swap


n = input()
arr = list(map(int, input().split(" ")))
sorted_arr, count_swap = selection_sort(arr)
print(' '.join(map(str, sorted_arr)))
print(count_swap)
        

        