"""
Find all pairs with a given sum

https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x/0

Given two unsorted arrays A of size N and B of size M of distinct elements,
the task is to find all pairs from both arrays whose sum is equal to X.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow.
Each test case contains 3 lines .
The first line contains 3 space separated integers N, M, X.
Then in the next two lines are space separated values of the array A and B respectively.

Output:
For each test case in a new line
print the sorted space separated values of all the pairs u,v
where u belongs to array A and v belongs to array B,
such that each pair is separated from the other by a ','
without quotes also add a space after the ',' .
If no such pair exist print -1.

Constraints:
1 <= T <= 100
1 <= N, M, X <= 106
-106 <= A, B <= 106

Example:
Input:
2
5 5 9
1 2 4 5 7
5 6 3 4 8
2 2 3
0 2
1 3
Output:
1 8, 4 5, 5 4
0 3, 2 1

Explanation:
Testcase 1: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.
"""


def parse_input(func):
    t = int(input())  # "How many use cases? "
    # print('{} test cases'.format(t))
    for i in range(t):
        # print('use case {}'.format(i + 1))
        n, m, x = tuple(int(s) for s in input().split())  # "Size of array? "
        # print('n = {}'.format(n))
        # print('m = {}'.format(m))
        # print('x = {}'.format(x))
        seq1 = list(int(s) for s in input().split())  # "Sequence? "
        seq2 = list(int(s) for s in input().split())  # "Sequence? "
        # print(seq1)
        # print(seq2)
        all_pairs = func(n, m, x, seq1, seq2)
        if len(all_pairs) == 0:
            print(-1)
        else:
            sorted_pairs = sorted(all_pairs)
            print(', '.join([' '.join([str(n) for n in pair]) for pair in sorted_pairs]))


def find_all_pairs(n, m, x, seq1, seq2):
    all_pairs = []
    complements = set()
    for elem in seq2:
        complements.add(x - elem)
    for elem in seq1:
        if elem in complements:
            all_pairs.append((elem, x-elem))
    return all_pairs


parse_input(find_all_pairs)
