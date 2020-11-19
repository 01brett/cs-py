'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # base case
    if n < 0:
        return 0
    if n == 0:
        return 1
    # recursion
    one = eating_cookies(n-1)
    two = eating_cookies(n-2)
    three = eating_cookies(n-3)
    return one + two + three

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
