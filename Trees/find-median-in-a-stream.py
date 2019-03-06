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


DEBUG = False


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.right_count = 0
        self.left_count = 0

    def left_first(self, function, **kwargs):
        if self.left:
            self.left.left_first(function, **kwargs)
        function(self.value, **kwargs)
        if self.right:
            self.right.left_first(function, **kwargs)


class MedBinTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def add(self, new_val):

        if not self.root:
            self.root = Node(new_val)
        else:
            node = self.root
            right = new_val > node.value
            next = node.right if right else node.left
            if right:
                node.right_count += 1
            else:
                node.left_count += 1
            while next:
                node = next
                right = new_val > node.value
                next = node.right if right else node.left
                if right:
                    node.right_count += 1
                else:
                    node.left_count += 1

            if right:
                node.right = Node(new_val)
            else:
                node.left = Node(new_val)

        self.length += 1

    def get_median(self):
        # print(self.length)
        low = int((self.length-1) / 2)
        targets = [low]
        if self.length % 2 == 0:
            targets.append(low+1)

        node = self.root
        position = node.left_count

        vals = []
        while targets:
            while position not in targets:
                prev_position = position
                if targets[0] > position:
                    node = node.right
                    position += node.left_count + 1
                else:
                    node = node.left
                    position -= node.right_count + 1
                if position == prev_position:
                    return position
            vals.append(node.value)
            targets.remove(position)

        if len(vals) == 1:
            return vals[0]
        else:
            return int((vals[0]+vals[1])/2)

    def print(self):
        self.root.left_first(print, end=' ')
        print()


def parse_input():

    n = int(input())
    if DEBUG: print('n = {}'.format(n))

    bin_tree = MedBinTree()

    for i in range(n):
        x = int(input())
        if DEBUG: print('x = {}'.format(x))

        bin_tree.add(x)
        if DEBUG: bin_tree.print()

        print(bin_tree.get_median())


parse_input()
