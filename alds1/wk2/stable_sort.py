"""
sorts a given set of cards in ascending order by their values
using bubble sort and selection sort. reports the stability
of the output for the given input
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j][1] < arr[j - 1][1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mini_idx = i
        for j in range(i + 1, n):
            if arr[j][1] < arr[mini_idx][1]:
                mini_idx = j
        if mini_idx != i:
            arr[i], arr[mini_idx] = arr[mini_idx], arr[i]
    return arr


n = input()
input_array = input().split()
arr = []
for element in input_array:
    suit, val = element[0], int(element[1])
    arr.append([suit, val])

arr1 = arr[:]
arr2 = arr[:]
bubble_sorted = bubble_sort(arr1)
selection_sorted = selection_sort(arr2)

print(" ".join(f"{card[0]}{card[1]}" for card in bubble_sorted))
print("Stable" if bubble_sorted == sorted(arr.copy(), key=lambda x: x[1]) else "Not stable")
print(" ".join(f"{card[0]}{card[1]}" for card in selection_sorted))
print("Stable" if selection_sorted == sorted(arr.copy(), key=lambda x: x[1]) else "Not stable")