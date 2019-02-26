"""
Rotate Array

https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0

Given an array of size N, rotate it by D elements.

Input:
The first line of the input contains T denoting the number of testcases.
First line of test case is the number of elements N, next line contains D.
Subsequent line will be the array elements.

Output:
For each testcase, in a new line, output the rotated array.

Constraints:
1 <= T <= 200
1 <= N <= 107
1 <= D <= N
1 <= arr[i] <= 103

Example:
Input:
2
5 2
1 2 3 4 5
10 3
2 4 6 8 10 12 14 16 18 20

Output:
3 4 5 1 2
8 10 12 14 16 18 20 2 4 6

Explanation :
Testcase 1: 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2
"""


def parse_input(func):
    t = int(input())  # "How many use cases? "
    # print('{} test cases'.format(t))
    for i in range(t):
        # print('use case {}'.format(i + 1))
        n, d = list(map(lambda x: int(x), input().split()))  # "Size of array? "
        # print('n = {}'.format(n))
        # print('d = {}'.format(d))
        seq = list(map(lambda x: int(x), input().split()))  # "Sequence? "
        # print(seq)
        rot_arr = func(n, d, seq)
        print(' '.join(str(n) for n in rot_arr))


def rotate_array(n, d, seq):
    rot_arr = seq[d:]
    rot_arr.extend(seq[:d])
    return rot_arr


parse_input(rotate_array)
