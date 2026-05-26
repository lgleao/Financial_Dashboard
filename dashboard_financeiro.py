import os
import time

#listas
cadastro_n = []
cadastro_s = []
gastos = []
gastos_lazer = []
gastos_transporte = []
gastos_investimento = []
gastos_alimento = []
gastos_domestico = []

#funções
def clear():
    os.system('clear')

def tipos_despesas():
    print("- - - - - - - - - - -")
    print("1. LAZER")
    print("2. TRANSPORTE")
    print("3. INVESTIMENTO")
    print("4. ALIMENTAÇÃO")
    print("5. DOMÉSTICO")
    print("6. GERAL")
    print("- - - - - - - - - - -")


def opcoes():
    print("- - - - - - - - - - -")
    print("1. EXIBIR SALDO")
    print("2. ADICIONAR GASTO")
    print("3. EXIBIR EXTRATO")
    print("4. ENCERRAR PROGRAMA")
    print("- - - - - - - - - - -")

#login
while True:
    validacao = input("Já possui uma conta? S/N ").upper()
    if validacao == "N":
        cadastro_nome = input("Digite seu nome: ")
        cadastro_senha = input("Digite sua senha: ")
        if len(cadastro_n) == 0:
            cadastro_n.append(cadastro_nome)
            cadastro_s.append(cadastro_senha)
        else:
            cadastro_n[0] = cadastro_nome
            cadastro_s[0] = cadastro_senha
        print("Nome e senha registrados!")
        time.sleep(2)
        clear()

    elif validacao == "S":
        login_nome = input("Digite seu nome: ")
        login_senha = input("Digite sua senha: ")
        if login_nome == cadastro_n[0] and login_senha == cadastro_s[0]:
            print("Nome e senha aceitos!")
            time.sleep(2)
            clear()
            break
        else:
            print("Não coincidem!")
            time.sleep(2)
            clear()
        
#iniciando conta
saldo = float(input("Quanto dinheiro você possui na sua conta atualmente?\n"))
print("executando programa...")
time.sleep(2)
clear()

#opções
while True:
    opcoes()       
    escolha = int(input("Digite a opção desejada: "))
    if escolha == 1:
        print(f"Seu saldo atual é de R${saldo}")
        time.sleep(2)
        clear()
    elif escolha == 2:
        clear()
        tipos_despesas()
        gasto = float(input("Digite o tipo de despesa: \n"))
        if gasto == 1:
            gasto = float(input("Digite quanto gastou: "))
            gastos_lazer.append(gasto)
            saldo -= gasto
            print(f"Você agora possui R${saldo}.")
            time.sleep(2)
            clear()
        elif gasto == 2:
            gasto = float(input("Digite quanto gastou: "))
            gastos_transporte.append(gasto)
            saldo -= gasto
            print(f"Você agora possui R${saldo}.")
            time.sleep(2)
            clear()
        elif gasto == 3:
            gasto = float(input("Digite quanto gastou: "))
            gastos_investimento.append(gasto)
            saldo -= gasto
            print(f"Você agora possui R${saldo}.")
            time.sleep(2)
            clear()
        elif gasto == 4:
            gasto = float(input("Digite quanto gastou: "))
            gastos_alimento.append(gasto)
            saldo -= gasto
            print(f"Você agora possui R${saldo}.")
            time.sleep(2)
            clear()
        elif gasto == 5:
            gasto = float(input("Digite quanto gastou: "))
            gastos_domestico.append(gasto)
            saldo -= gasto
            print(f"Você agora possui R${saldo}.")
            time.sleep(2)
            clear()
        elif gasto == 6:
            gasto = float(input("Digite quanto gastou: "))
            gastos.append(gasto)
            saldo -= gasto
            print(f"Você agora possui R${saldo}.")
            time.sleep(2)
            clear()
        else:
            print("Inválido!")
            time.sleep(2)
            clear()

    elif escolha == 3:
        clear()
        tipos_despesas()
        extrato = int(input("Escolha o tipo de gasto: "))
        if extrato == 1:
            print(gastos_lazer)
            time.sleep(2)
            clear()
        elif extrato == 2:
            print(gastos_transporte)
            time.sleep(2)
            clear()
        elif extrato == 3:
            print(gastos_investimento)
            time.sleep(2)
            clear()
        elif extrato == 4:
            print(gastos_alimento)
            time.sleep(2)
            clear()
        elif extrato == 5:
            print(gastos_domestico)
            time.sleep(2)
            clear()
        elif extrato == 6:
            print(gastos_lazer,gastos_transporte,gastos_investimento,gastos_alimento,gastos_domestico,gastos)
            time.sleep(2)
            clear()
        else:
            print("Inválido!")
            time.sleep(2)
            clear()

    elif escolha == 4:
        print("Saindo...")
        time.sleep(2)
        clear()
        print("Volte em breve!")
        time.sleep(1)
        clear()
        break

print("Obrigado por usar o programa!")