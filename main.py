class Pedido:
    def __init__(self, numero, descricao):
        self.numero = numero
        self.descricao = descricao

class Nodo:
    def __init__(self, pedido):
        self.pedido = pedido
        self.esquerda = None
        self.direita = None

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None
    
    def adicionar_pedido(self, pedido):
        if not self.raiz:
            self.raiz = Nodo(pedido)
        else:
            self._adicionar(self.raiz, pedido)
    
    def _adicionar(self, nodo, pedido):
        if pedido.numero < nodo.pedido.numero:
            if nodo.esquerda is None:
                nodo.esquerda = Nodo(pedido)
            else:
                self._adicionar(nodo.esquerda, pedido)
        else:
            if nodo.direita is None:
                nodo.direita = Nodo(pedido)
            else:
                self._adicionar(nodo.direita, pedido)
    
    def buscar_pedido(self, numero):
        return self._buscar(self.raiz, numero)
    
    def _buscar(self, nodo, numero):
        if nodo is None or nodo.pedido.numero == numero:
            return nodo
        if numero < nodo.pedido.numero:
            return self._buscar(nodo.esquerda, numero)
        else:
            return self._buscar(nodo.direita, numero)

class FilaDePedidos:
    def __init__(self):
        self.fila = []
    
    def adicionar_pedido(self, pedido):
        self.fila.append(pedido)
    
    def processar_pedido(self):
        if not self.fila:
            print("Nenhum pedido na fila.")
            return None
        return self.fila.pop(0)
    
    def exibir_fila(self):
        if not self.fila:
            print("Nenhum pedido na fila.")
        else:
            for pedido in self.fila:
                print(f"Pedido: {pedido.numero}, Descrição: {pedido.descricao}")

# Exemplo de uso
arvore = ArvoreBinariaDeBusca()
fila = FilaDePedidos()

pedido1 = Pedido(101, "Pizza Margherita")
pedido2 = Pedido(102, "Hambúrguer")
pedido3 = Pedido(103, "Sushi")

arvore.adicionar_pedido(pedido1)
arvore.adicionar_pedido(pedido2)
arvore.adicionar_pedido(pedido3)

fila.adicionar_pedido(pedido1)
fila.adicionar_pedido(pedido2)
fila.adicionar_pedido(pedido3)

fila.exibir_fila()

pedido_processado = fila.processar_pedido()
if pedido_processado:
    print(f"Processando pedido: {pedido_processado.numero} - {pedido_processado.descricao}")

fila.exibir_fila()

pedido_buscado = arvore.buscar_pedido(102)
if pedido_buscado:
    print(f"Pedido encontrado: {pedido_buscado.pedido.numero} - {pedido_buscado.pedido.descricao}")
