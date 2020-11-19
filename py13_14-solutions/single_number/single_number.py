"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


def single_number(arr):
    # store the visited counts
    count = {}

    # loop through arr counting what we see
    for num in arr:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    # return the single num
    for num in count:
        if count[num] == 1:
            return num


# def single_number(arr):
#     count = {}
#     seen = []
#     # loop through arr
#     for n in arr:
#         if n not in count:
#             count[n] = 1
#             seen.append(n)
#         else:
#             seen.remove(n)
#             count[n] += 1

#     # return the single num
#     return seen[0]


if __name__ == "__main__":
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
