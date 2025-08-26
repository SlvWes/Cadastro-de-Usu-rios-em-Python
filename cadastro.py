from colorama import Fore, Style, init

# Inicializa o colorama para que as cores funcionem no terminal
init(autoreset=True)  

# ---- Menu ----
def menu():
    print(Fore.CYAN + Style.BRIGHT + "==== Menu ====")
    print(Fore.YELLOW + "1 - Cadastrar")
    print(Fore.YELLOW + "2 - Listar")
    print(Fore.RED + "3 - Sair")

# ---- Cadastrando usuário ----
def cadastrar_usuario():
    nome = input(Fore.MAGENTA + "Digite o Nome Completo: ")
    email = input(Fore.MAGENTA + "Digite o Email: ")
    cpf = input(Fore.MAGENTA + "Digite o CPF: ")

    # Salvando informações nos arquivos
    with open("Nome.txt", "a") as arquivo:
        arquivo.write(f"{nome}\n")
    with open("Email.txt", "a") as arquivo:
        arquivo.write(f"{email}\n")
    with open("CPF.txt", "a") as arquivo:
        arquivo.write(f"{cpf}\n")
    
    print(Fore.GREEN + Style.BRIGHT + "Usuário cadastrado com sucesso!")

# ---- Listando usuários ----
def listar_usuario():
    # Lendo dados dos arquivos
    with open("Nome.txt", "r") as arquivo:
        nomes = arquivo.readlines()
    with open("Email.txt", "r") as arquivo:
        emails = arquivo.readlines()
    with open("CPF.txt", "r") as arquivo:
        cpfs = arquivo.readlines()

    # Exibindo os dados para o usuário
    for i in range(len(nomes)):
        nome = nomes[i].strip()   # Remove a quebra de linha
        email = emails[i].strip()
        cpf = cpfs[i].strip()
        print(Fore.MAGENTA + f"Nome: {nome}" + 
              Fore.CYAN + f" | Email: {email}" + 
              Fore.YELLOW + f" | CPF: {cpf}")

# ---- Loop principal ----
while True:
    menu()
    try:
        opcao = int(input(Fore.GREEN + Style.BRIGHT + "Digite a sua opção: "))
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "Por favor, digite um número válido!")
        continue

    if opcao == 1:
        cadastrar_usuario()
    elif opcao == 2:
        listar_usuario()
    elif opcao == 3:
        print(Fore.GREEN + Style.BRIGHT + "Saindo...")
        break
    else:
        print(Fore.RED + Style.BRIGHT + "Opção inválida!")
