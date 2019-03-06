"""
Find triplets with zero sum

https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1

Given an array A of N elements.
The task is to complete the function which returns true if triplets exists in array A whose sum is zero else returns false.

Input Format:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow.
The first line of each test case contains an integer N, denoting the number of elements in array.
The second line of each test case contains N space separated values of the array.

Output:
For each test case, output will be 1 if triplet exists else 0.

Your Task:
Your task is to only complete the function to findTriplets().

Constrains:
1 <= T <= 100
1 <= N <= 106
-106 <= A <= 106

Example:
Input:
2
5
0 -1 2 -3 1
3
1 2 3

Output:
1
0

Explanation:
Testcase 1: 0, -1 and 1 forms a triplet with sum equal to 0.
Testcase 2: No triplet exists which sum to 0.
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''


# User function Template for python3
def find_triplet(n, seq):
    if n < 3:
        return 0

    a = seq[0]
    b = seq[1]
    c = seq[2]

    i = 2
    while a + b + c != 0 and i+1 < n:
        i += 1
        a = b
        b = c
        c = seq[i]

    if a + b + c == 0:
        return 1
    return 0


t = int(input())
for case in range(t):
    n = int(input())
    seq = [int(x) for x in input().split()]
    print(find_triplet(n, seq))
