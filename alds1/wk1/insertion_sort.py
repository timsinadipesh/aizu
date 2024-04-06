"""
insertion sort algorithm which
sorts a sequence in ascending order
"""

# the number of elements in the sequence
n = int(input())

# read the input and convert each to integer
arr = list(map(int, input().split()))

output = ""
for each in arr:
    output += str(each) + " "
print(output[:-1])

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    # compare the key to elements in the sorted array
    # move those that are greater than the key
    # one position ahead
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    # place the key in its correct position
    arr[j + 1] = key

    output = ""
    for each in arr:
        output += str(each) + " "
    print(output[:-1])

