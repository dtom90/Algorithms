"""
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case consists of two lines.
The first line of each test case is N and S, where N is the size of array and S is the sum.
The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing)
of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
"""

input_sequence = "2\n" \
                 "5 12\n" \
                 "1 2 3 7 5\n" \
                 "10 15\n" \
                 "1 2 3 4 5 6 7 8 9 10"


def subarray_with_given_sum(input_sequence):
    input_arr = input_sequence.split('\n')
    t = int(input_arr[0])

    print('{} test cases'.format(t))
    for i in range(t):

        print('use case {}'.format(i+1))
        n, s = tuple(map(lambda x: int(x), input_arr[2*i+1].split()))
        print('n = {}'.format(n))
        print('s = {}'.format(s))

        arr = list(map(lambda x: int(x), input_arr[2 * i + 2].split()))
        print(arr)
        print(find_match(n, s, arr))


def find_match(n, s, arr):
    for j in range(n):
        sum = arr[j]
        for k in range(j, n):
            if k > j:
                sum += arr[k]
            # print(j, k, sum)
            if sum == s:
                return j+1, k+1
    return -1


subarray_with_given_sum(input_sequence)
