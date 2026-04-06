import os

#variáveis
email_cadastrado = ""
senha_cadastrada = ""

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def tela_cadastro(): 
    global email_cadastrado, senha_cadastrada
    limpar_tela()
    print("   CADASTRO VOLTLINK   ")
    email_cadastrado = input("Digite seu email: ")
    while True:
        senha = input("Crie uma senha: ")
        confirmacao = input("Confirme sua senha: ")
        
        if senha == confirmacao:
            senha_cadastrada = senha
            print("\n✅ Senhas conferem! Cadastro realizado.")
            break  # Sai do loop e finaliza a função
        else:
            print("\n❌ As senhas não coincidem! Tente novamente.")
            # O loop volta para o início do 'while True'
            
    input("\nPressione Enter para voltar ao menu...")
   
#menu usuário
def menu_entrada():
    while True:
        limpar_tela()
        print("⚡ BEM-VINDO AO VOLTLINK ⚡")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            tela_login()
        elif opcao == "2":
            tela_cadastro()
        elif opcao == "3":
            print("\nObrigado por usar o VoltLink! Saindo...")
            break 
        else:
            print("\n⚠️ Opção inválida! Tente novamente.")
            input("Aperte Enter para continuar...")

# iniciar o programa chamando o menu
if __name__ == "__main__":
    menu_entrada()




