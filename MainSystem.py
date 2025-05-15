import random


def cadastrar_cliente():
    cliente = {
        "nome": "",
        "idade": "",
        "cpf": "",
        "email": "",
    }

    nome = input("Nome: ")
    cliente["nome"] = nome

    idade = input("idade: ")
    cliente["idade"] = idade

    cpf = input("CPF: ")
    cliente["cpf"] = cpf

    email = input("Email: ")
    cliente["email"] = email

    return cliente

def validar_cpf(cpf):
    nove_digitos = cpf

    resultado_soma_1 = 0
    contador_1 = 0
    
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

    cpf_gerado = f"{nove_digitos}{digito_1}{digito_2}"

    if cpf_gerado != cpf:
        return True

def listar_clientes(cpf):
    pass

def buscar_cliente(cpf):
    pass

def remover_cliente(cpf):
    pass