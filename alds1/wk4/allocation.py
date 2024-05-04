"""
n = packages, k = trucks, w_i = weight of a package i
P = common maximum load 
reads n, k and w_i (i = 0,1,...,n-1) and
reports the minimum value of the maximum load P
to load all packages from the belt conveyor
"""

def min_max_load(loads, k):
    def feasible(max_load):
        trucks_used = 1
        current_load = 0
        for load in loads:
            if load > max_load:
                return False # infeasible
            if current_load + load > max_load:
                trucks_used += 1
                current_load = 0
            current_load += load
        return trucks_used <= k


    # binary search to find the optimal max load
    left, right = max(loads), sum(loads)
    while left < right:
        mid = (left + right) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
        

n, k = map(int, input().split())
loads = [int(input()) for _ in range(n)]

min_p = min_max_load(loads, k)
print(min_p)