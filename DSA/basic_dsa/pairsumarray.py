"""

Given an array arr[] with n integers and a target value .
The task is to find out whether there is a pair of elements in the array whose sum is equal to the target value
Input: arr[] = {0, -1, 2, -3, 1}, Target = -2
Output: True
Explanation: When we calculate the sum of the output, 1 + (-3) = -2


Input: arr[] = {1, -2, 1, 0, 5}, Target = 0
Output : False

"""


def two_sum(arr_num, target_val):
    n = len(arr_num)

    for i in range(n):

        for j in range(i+1, n):
            if arr_num[i] + arr_num[j] == target_val:
                print("(", arr_num[i] , arr_num[j] , ")" )
                return True

    return  False


if __name__ == "__main__":
    arr_num = [0, -1, 2, -3, 1]
    target_val = -2
    two_sum(arr_num, target_val)
