"""
Missing number in array
https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases.
For each test case first line contains N(size of array).
The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9
"""


def parse_input(func):
    t = int(input())  # "How many use cases? "
    # print('{} test cases'.format(t))
    for i in range(t):
        # print('use case {}'.format(i + 1))
        n = int(input())  # "Size of array? "
        # print('n = {}'.format(n))
        seq = list(map(lambda x: int(x), input().split()))  # "Sequence? "
        # print(seq)
        print(func(n, seq))


def missing_number(n, seq):
    expected_sum = int(n*(n+1) / 2)
    return expected_sum - sum(seq)


parse_input(missing_number)
