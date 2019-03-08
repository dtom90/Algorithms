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
    print(string, n)

    a = 0
    z = len(string)-1

    removed = 0
    equal = True
    low_grp = {}
    hi_grp = {}
    while a < z:
        print(string[a], string[z])
        if not equal:
            low_grp[string[a]] += 1
            hi_grp[string[z]] += 1
            diff = 0
            for letter, count in low_grp.items():
                if letter in hi_grp:
                    diff += abs(count - hi_grp[letter])
                else:
                    diff += count
            for letter in hi_grp:
                if letter not in low_grp:
                    diff += hi_grp[letter]
            print(diff)

        if string[a] != string[z]:
            print('inequal!')
            equal = False
            low_grp[string[a]] = 1
            hi_grp[string[z]] = 1
        a += 1
        z -= 1

    return low_grp, hi_grp


parse_input()

# TODO: Improve efficiency
