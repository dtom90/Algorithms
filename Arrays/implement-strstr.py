"""
Implement strstr

https://practice.geeksforgeeks.org/problems/implement-strstr/1

Your task is to implement the function strstr.
The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s.
The function returns and integer denoting the first occurrence of the string x in s.

Input Format:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow.
The first line of each test case contains two strings s and x.

Output Format:
For each test case, in a new line, output will be an integer denoting the first occurrence of the x in the string s.
Return -1 if no match found.

Your Task:
Since this is a function problem, you don't have to take any input. Just complete the strstr function.

Constraints:
1 <= T <= 100
1<= |s|,|x| <= 1000

Example:
Input
2
GeeksForGeeks Fr
GeeksForGeeks For
Output
-1
5
"""


def parse_input():
    t = int(input())
    # print('\n{} test cases'.format(t))
    for i in range(t):
        # print('\nuse case {}\n'.format(i + 1))
        s, x = tuple(input().split())
        print(strstr(s, x))


def strstr(s, x):
    for i in range(len(s)):
        j = 0
        while j < len(x) and j < len(s) - i and s[i+j] == x[j]:
            j += 1
        if j == len(x):
            return i
    return -1


parse_input()
