"""
Kth smallest element

https://practice.geeksforgeeks.org/problems/kth-smallest-element/0

Given an array arr and a number K where K is smaller than size of array,
the task is to find the K’th smallest element in the given array.
It is given that all array elements are distinct.

Expected Time Complexity: O(n)

Input:
The first line of input contains an integer T, denoting the number of testcases.
Then T test cases follow. Each test case consists of three lines.
First line of each testcase contains an integer N denoting size of the array.
Second line contains N space separated integer denoting elements of the array.
Third line of the test case contains an integer K.

Output:
Corresponding to each test case, print the desired output in a new line.

Constraints:
1 <= T <= 106
1 <= N <= 100
1 <= arr[i] <= 103
1 <= K <= N

Example:
Input:
2
6
7 10 4 3 20 15
3
5
7 10 4 20 15
4

Output:
7
15
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
        k = int(input())  # "Size of array? "
        # print('k = {}'.format(k))
        print(func(n, seq, k))


def kth_smallest_element(n, seq, k):
    smallest = sorted(seq[:k])
    for elem in seq[k:]:
        if elem < smallest[-1]:
            smallest.pop(-1)
            smallest.append(elem)
            smallest = sorted(smallest)
    return smallest[-1]


parse_input(kth_smallest_element)
