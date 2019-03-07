"""
K-Palindrome

https://practice.geeksforgeeks.org/problems/k-palindrome/1

A string is k palindrome if it can be transformed into a palindrome on removing at most k characters from it.
Your task is to complete the function is_k_palin which takes two arguments a string str and a number N .
Your function should return true if the string is k palindrome else it should return false.

Input:
The first line of input is an integer T denoting the number of test cases . Then T test cases follow .
Each test case  contains a string str and an integer N separated by space.

Output:
The output will be 1 if the string is  k palindrome else 0 .

Constraints:
1<=T<=100
1<=length of str<=100
1<=N<=20

Example:
Input
2
abcdecba 1
acdcb  1
Output
1
0
"""
from itertools import chain, combinations


def parse_input():
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        string = arr[0]
        n = int(arr[1])
        print(is_k_palin(string, n))


def is_k_palin(string, n):
    rev_string = string[::-1]
    if string == rev_string:
        return 1

    inequals = []
    for i, c in enumerate(string):
        if c != rev_string[i]:
            inequals.append(i)

    powerset = chain.from_iterable(combinations(inequals, r) for r in range(len(inequals)+1))

    for drops in powerset:
        if len(drops) > n:
            return 0
        substr = string
        for idx in drops:
            substr = string[:idx] + string[idx + 1:]

        if substr == substr[::-1]:
            return 1
    return 0


parse_input()

# TODO: Improve efficiency
