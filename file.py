contatos = []
## definir a ação de adicionar o contato
def adicionar_contato(nome, idade, telefone, email, renda, estado):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    telefone = input("Telefone: ")
    email = input("Email: ")
    renda = float(input("Renda: "))
    estado = input("Estado (sigla, ex: SP): ").upper()

    contato = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone,
        'email': email,
        'renda': renda,
        'estado': estado
    }
    contatos.append(contato)
    print("Contato adicionado com sucesso!\n")

## definir a ação de adicionar o contato
def adicionar_contatoex(nome, idade, telefone, email, renda, estado):

    contato = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone,
        'email': email,
        'renda': renda,
        'estado': estado
    }
    contatos.append(contato)
    print("Contato adicionado com sucesso!\n")

## aq adiciona os contatos aparti de uma outra variavel sem input
adicionar_contatoex("Caio", 30, "11981805473", "caioleo@email.com", 4500.00, "sp")
adicionar_contatoex("Rosmary", 16, "11958083865", "rosmarykitty@email.com", 3200.00, "sp")
adicionar_contatoex("Fer", 32, "11967539814", "fernandaalq@email.com", 6400.00, "sp")
adicionar_contatoex("Carol", 23, "11937444531", "carolcomk@email.com", 2300.00, "sp")
adicionar_contatoex("Roger", 26, "11962961628", "rogergamer@email.com", 1200.00, "sp")

## define a exibição dos contatos
## linha 25: se não tiver nenhum contato mostrar o texto
def exibir_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.\n")
    for contato in contatos:
        print()
        print(f"Nome: {contato['nome']}") 
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
    print()

## busca pelo nome o contato inteiro
def buscar_contato():
    nome = input("Digite o nome do contato: ")
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            print()
            print(f"Nome: {contato['nome']}") 
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            print(f"Renda: {contato['renda']}")
            print(f"Email: {contato['estado']}")
            print()
            break
    else:
        print("Contato não encontrado.\n")

## remove o contanto pelo nome
def remover_contato():
    nome = input("Digite o nome do contato a ser removido: ")
    for i, contato in enumerate(contatos):
        if contato['nome'].lower() == nome.lower():
            del contatos[i]
            print("Contato removido com sucesso.\n")
            break
    else:
        print("Contato não encontrado.\n")

## corrige a informação do contanto desejada pelo usuario
def corrigir_contato():
    nome = input("Digite o nome do contato a ser corrigido: ")
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            campo = input("Qual informação deseja corrigir? (nome, idade, telefone, email, renda, estado): ").lower()
            if campo in contato:
                novo_valor = input(f"Digite o novo valor para {campo}: ")
                if campo == 'idade':
                    novo_valor = int(novo_valor)
                elif campo == 'renda':
                    novo_valor = float(novo_valor)
                elif campo == 'estado':
                    novo_valor = novo_valor.upper()
                contato[campo] = novo_valor
                print("Informação atualizada com sucesso.\n")
            else:
                print("Campo inválido.\n")
            break
    else:
        print("Contato não encontrado.\n")

## quantos contatos no total tem
def quantidade_contatos():
    print(f"Quantidade de contatos: {len(contatos)}\n")

## faz a media de idade dos contatos
def media_idade():
    if not contatos:
        print("Nenhum contato cadastrado.\n")
    else:
        media = sum(c['idade'] for c in contatos) / len(contatos)
        print(f"Média de idade dos contatos: {media:.2f}\n")

## quantos contatos tem em tal estado
def quantidade_por_estado():
    estados = {}
    for contato in contatos:
        estado = contato['estado']
        estados[estado] = estados.get(estado, 0) + 1
    print("Quantidade de contatos por estado:")
    for estado, quantidade in estados.items():
        print(f"{estado}: {quantidade}")
    print()

## menu bonito que coisa linda :)
def menu():
    while True:
        print("1. Adicionar contato")
        print("2. Exibir contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Corrigir contato")
        print("6. Mostrar quantidade de contatos")
        print("7. Mostrar média de idade")
        print("8. Mostrar quantidade por estado")
        print("9. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            exibir_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            remover_contato()
        elif opcao == '5':
            corrigir_contato()
        elif opcao == '6':
            quantidade_contatos()
        elif opcao == '7':
            media_idade()
        elif opcao == '8':
            quantidade_por_estado()
        elif opcao == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

# Iniciar o programa
menu()
