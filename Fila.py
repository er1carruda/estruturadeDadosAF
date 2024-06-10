from Node_Fila import Node

class Fila:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def peek(self):
        if not self.is_empty():
            return self.first.value
        return None

    def push(self, value):
        new_node = Node(value)
        if self.last is None:
            self.first = self.last = new_node
            return
        self.last.next = new_node
        self.last = new_node

    def pop(self):
        if self.is_empty():
            return None
        removed_node = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return removed_node.value

    def size(self):
        current = self.first
        count = 0
        while current:
            count += 1
            current = current.next
        return count