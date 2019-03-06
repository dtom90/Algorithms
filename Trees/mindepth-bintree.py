"""
Minimum Depth of a Binary Tree

https://practice.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1

Given a binary tree, your task is to complete the function minDepth
which takes one argument the root of the binary tree and prints the min depth of  binary tree .

          1
       /    \
     2       3
   /
4

For the tree above the min depth is 2 ie 1 3

Input:

The task is to complete the method which takes one argument, root of Binary Tree.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The output will be an integer denoting the min depth of the binary tree.

Constraints:
1 <=T<= 30
1 <= Number of nodes<= 20


Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
2
2


"""

class Node:

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:  # Binary tree Class

    def createNode(self, data):
        return Node(data)

    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right

    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i

    def traverseInorder(self, root):
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data, end=" ")
            self.traverseInorder(root.right)


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# Function should return an integer
def minDepth(root):
    return getDepth(root, 0)


def getDepth(node, depth):
    if node is None:
        return depth

    depth += 1
    left_depth = getDepth(node.left, depth)
    right_depth = getDepth(node.right, depth)
    return min(left_depth, right_depth)


t=int(input())
for i in range(t):
    n=int(input())
    arr = input().strip().split()
    tree = Tree()
    lis=[]
    root = None
    root = tree.insert(root, int(arr[0]), 'L')
    lis.append(root)
    k=0
    for j in range(n):
        ptr = None
        ptr = tree.search(lis, int(arr[k]))
        lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
        k+=3
    # tree.traverseInorder(root)
    # print ''
    print(minDepth(root))

# Contributed by: Harshit Sidhwa
