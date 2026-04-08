import os

#variáveis
email_cadastrado = ""
senha_cadastrada = ""
número_contato = ""

# Lista de usuários já cadastrados (simulando um banco de dados)
usuarios_existentes = ["teste@gmail.com", "jose@ufrpe.br"]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def tela_cadastro(): 
    global email_cadastrado, senha_cadastrada, número_contato
    limpar_tela()
    print("   CADASTRO VOLTLINK   ")

    while True:
        email = input("Digite seu email:  ").strip().lower()
        if not email: 
             print(" Erro: O campo e-mail não pode estar vazio.")
        elif "@" not in email or "." not in email or " " in email:
             print(" Erro: E-mail inválido! Certifique-se de que não há espaços e que possui '@' e '.'")
        elif "ufrpe" not in email and "gmail" not in email:
             print( " Erro: Aceitamos apenas email da UFRPE ou Gmail.")
        elif not (email.endswith(".com") or email.endswith(".br")):
             print(" Erro: O e-mail deve terminar em .com ou .br")
        elif email in usuarios_existentes:
             print(" Erro: Email já cadastrado!")
        else: 
             email_cadastrado = email
             print(f" Email {email_cadastrado} validado!")
             break 


    while True:
        tel = input("Digite seu telefone (11 dígitos): ").strip()
        if not tel.isdigit():
            print(" Erro: Digite apenas números.")
        elif len(tel) != 11:
            print(" Erro: O telefone precisa de exatamente 11 dígitos.")
        else:
            numero_contato = tel
            break 
    
    while True:
        senha = input("Crie uma senha (4-8 caracteres, 1 numero, 1 maiuscula): ").strip()
        if not (4 <= len(senha) <= 8):
            print("Erro: A senha deve ter entre 4 a 8 caraceres.")
            continue
        if not any(char.isdigit() for char in senha):
            print("Erro: A senha deve conter pelo menos um número.")
            continue 
        if not any(char.isupper() for char in senha):
            print("Erro: A senha deve conter pelo menos uma letra maiúscula. ")
            continue

    
        confirmacao = input("Confirme sua senha: ").strip()
        if senha == confirmacao:
            senha_cadastrada = senha
            usuarios_existentes.append(email_cadastrado)
            print("Senha validada e cadastrada!")
            break
        else:
             print(" Erro: As senhas não coincidem. Tente novamente.")

    print("Cadastro realizado com sucesso!")
    print(f"Usuário: {email_cadastrado}")
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
            print("\n Opção inválida! Tente novamente.")
            input("Aperte Enter para continuar...")

          
# --- O FINAL DO ARQUIVO É AQUI ---
if __name__ == "__main__":
    menu_entrada()
            



