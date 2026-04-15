import os 
import time 

cartoes_cadastrados = []

#variáveis 
debito = ""
credito = ""



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_cartao():
     print("\n    CADASTRO DE NOVO CARTÃO   ")

     nome_titular = input("Nome do Titular (como no cartão): ").strip().upper()
     if not nome_titular: 
         print(" Erro: O nome não pode estar vazio.")
         return

     numero_cartao = input("Número do Cartão (16 dígitos): ").replace(" ", "")
     if len(numero_cartao) != 16 or not numero_cartao.isdigit():
         print(" Erro: Cartão inválido! Digite os 16 números.")
         return

     validade = input("Validade (MM/AA): ").strip()
     if "/" not in validade or len(validade) != 5:
         print(" Erro: Formato de validade inválido (use MM/AA).")
         return

     cvv = input("CVV (3 dígitos): ").strip()
     if len(cvv) != 3 or not cvv.isdigit():
         print(" Erro: CVV inválido! ")
         return

     novo_cartao = {          #é para salvar o cartão
             "nome": nome_titular,
             "numero": numero_cartao,
             "validade": validade
            }
     cartoes_cadastrados.append(novo_cartao)
     print("\n  Cartão cadastrado com sucesso!")
     return novo_cartao
     


def menu_pagamento():
    while True: 
        limpar_tela()
        print("   ÁREA DE PAGAMENTO   ")
        print("1. Débito")
        print("2. Crédito")
        print("3. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1": 
            debito()
        elif opcao == "2": 
            credito()
        elif opcao == "3": 
            print("\nObrigado por usar o VoltLink! Saindo...")
            break
        else: 
            print("\n Opção inválida! Tente novamente.")
            break
            time.sleep(1)


def debito():
    while True: 
        print("\n   DÉBITO   ")
        print("1. Usar cartão cadastrado")
        print("2. Cadastrar novo cartão")
        print("3. Voltar")

        escolha = input("\nEscolha uma opção:")

        if escolha == "1":
            if not cartoes_cadastrados:
               print("\n Você não tem cartões salvos! ")
            else: 
                print("\n Seus cartões:")
                for i, cartao in enumerate(cartoes_cadastrados):
                    ''' Mostrar apenas os 4 últimos dígitos '''
                    print(f"{i+1}. Cartão final {cartao['numero'][-4:]}")
                input("\nSelecione o cartão (ou Enter para voltar)...")
        
        elif escolha == "2":
            cartao_atual = cadastrar_cartao()
            if cartao_atual: 

             #processar pagamento
        
             print("\n Processando pagamento,por favor aguarde...") 
             time.sleep(2)
             print("\n PAGAMENTO REALIZADO COM SUCESSO! ")
             print(f"Valor debitado do cartão final {cartao_atual['numero'][-4:]}")
             input("\n Pressione Enter para voltar ao menu principal...")
             break

        elif escolha == "3":
            break


def credito():
    while True: 
        limpar_tela()
        print("\n   CRÉDITO   ")
        print("1. Usar cartão cadastrado ")
        print("2. Cadastrar novo cartão ")
        print("3. Voltar")

        escolha = input("\Escolha uma opção: ")

        if escolha == "1":
            if not cartoes_cadastrados:
                print("\n Você não tem cartões salvos!")
                time.sleep(1.5)
            else: 
                for i, cartao in enumerate(cartoes_cadastrados):
                    print(f"{i+1}. {cartao['nome']} | Final: {cartao['numero'][-4:]}")
                input("\nSelecione o cartão (ou Enter para voltar )...")
        elif escolha == "2":
            cartao_atual = cadastrar_cartao()
            if cartao_atual: 

                # processar pagamento 
             print("\n Processando pagamento, por favor aguarde...")
             time.sleep(2)
             print("\n PAGAMENTO REALIZADO COM SUCESSO! ")
             print(f"Valor debitado do cartão final {cartao_atual['numero'][-4:]}")
             input("\n Pressione Enter para voltar ao menu principal...")
             break
        elif escolha == "3":
            break







if __name__ == "__main__": 
    menu_pagamento()