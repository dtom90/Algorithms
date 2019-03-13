"""
Maximum of all subarrays of size k

https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k/0

Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case contains a single integer N denoting the size of array and the size of subarray K.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum for every subarray of size k.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ K ≤ N
0 ≤ A[i] <= 107

Example:
Input:
2
9 3
1 2 3 1 4 5 2 3 6
10 4
8 5 10 7 9 4 15 12 90 13

Output:
3 3 4 5 5 5 6
10 10 10 15 15 90 90

Explanation:
Testcase 1: Starting from first subarray of size k = 3, we have 3 as maximum.
Moving the window forward, maximum element are as 3, 4, 5, 5, 5 and 6.
"""


def parse_input():
    t = int(input())
    for i in range(t):
        n, k = tuple(int(x) for x in input().split())
        seq = [int(x) for x in input().split()]
        res = max_subarr(n, k, seq)
        print(' '.join([str(x) for x in res]))


def max_subarr(n, k, arr):

    sub_dict = {}
    sub_arr = arr[:k]
    cur_max = -float("inf")
    for elem in sub_arr:
        sub_dict[elem] = sub_dict[elem] + 1 if elem in sub_dict else 1
        if elem > cur_max:
            cur_max = elem
    res = [cur_max]

    for i in range(k, n):
        new_elem = arr[i]
        old_elem = arr[i-k]

        sub_dict[old_elem] -= 1
        if sub_dict[old_elem] == 0:
            del sub_dict[old_elem]
            if old_elem == cur_max:
                cur_max = -float("inf")
                for elem in sub_dict:
                    if elem > cur_max:
                        cur_max = elem

        sub_dict[new_elem] = sub_dict[new_elem] + 1 if new_elem in sub_dict else 1
        if new_elem > cur_max:
            cur_max = new_elem

        res.append(cur_max)
    return res


parse_input()
