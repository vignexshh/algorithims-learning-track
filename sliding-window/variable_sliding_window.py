#goal is to determine longest subarray sum <= k
def longest_subarray_sum(arr, k):
    window_sum = 0
    max_len = 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum > k:
            window_sum -= arr[left]
            left += 1

        max_len = max(max_len, right - left + 1)





arr = [1, 2, 3, 4, 5]
print(longest_subarray_sum(arr, 7))