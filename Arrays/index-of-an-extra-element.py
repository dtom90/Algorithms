"""
Index Of an Extra Element
https://practice.geeksforgeeks.org/problems/index_of_an_extra_element/1

Given two sorted arrays. There is only 1 difference between the arrays.
First array has one element extra added in between. Find the index of the extra element.

Input:
The first line of input contains an integer T, denoting the no of test cases. Then T test cases follow.
The first line of each test case contains an integer N, denoting the number of elements in array.
The second line of each test case contains N space separated values of the array A[].
The Third line of each test case contains N_1 space separated values of the array B[].

Output:
Return the index of the corresponding extra element in array A[].(starting index 0).

Constraints:
1<=T<=100
1<=N<=100
1<=Ai<=1000

Example:
Input:
2
7
2 4 6 8 9 10 12
2 4 6 8 10 12
6
3 5 7 9 11 13
3 5 7 11 13
Output:
4
3
"""


def parse_input(func):
    t = int(input())  # "How many use cases? "
    print('\n{} test cases'.format(t))
    for i in range(t):
        print('\nuse case {}'.format(i + 1))
        n = int(input())  # "Size of array? "
        print('n = {}'.format(n))
        seq1 = list(map(lambda x: int(x), input().split()))  # "Sequence? "
        print(seq1)
        seq2 = list(map(lambda x: int(x), input().split()))  # "Sequence? "
        print(seq2)
        print(find_extra(seq1, seq2, n))


def find_extra(a, b, n):
    if n == 1:
        return 0

    i = 0
    elem1 = a[i]
    elem2 = b[i]
    while elem1 == elem2 and i < n-2:
        i += 1
        elem1 = a[i]
        elem2 = b[i]

    if elem1 != elem2:
        return i
    else:
        return i + 1


parse_input(find_extra)
