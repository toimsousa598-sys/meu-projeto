clientes = []

while True:
    print("\n=====SISTEM DE CLIENTES=====")
    print("1. Cadastro de Cliente")
    print("2. Listar Clientes")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        idade = input("Digite a idade do cliente: ")

        clinte = {

            "nome": nome,
            "idade": idade

        }

        clientes.append(clinte)
        print("Cliente cadastrado com sucesso!")
    elif opcao == "2":
        print("\n=====LISTA DE CLIENTES=====")

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}")
    elif opcao == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opção invalida. Por favor, tente novamente.")
        