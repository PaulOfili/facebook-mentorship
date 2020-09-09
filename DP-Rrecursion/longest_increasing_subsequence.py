def longest_increasing_subsequence(arr):

    longest_streak = [1] * len(arr)

    for j in range(1, len(arr)):
        _max = 0
        for i in range(j):
            if arr[j] > arr[i]:
                _max = max(_max, longest_streak[i])

        longest_streak[j] = 1 + _max

    return max(longest_streak)


print(longest_increasing_subsequence([0,8,4,12,2,10,6,14,1,9]))
print(longest_increasing_subsequence([1,2,3,4,50,2,3,4,2]))
print(longest_increasing_subsequence([1,2,1,2,1,2,1,2,3]))


"""
   
"""

