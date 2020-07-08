class Node:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        # Initializes two dummy nodes, a head node and a tail node
        self.head = Node('*', '*')
        self.tail = Node('*', '*')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def add(self, node):
        # Inserts new node just before the tail node, increases length by 1
        before_tail_node = self.tail.prev
        before_tail_node.next = node
        node.prev = before_tail_node
        node.next = self.tail
        self.tail.prev = node
        self.length += 1

    def delete(self, node):
        if self.length == 0:
            raise IndexError("Out of bounds")
        else:
            # Removes specified node by linking the two nodes before and after it together, decreases length by 1
            if not node:
                node = self.head.next
            before_node = node.prev
            after_node = node.next
            before_node.next = after_node
            after_node.prev = before_node
            self.length -= 1

            return node

class LRUCache:

    def __init__(self, capacity):
        # Initializes the hashmap and doubly-linked-list data structures
        self.lookup = {}
        self.doublyList = DoublyLinkedList()
        self.capacity = capacity

    def put(self, key, value):
        # Deletes the node if key is present or the first node in the linked-list if length has reached LRUCache capacity
        if key in self.lookup:
            current_node = self.lookup[key]
            self.doublyList.delete(current_node)
        elif self.doublyList.length == self.capacity:
            first_index = self.doublyList.delete(None)
            del self.lookup[first_index.key]

        # Adds the node to the end of the linked-list
        node = Node(key, value)
        self.lookup[key] = node
        self.doublyList.add(node)

    def get(self, key):
        # Adds specified node at the end of the list and returns the value if present or else return -1
        if key in self.lookup:
            node = self.lookup[key]
            self.doublyList.delete(node)
            self.doublyList.add(node)
            return node.value
        else:
            return -1


#Sample testcases
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

