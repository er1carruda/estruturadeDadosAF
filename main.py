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
            print("\nNenhum pedido na fila.")
        else:
            print("\n=========== Fila de Pedidos ===========")
            for pedido in self.fila:
                print(f"\n🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸")
                print(f"🔸 Pedido: {pedido.numero}")
                print(f"🔸 Cliente: {pedido.nome}")
                print(f"🔸 Descrição: {pedido.descricao}")
                print(f"🔸 Endereço: {pedido.endereco}")
                print(f"🔸 Telefone: {pedido.telefone}")
                print("🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸")
            print("=========================================")
    
    def excluir_pedido(self, numero):
        for i, pedido in enumerate(self.fila):
            if pedido.numero == numero:
                del self.fila[i]
                print(f"Pedido {numero} excluído com sucesso.")
                return True
        print(f"Pedido {numero} não encontrado.")
        return False

    def editar_pedido(self, numero, descricao, nome, endereco, telefone):
        for pedido in self.fila:
            if pedido.numero == numero:
                pedido.descricao = descricao
                pedido.nome = nome
                pedido.endereco = endereco
                pedido.telefone = telefone
                return True
        return False

def mostrar_menu():
    print("\n\n========== 🍕 Menu Papa's Pizzaria🍕 ==========")
    print("             1. Receber novo pedido")
    print("             2. Finalizar próximo pedido")
    print("             3. Verificar fila de pedidos")
    print("             4. Excluir pedido")
    print("             5. Editar pedido")
    print("             6. Encerrar Expediente")
    print("================================================\n\n")

def solicitar_informacao(mensagem):
    while True:
        resposta = input(mensagem).strip()
        if resposta:
            return resposta
        print("Campo obrigatório. Por favor, preencha a informação.")

arvore = BinaryTree()
fila = FilaDePedidos()
proximo_numero_pedido = 1

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = proximo_numero_pedido
        descricao = solicitar_informacao("Descrição do pedido: ")
        nome = solicitar_informacao("Nome do Cliente: ")
        endereco = solicitar_informacao("Endereço: ")
        telefone = solicitar_informacao("Telefone de contato: ")
        novo_pedido = Pedido(numero, descricao, nome, endereco, telefone)
        arvore.insert(novo_pedido.numero)  # Inserindo na árvore binária
        fila.adicionar_pedido(novo_pedido)  # Adicionando na fila
        print("Pedido adicionado com sucesso.")
        proximo_numero_pedido += 1
    elif opcao == "2":
        pedido_processado = fila.processar_pedido()
        if pedido_processado:
            print(f"\nProcessando pedido {pedido_processado.numero} de {pedido_processado.nome}: {pedido_processado.descricao}")
    elif opcao == "3":
        fila.exibir_fila()
    elif opcao == "4":
        numero_excluir = int(solicitar_informacao("Número do pedido a excluir: "))
        fila.excluir_pedido(numero_excluir)
    elif opcao == "5":
        numero_editar = int(solicitar_informacao("Número do pedido a editar: "))
        for pedido in fila.fila:
            if pedido.numero == numero_editar:
                descricao = solicitar_informacao("Nova descrição do pedido: ")
                nome = solicitar_informacao("Novo nome do Cliente: ")
                endereco = solicitar_informacao("Novo endereço: ")
                telefone = solicitar_informacao("Novo telefone de contato: ")
                fila.editar_pedido(numero_editar, descricao, nome, endereco, telefone)
                print(f"Pedido {numero_editar} editado com sucesso.")
                break
        else:
            print(f"Pedido {numero_editar} não encontrado.")
    elif opcao == "6":
        print("Encerrando o trabalho de hoje...")
        break
    else:
        print("Opção inválida. Tente novamente.")
