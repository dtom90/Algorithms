"""
Total Decoding Messages

https://practice.geeksforgeeks.org/problems/total-decoding-messages/0

A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent. You have to determine the total number of ways that message can be decoded.
Note: An empty digit sequence is considered to have one decoding.
It may be assumed that the input contains valid digits from 0 to 9
and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.

Example :
Given encoded message "123",  it could be decoded as "ABC" (1 2 3) or "LC" (12 3) or "AW"(1 23).
So total ways are 3.

Input:
First line contains the test cases T.  1<=T<=1000
Each test case have two lines
First is length of string N.  1<=N<=40
Second line is string S of digits from '0' to '9' of N length.

Example:
Input:
2
3
123
4
2563
Output:
3
2
"""


def parse_input(func):
    t = int(input())  # "How many use cases? "
    # print('{} test cases'.format(t))
    for i in range(t):
        # print('use case {}'.format(i + 1))
        n = int(input())  # "Size of array? "
        # print('n = {}'.format(n))
        seq = input()  # "Sequence? "
        # print(seq)
        print(func(n, seq))


rev_mapping = dict([(n+1, chr(ord('A')+n)) for n in range(26)])


def total_decoding(n, seq):
    # print(seq)
    return count_sub_decodes('', '-1', seq)


def count_sub_decodes(this_msg, check_num, next_nums):
    # print(this_msg, check_num, next_nums)

    n = int(check_num)
    if check_num[0] != '0' and n in rev_mapping:
        this_msg += rev_mapping[n]
    elif n != -1:
        return 0

    # print(this_msg, next_nums)

    if len(next_nums) > 0:
        combos = 0
        combos += count_sub_decodes(this_msg, next_nums[0], next_nums[1:])
        if len(next_nums) > 1:
            combos += count_sub_decodes(this_msg, next_nums[:2], next_nums[2:])
        return combos
    else:
        return 1


parse_input(total_decoding)
