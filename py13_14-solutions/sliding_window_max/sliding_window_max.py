"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


# def sliding_window_max(nums, k):
#     ans = []
#     start = 0
#     window = k
#     end = len(nums) + 1 - k

#     while start < end:
#         maxv = nums[start]
#         for i in range(start, window):
#             if nums[i] > maxv:
#                 maxv = nums[i]
        
#         ans.append(maxv)
#         start += 1
#         window += 1

#     return ans

def sliding_window_max(nums, k):
    ans = []
    for i in range(len(nums) + 1 - k):
        window = nums[i : i + k]
        ans.append(max(window))
    return ans


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}"
    )  # [3,3,5,5,6,7]
