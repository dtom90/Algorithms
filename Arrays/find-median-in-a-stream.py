"""
Find median in a stream

https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0

Given an input stream of N integers.
The task is to insert these numbers into a new stream
and find the median of the stream formed by each insertion of X to the new stream.

Input:
The first line of input contains an integer N denoting the number of elements in the stream.
Then the next N lines contains integer x denoting the number to be inserted into the stream.
Output:
For each element added to the stream print the floor of the new median in a new line.

Constraints:
1 <= N <= 106
1 <= x <= 106

Example:
Input:
4
5
15
1
3
Output:
5
10
5
4

Explanation:
Testcase 1:
Flow in stream : 5, 15, 1, 3
5 goes to stream --> median 5 (5)
15 goes to stream --> median 10 (5, 15)
1 goes to stream --> median 5 (5, 15, 1)
3 goes to stream --> median 4 (5, 15, 1, 3)
"""


DEBUG = True


def parse_input(func):
    n = int(input())
    # if DEBUG: print('n = {}'.format(n))
    seq = []
    for i in range(n):
        x = int(input())
        # if DEBUG: print('x = {}'.format(x))
        seq = func(x, seq, i)


def find_median_in_stream(x, seq, length):
    # print(x, seq, length)

    if length == 0:
        seq.append(x)
    else:
        i = int(length/2)
        if length % 2 == 0:
            i -= 1
        sub = max(int(length/4), 1)
        inserted = False

        while not inserted and 0 <= i <= length-1:

            if i == 0 and x < seq[i]:
                seq.insert(0, x)
                inserted = True
            elif i == length-1 and x > seq[i]:
                seq.append(x)
                inserted = True
            elif seq[i] < x < seq[i + 1]:
                seq.insert(i + 1, x)
                inserted = True
            elif seq[i + 1] < x:
                i += sub
            else:
                i -= sub
            sub = max(int(sub/2), 1)
        length += 1

    # if DEBUG: print(seq)
    if length == 1:
        med = seq[0]
    elif length % 2 == 0:
        a = int(length / 2)
        med = (seq[a-1] + seq[a]) / 2
    else:
        med = seq[int(length / 2)]
    print(int(med))

    return seq


parse_input(find_median_in_stream)


# Next idea: maintain a binary tree
