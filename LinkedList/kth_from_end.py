class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


a = Node(1)
a.next = Node(4)
a.next.next = Node(5)


def kth_from_end(head, k):

    if not head or k == 0:
        return None

    first = head
    second = head

    for _ in range(k):
        if not second:
            return None
        second = second.next

    while second:
        first = first.next
        second = second.next

    return first

print(kth_from_end(a, 3))
