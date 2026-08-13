import json

def salvar_clientes(clientes):
    with open("clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)
def carregar_clientes():
    try:
        with open("clientes.json", "r") as arquuivo:
            return json.load(arquuivo)
    except FileNotFoundError:
        return []

clientes = carregar_clientes()

while True:
    print("\n=====SISTEM DE CLIENTES=====")
    print("1. Cadastro de Cliente")
    print("2. Listar Clientes")
    print("3. Buscar Cliente")
    print("4. Excluir Cliente")
    print("5. Editar Cliente")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        idade = input("Digite a idade do cliente: ")

        cliente = {

            "nome": nome,
            "idade": idade

        }

        clientes.append(cliente)
        salvar_clientes(clientes)
        print("Cliente cadastrado com sucesso!")
    elif opcao == "2":
        print("\n=====LISTA DE CLIENTES=====")

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}")
    elif opcao == "3":
        nome_busca = input("Digite o nome do cliente que deseja buscar: ")

        encontrado = False

        for cliente in clientes:
            if cliente['nome'].lower() == nome_busca.lower():
                print(f"Cliente econtrado: Nome: {cliente['nome']}, idade: {cliente['idade']}")
                print("\nCliente econtrado com sucesso!")
                print(f"Nome: {cliente['nome']}")
                print(f"Idade: {cliente['idade']}")
                encontrado = True
                break
        if not encontrado:
            print("Cliente não encontrado.")
    elif opcao == "4":
        nome_excluir = input("Digite o nome do cliente que deseja exluir: ")

        encontrado = False

        for cliente in clientes:
            if cliente['nome'].lower() == nome_excluir.lower():
                clientes.remove(cliente)
                salvar_clientes()

                print("Cliente excluido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Cliente não econtrado.")
    elif opcao == "5":
        nome_editar = input("Digite o nome do cliente que deseja editar:")

        encontrado = False

        for cliente in clientes:
            if cliente['nome'].lower() == nome_editar.lower():
                novo_nome = input("Digite o novo nome do cliente: ")
                nova_idade = input("Digite a nova idade do cliente: ")
                cliente['nome'] = novo_nome
                cliente['idade'] = nova_idade
                
                salvar_clientes()
        
                print("Cliente atualizado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Cliente não encontrado.")
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção invalida. Por favor, escolha uma opção válida.")
        print("Sistema desenvolvido para estudos de Python.")
        
    
        

       

