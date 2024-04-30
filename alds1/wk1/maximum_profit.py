"""
reads values of a currency R_t at a certain time t(t=0,1,2,...,n-1)
and reports the maximum value of R_j - R_i where j > i
"""

n = int(input())
li = []          
for _ in range(n):
    li.append(int(input()))

tmp_low = float('inf')
max_diff = float('-inf')
for i in range(n - 1):
    if li[i] < tmp_low:     
        tmp_low = li[i]
        tmp_diff = li[i + 1] - li[i]
    else:
        tmp_diff = li[i + 1] - tmp_low
    if tmp_diff > max_diff:
        max_diff = tmp_diff
print(max_diff)


