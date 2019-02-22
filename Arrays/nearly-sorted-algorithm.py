"""
Nearly Sorted Algorithm
https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0

Given an array of n elements, where each element is at most k away from its target position.
The task is to print array in sorted form.

Input:
First line consists of T test cases.
First line of every test case consists of two integers N and K,
denoting number of elements in array and at most k positions away from its target position respectively.
Second line of every test case consists of elements of array.

Output:
Single line output to print the sorted array.

Constraints:
1<=T<=100
1<=N<=100
1<=K<=N

Example:
Input:
2
3 3
2 1 3
6 3
2 6 3 12 56 8
Output:
1 2 3
2 3 6 8 12 56
"""


def parse_input(func):
    t = int(input())  # "How many use cases? "
    # print('{} test cases'.format(t))
    for i in range(t):
        # print('use case {}'.format(i + 1))
        n, k = list(map(lambda x: int(x), input().split()))  # "Size of array? "
        # print('n = {}'.format(n))
        # print('k = {}'.format(k))
        seq = list(map(lambda x: int(x), input().split()))  # "Sequence? "
        # print(seq)
        print(func(n, k, seq))


def fast_sort(n, k, seq):
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if seq[i+1] < seq[i]:
                tmp = seq[i]
                seq[i] = seq[i+1]
                seq[i+1] = tmp
                swapped = True
    return ' '.join(str(n) for n in seq)


parse_input(fast_sort)
