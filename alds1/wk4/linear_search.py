"""
uses linear search to find the number of elements
that are common in two arrays
"""

n = int(input())
arr1 = list(map(int, input().split(" ")))
q = int(input())
arr2 = list(map(int, input().split(" ")))

common_elements = set()

for i in range(n):
    for j in range(q):
        if arr1[i] == arr2[j]:
            common_elements.add(arr1[i])

print(len(common_elements))
