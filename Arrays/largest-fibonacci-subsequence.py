"""
Largest Fibonacci Subsequence

https://practice.geeksforgeeks.org/problems/largest-fibonacci-subsequence/0

Given an array with positive number,
the task is to find the largest subsequence from array that contain elements which are Fibonacci numbers.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow.
Each test case contains an integer N denoting the size of the array.
Then in the next line are N space separated values of the array.

Output:
For each test case in a new line print the space separated elements of the  longest fibonacci subsequence.

Constraints:
1<=T<=100
1<=N<=100
1<=A[]<=1000

Example:
Input:
2
7
1 4 3 9 10 13 7
9
0 2 8 5 2 1 4 13 23

Output:
1 3 13
0 2 8 5 2 1 13

# NOTE: This is not the largest fibonacci sequence, but sequence of fibonacci numbers
"""


def parse_input():
    t = int(input())
    for i in range(t):
        n = int(input())
        seq = [int(x) for x in input().split()]
        print(largest_fib(n, seq))


def largest_fib(n, seq):

    fibs = set([0, 1, 2])
    fib1 = 1
    fib2 = 2

    fib_seq = []
    for num in seq:
        while num > fib2:
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
            fibs.add(fib2)
        if num in fibs:
            fib_seq.append(num)

    return ' '.join([str(j) for j in fib_seq])


parse_input()
