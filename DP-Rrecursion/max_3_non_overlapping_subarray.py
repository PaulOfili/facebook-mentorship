
def get_k_prefix_sums(arr, k):

    prefix_sum = 0
    for i in range(k):
        prefix_sum += arr[i]

    every_sublist = [prefix_sum]
    for i in range(k, len(arr)):
        prefix_sum += arr[i]
        prefix_sum -= arr[i - k]
        every_sublist.append(prefix_sum)

    return every_sublist

def max_3_non_overlapping_recursive(arr, k):

    if k > len(arr) or 3*k > len(arr):
        return False

    k_prefix_sums = get_k_prefix_sums(arr, k)

    max_depth = 3

    def helper(i, m):
        if i >= len(k_prefix_sums) or m == 0:
            return 0

        incl = k_prefix_sums[i] + helper(i+k, m-1)
        excl = helper(i+1, m)

        return max(incl, excl)

    return helper(0, max_depth)



def max_3_non_overlapping_iterative(arr, k):

    if k > len(arr) or 3*k > len(arr):
        return False

    k_prefix_sums = get_k_prefix_sums(arr, k)
    prefix_sums_length = len(k_prefix_sums)

    count = 3
    dpTable = [[0]*(count+1) for _ in range(prefix_sums_length)]

    for i in range(len(dpTable)):
        for j in range(count+1):
            if j == 0:
                dpTable[i][j] = 0
                continue

            _with = k_prefix_sums[i] + (dpTable[i-k][j-1] if i >= k else 0)

            without = dpTable[i-1][j] if i > 0 else float("-inf")

            dpTable[i][j] = max(_with, without)

    return dpTable[prefix_sums_length-1][count]

def max_3_non_overlapping_linear(arr, k):

    if k > len(arr) or 3 * k > len(arr):
        return False

    k_prefix_sums = get_k_prefix_sums(arr, k)

    left = []
    right = []

    left_max = float("-inf")
    for num in k_prefix_sums:
        left_max = max(left_max, num)
        left.append(left_max)

    right_max = float("-inf")
    for i in range(len(k_prefix_sums)-1, -1, -1):
        right_max = max(right_max, k_prefix_sums[i])
        right.append(right_max)
    right.reverse()

    _max = float("-inf")
    for i in range(k, len(k_prefix_sums)-k):
        current_sum = left[i-k] + k_prefix_sums[i] + right[i+k]
        _max = max(_max, current_sum)

    return _max



print(max_3_non_overlapping_recursive([1,2,3,4,5,6], 2))
print(max_3_non_overlapping_iterative([1,2,3,4,5,6], 2))
print(max_3_non_overlapping_linear([1,2,3,4,5,6], 2))
print(max_3_non_overlapping_linear([-1,-2,-3], 1))
print(max_3_non_overlapping_recursive([1,2,6,3,11,2], 2))
print(max_3_non_overlapping_iterative([1,2,6,3,11,2], 2))
print(max_3_non_overlapping_linear([1,2,6,3,11,2], 2))
print(max_3_non_overlapping_recursive([2,3,4,5,6,8], 2))
print(max_3_non_overlapping_iterative([2,3,4,5,6,8], 2))
print(max_3_non_overlapping_linear([2,3,4,5,6,8], 2))