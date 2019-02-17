"""
Kadane's Algorithm
https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1
"""

def parse_input(func):
    t = int(input())  # "How many use cases? "
    # print('{} test cases'.format(t))
    for i in range(t):
        # print('use case {}'.format(i + 1))
        n = int(input())  # "Size of array? "
        # print('n = {}'.format(n))
        seq = list(map(lambda x: int(x), input().split()))  # "Sequence? "
        print(func(n, seq))


def max_sum(n, seq):
    # print(seq)
    all_negs = True
    all_pos = True
    for i in seq:
        if i > 0:
            all_negs = False
        elif i < 0:
            all_pos = False
    if all_negs and all_pos:
        return 0
    else:
        if all_pos:
            return sum(seq)
        elif all_negs:
            return max(seq)
        else:
            m_sum = -float("inf")
            for j in range(n):
                for k in range(j+1, n+1):
                    this_sum = sum(seq[j:k])
                    if this_sum > m_sum:
                        m_sum = this_sum
            return m_sum


parse_input(max_sum)
