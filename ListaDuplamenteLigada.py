from Node_Lista import Node

class ListaDuplamenteLigada:
    def __init__(self):
        self.head = None  # Cabeça da lista
        self.tail = None  # Cauda da lista

    def append(self, value):
        """Adiciona um nó ao final da lista."""
        new_node = Node(value)
        if self.tail is None:  # Se a lista está vazia
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, value):
        """Adiciona um nó ao início da lista."""
        new_node = Node(value)
        if self.head is None:  # Se a lista está vazia
            self.head = self.tail = new_node
        else:
  
            new_node.next = self.head
            self.head = new_node

    def display(self):
        """Exibe todos os elementos da lista."""
        current = self.head
        while current:
            print(current.value, end=' <-> ' if current.next else '')
            current = current.next
        print()

    def remove(self, value):
        """Remove um nó da lista pelo valor."""
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True  # Nó encontrado e removido
            current = current.next
        return False  # Nó não encontrado
    
