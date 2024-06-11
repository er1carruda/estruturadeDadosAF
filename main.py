from BinaryTree import BinaryTree
from pedido import Pedido


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

def mostrar_menu():
    print("\nMenu:")
    print("1. Receber novo pedido")
    print("2. Finalizar próximo pedido")
    print("3. Verificar fila de pedidos")
    print("4. Exibir pedidos em ordem crescente")
    print("5. Sair")


arvore = BinaryTree()
fila = FilaDePedidos()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Número do pedido: "))
        descricao = input("Descrição do pedido: ")
        novo_pedido = Pedido(numero, descricao)
        arvore.insert(novo_pedido.numero)
        fila.adicionar_pedido(novo_pedido)
        print("Pedido adicionado com sucesso.")
    elif opcao == "2":
        pedido_processado = fila.processar_pedido()
        if pedido_processado:
            print(f"Processando pedido: {pedido_processado.numero} - {pedido_processado.descricao}")
    elif opcao == "3":
        fila.exibir_fila()
    elif opcao == "4":
        print("Pedidos em ordem crescente:")
        arvore.inorder()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")