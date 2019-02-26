"""
Leaders in an array

https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side.
Also, the rightmost element is always a leader.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print all the leaders.

Constraints:
1 <= T <= 100
1 <= N <= 107
0 <= Ai <= 1018

Example:
Input:
3
6
16 17 4 3 5 2
5
1 2 3 4 0
5
7 4 5 7 3
Output:
17 5 2
4 0
7 7 3

Explanation:
Testcase 3: All elements on the right of 7 (at index 0) are smaller than or equal to 7. Also, all the elements of right side of 7 (at index 3) are smaller than 7. And, the last element 3 is itself a leader since no elements are on its right.
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
        leaders = func(n, seq)
        print(' '.join(str(n) for n in leaders))


def leaders_in_array(n, seq):
    leaders = [seq[n-1]]
    max_so_far = seq[n-1]

    for i in range(n-2, -1, -1):
        if seq[i] >= max_so_far:
            leaders.append(seq[i])
            max_so_far = seq[i]

    leaders.reverse()
    return leaders


parse_input(leaders_in_array)
