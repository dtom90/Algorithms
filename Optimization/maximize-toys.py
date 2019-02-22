"""
https://practice.geeksforgeeks.org/problems/maximize-toys/0

Maximize Toys

Given an array consisting cost of toys.
Given an integer K depicting the amount with you.
Maximise the number of toys you can have with K amount.

Input:

The first line contains an integer T, depicting total number of test cases.
Then following T lines contains an integer N depicting the number of toys and an integer K depicting the value of K.
Next line is followed by the cost of toys.


Output:

Print the maximum toys in separate line.


Constraints:

1 ≤ T ≤ 30
1 ≤ N ≤ 1000
1 ≤ K ≤ 10000
1 ≤ A[i] ≤ 10000


Example:

Input
1
7 50
1 12 5 111 200 1000 10
Output
4
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


def maximize_toys(n, k, seq):
    available_toys = []
    for toy in seq:
        if toy < k:
            available_toys.append(toy)
            available_toys = sorted(available_toys)

    num_toys = 0
    i = 0
    while k > 0 and i < len(available_toys):
        k -= available_toys[i]
        num_toys += 1
        i += 1
    if k < 0:
        num_toys -= 1

    return num_toys


parse_input(maximize_toys)
