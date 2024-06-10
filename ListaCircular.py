from Node_Lista import Node

class ListaCircular:
    def __init__(self):
        self.head = None  # Cabeça da lista

    def insert(self, value):
        """Insere um novo nó no final da lista circular."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head  # Faz o nó apontar para si mesmo
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Completa o círculo apontando para a cabeça da lista
    
    def remove(self, value):
        """Remove um nó da lista pelo valor."""
        if self.head is None:
            return False  # Lista vazia

        current = self.head
        prev = None
        while True:
            if current.value == value:
                if prev is not None:
                    prev.next = current.next
                    if current == self.head:  # Se estiver removendo a cabeça
                        self.head = current.next
                else:
                    # Se a lista tiver apenas um nó
                    if current.next == self.head:
                        self.head = None
                    else:
                        self.head = current.next
                        prev = self.head
                        while prev.next != current:
                            prev = prev.next
                        prev.next = self.head
                return True
            prev = current
            current = current.next
            if current == self.head:
                break
        return False  # Dado não encontrado

    def display(self):
        """Exibe os elementos da lista."""
        if self.head is None:
            print("A lista está vazia")
            return
        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(volta para o início)")
