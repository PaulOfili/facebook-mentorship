"""
Largest absolute difference in binary tree between any node and its ancestor
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Node(1000)
a.left = Node(9)
a.left.left = Node(3)
a.left.right = Node(-460)
a.left.left.right = Node(1000)
a.right = Node(400)


def maximumDifference(root):

    def helper(node, limit):

        if node:
            current_max = max(abs(limit[0]-node.value), abs(limit[1]-node.value))

            left_max = helper(node.left, [min(limit[0], node.value), max(limit[1], node.value)])
            right_max = helper(node.right, [min(limit[0], node.value), max(limit[1], node.value)])

            return max(left_max, right_max, current_max)

        return float('-inf')

    return helper(root, [root.value, root.value])

print(maximumDifference(a))