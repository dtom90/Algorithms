"""
Activity Selection

https://practice.geeksforgeeks.org/problems/activity-selection/0

Given N activities with their start and finish times.
Select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.

Note : The start time and end time of two activities may coincide.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases.
First line is N number of activities
then second line contains N numbers which are starting time of activies.
Third line contains N finishing time of activities.

Output:
For each test case, output a single number denoting maximum activites which can be performed in new line.


Constraints:
1<=T<=50
1<=N<=1000
1<=A[i]<=100


Example:
Input:
1
6
1 3 2 5 8 5
2 4 6 7 9 9

Output:
4
"""


def parse_input():
    t = int(input())
    for i in range(t):
        n = int(input())
        starts = [int(x) for x in input().split()]
        ends = [int(x) for x in input().split()]
        print(max_activites(n, starts, ends))


def max_activites(n, starts, ends):
    activities = [(starts[i], ends[i]) for i in range(n)]
    activities.sort()
    max_b = 0
    for i in range(n):
        new_branch = max_branch(i, 1, n, activities)
        if new_branch > max_b:
            max_b = new_branch
    return max_b


def max_branch(i, d, n, activities):
    max_b = 0
    leaf = True
    for j in range(i+1, n):
        if activities[i][1] < activities[j][0]:
            leaf = False
            new_branch = max_branch(j, d+1, n, activities)
            if new_branch > max_b:
                max_b = new_branch
    if leaf:
        return d
    else:
        return max_b


parse_input()

# TODO: Optimize
