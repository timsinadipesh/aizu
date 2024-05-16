# implement merge sort algorithm
# report the number of comparisons in the merge funciton

NUM_COMP = 0

def merge(arr, left, mid, right):
    global NUM_COMP
    n1 = mid - left
    n2 = right - mid
    left_arr = [arr[i] for i in range(left, mid)]
    right_arr = [arr[i] for i in range(mid, right)]
    left_arr.append(float('inf'))
    right_arr.append(float('inf'))
    i, j = 0, 0
    for k in range(left, right):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        NUM_COMP += 1

def merge_sort(arr, left, right):
    if len(arr) <= 1:
        return arr
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


n = int(input())
arr = list(map(int, input().split()))
merge_sort(arr, 0, len(arr))
print(*arr)
print(NUM_COMP)