class Node:  # дополнительная информация об узле списка
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class Stack: # класс стека
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.items.__len__()

    def __repr__(self):
        return self.items.__repr__()

    def push(self, item):
        self.items.add(item, 0)

    def pull(self):
        self.items.remove(0)


class Queue:  # класс очереди
    def __init__(self):
        self.queue = list()

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed

    def size(self):
        return len(self.queue)


class LinkedList: # класс списка
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return ",".join(nodes)

    def append(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
