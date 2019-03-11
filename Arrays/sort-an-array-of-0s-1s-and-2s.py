"""
Sort an array of 0s, 1s and 2s

https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0/?ref=self

Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow.
Each testcases contains two lines of input. The first line denotes the size of the array N.
The second lines contains the elements of the array A separated by spaces.

Output:
For each testcase, print the sorted array.

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1

Explanation:
Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2 which shown in the output.
"""


def parse_input():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        sa = sort_arr(a)
        print(' '.join([str(x) for x in sa]))


def sort_arr(a):
    count = {0: 0, 1: 0, 2: 0}
    for x in a:
        count[x] += 1

    sa = []
    for i in range(3):
        sa.extend([i] * count[i])
    return sa


parse_input()
