"""
sorts an array in ascending order using the bubble sort algorithm

input line 1: n, the number of elements in the array
input line 2: n elements of the array, separated by space character

output line 1: the sorted array
output line 2: the number of swaps taken to sort the array
"""


def bubble_sort(array):
    n = len(array)
    count_swap = 0

    for i in range(n):
        # flag to track swapping in the current iteration
        swapped = False

        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                # place the larger element in the higher index position
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                count_swap += 1

        # if no swapping occurred, the array is already sorted
        if not swapped:
            break

    return array, count_swap


n = input()
arr = list(map(int, input().split(" ")))
sorted_arr, count_swap = bubble_sort(arr)
print(' '.join(map(str, sorted_arr)))
print(count_swap)