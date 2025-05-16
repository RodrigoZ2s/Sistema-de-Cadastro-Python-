import random

clientes_lista = [] # Armazena os cliente

def menu_visual():
    print("\n" + "="*40)
    print("     CADASTRO DE CLIENTES")
    print("="*40)
    print("1 - Cadastrar cliente")
    print("2 - Buscar clientes")
    print("3 - Listar clientes")
    print("4 - Remover clientes")
    print("0 - Sair")
    print("="*40)
    
def cadastrar_cliente():
    cliente_atual = {
        "nome": "",
        "idade": "",
        "cpf": "",
        "email": "",
    }

    cpf = input("CPF: ")
    while True:
        if validar_cpf(cpf) == True: # Verifica se o CPF é válido
            cliente_atual["cpf"] = cpf
            break
        else: 
            print("CPF inválido. Tente novamente.")
            break
            
    nome = input("Nome: ")
    cliente_atual["nome"] = nome

    idade = input("idade: ")
    cliente_atual["idade"] = idade

    email = input("Email: ")
    cliente_atual["email"] = email

    clientes_lista.append(cliente_atual) # Adiciona novos clientes a uma lista
    print("Cliente cadastrado com sucesso!")

    return cliente_atual

def validar_cpf(cpf):
    nove_digitos = cpf[:9]

    resultado_soma_1 = 0
    contador_1 = 10
    
    for digito in nove_digitos:
        resultado_soma_1 += int(digito) * contador_1
        contador_1 -= 1

    digito_1 = (resultado_soma_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_2 = 11

    resultado_soma_2 = 0
    for digito in dez_digitos:
        resultado_soma_2 += int(digito) * contador_2
        contador_2 -= 1

    digito_2 = (resultado_soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_calculado = f"{nove_digitos}{digito_1}{digito_2}"
    if cpf_calculado == cpf:
        return True
    return False
    
def listar_clientes(lista):
    for i, cliente in enumerate(lista, 1):
        print(f"Cliente {i}:")
        for chave, valor in cliente.items():
            print(f"  {chave.capitalize()}: {valor}")
        print("="*40)

def buscar_cliente():
    cpf_digitado = input("Digite seu CPF: ")
    for cliente in clientes_lista:
        if cliente["cpf"] == cpf_digitado:
            print("Cliente encontrado com sucesso")
            for chave, valor in cliente.items():
                print(f"{chave.capitalize()}: {valor}")
            return  # Sai da função assim que achar o cliente
    print(f"O CPF [{cpf_digitado}] não foi cadastrado no sistema")


def remover_cliente():
    cpf_cliente = input("CPF do cliente: ")
    for indice, cliente in enumerate(clientes_lista):
        if cliente["cpf"] == cpf_cliente:
            del clientes_lista[indice]
            print("Cliente removido com sucesso")
            return
    else:
        print("Cliente não encontrado")

while True:          
    menu_visual()

    escolha_menu = input("Escolha uma opção: ")         
    if escolha_menu == "1":
        cadastrar_cliente()
    elif escolha_menu == "2":
        buscar_cliente()
    elif escolha_menu == "3":
        listar_clientes(clientes_lista)
    elif escolha_menu == "4":
        remover_cliente()
    elif escolha_menu == "0":
        break
    else:
        print("Opção inválida")
        continue




    



