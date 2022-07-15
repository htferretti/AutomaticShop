import time

pessoas = [['adm','teste','teste','Teste Admi','11000000000','20']]
livros_disponiveis = [['The Silver Eyes','Scott Cawthon','2015',0],['The Twisted Ones','Scott Cawthon','2017',0],['The Fourth Closet','Scott Cawthon','2018',0]]
livros_alugados = []

def menu():
    validado = False
    while(validado == False):
        login = input('Login:   ')
        senha = input('Senha:   ')
        validado = validar(login, senha)
        if(validado == False):
            print('Login ou senha incorreto.\n')

    if(verific_adm(login)):
        menu_adm()
    else:
        menu_user(login)

def validar(login, senha):    
    tem_pessoa = False

    for pessoa in pessoas:
        if(login == pessoa[1] and senha == pessoa[2]):
            tem_pessoa = True
            print('\n',pessoa[3])

    return tem_pessoa

def verific_adm(login):
    for pessoa in pessoas:
        if(login == pessoa[1] and pessoa[0] == 'adm'):
            return True

    return False
            
def menu_adm():
    while True:
        menu_adm1()

        adm1 = input('\nDigite o número a qual deseja efetuar a ação:   ')
        if(adm1 == '1'):
            cadastrar_pessoa()
            break

        if(adm1 == '2'):
            excluir_pessoa()
            break

        if(adm1 == '3'):
            listar_pessoas()
            break

        if(adm1 == '4'):
            listar_livros()
            break

        if(adm1 == '5'):
            listar_livros_alugados()
            break

        if(adm1 == '6'):
            listar_livros_disponiveis()
            break

        if(adm1 == '7'):
            cadastrar_livro()
            break

        if(adm1 == '8'):
            excluir_livro()
            break

        if(adm1 == '9'):
            menu()
            break

def menu_adm1():
    print('\n1 - Cadastrar Pessoa\n2 - Excluir Pessoa\n3 - Listar Pessoas\n4 - Listar Livros\n5 - Listar Livros Alugados\n6 - Listar Livros Disponíveis\n7 - Cadastrar Livro\n8 - Excluir Livro\n9 - Logout')


def cadastrar_pessoa():
    adm_ou_user = input('Digite 1 se pessoa for adm:   ')
    login = input('Login:   ')
    senha = input('Senha:   ')
    nome = input('Nome:   ')
    cpf = input('Cpf:   ')
    idd = input('Idade:   ')
    if(adm_ou_user == '1'):
        pessoas.append(['adm',login,senha,nome,cpf,idd])
    else:
        pessoas.append(['user',login,senha,nome,cpf,idd])
    time.sleep(1)
    menu_adm()

def excluir_pessoa():
    numero_de_pessoas = 1
    for pessoa in pessoas:
        print('Digite',numero_de_pessoas,'para excluir',pessoa[3])
        numero_de_pessoas = numero_de_pessoas + 1

    excluir_pessoa1 = int(input('\nDigite o número a qual deseja efetuar a ação:   '))
    total = excluir_pessoa1 - 1
    if(excluir_pessoa1 > 0 and excluir_pessoa1 < (len(pessoas) + 1)):
        pessoas.remove(pessoas[total])
    time.sleep(1)
    menu_adm()

def listar_pessoas():
    for pessoa in pessoas:
        print(pessoa[0],pessoa[3])
        time.sleep(1)
    menu_adm()

def listar_livros():
    for livro in livros_alugados:
        print(livro[0])
        time.sleep(1)
    for livro in livros_disponiveis:
        print(livro[0])
        time.sleep(1)
    menu_adm()

def listar_livros_alugados():
    for livro in livros_alugados:
        print(livro[0],'alugado por',livro[-1])
        time.sleep(1)
    menu_adm()

def listar_livros_disponiveis():
    for livro in livros_disponiveis:
        print(livro[0])
        time.sleep(1)
    menu_adm()

def cadastrar_livro():
    nome = input('Nome:   ')
    autor = input('Autor:   ')
    data = input('Data:   ')
    livros_disponiveis.append([nome,autor,data,0])
    time.sleep(1)
    menu_adm()

def excluir_livro():
    numero_de_livros = 1
    for livro in livros_disponiveis:
        print('Digite',numero_de_livros,'para excluir',livro[0])
        numero_de_livros = numero_de_livros + 1

    excluir_livro1 = int(input('\nDigite o número a qual deseja efetuar a ação:   '))
    total = excluir_livro1 - 1
    if(excluir_livro1 > 0 and excluir_livro1 < (len(livros_disponiveis))):
        livros_disponiveis.remove(livros_disponiveis[total])
    time.sleep(1)
    menu_adm()


def menu_user(login):
    while True:
        menu_user1()

        user1 = input('\nDigite o número a qual deseja efetuar a ação:   ')
        if(user1 == '1'):
            alugar_livro(login)
            break

        if(user1 == '2'):
            devolver_livro(login)
            break

        if(user1 == '3'):
            menu()
            break

def menu_user1():
    print('\n1 - Alugar livro\n2 - Devolver livro\n3 - Logout')

def alugar_livro(login):
    if(len(livros_disponiveis) == 0):
        print('Não há livros disponíveis.')
        time.sleep(1)
        menu_user(login)
    
    else:
        numero_de_livros = 1
        for livro in livros_disponiveis:
            print('Digite',numero_de_livros,'para alugar',livro[0])
            numero_de_livros = numero_de_livros + 1

    alugar = int(input('\nDigite o número a qual deseja efetuar a ação:   '))
    total = alugar - 1
    if(alugar > 0 and alugar <= len(livros_disponiveis)):
        for pessoa in pessoas:
            if(login == pessoa[1]):
                livros_disponiveis[total][-1] = pessoa[3]
                livros_alugados.append(livros_disponiveis[total])
                livros_disponiveis.pop(total)
                time.sleep(1)
                menu_user(login)
    
    else:
        print('O número',alugar,'está inválido')
        time.sleep(1)
        menu_user(login)

def devolver_livro(login):
    alugado = False
    for pessoa in pessoas:
        if(pessoa[1] == login):
            for livro in livros_alugados:
                if(livro[-1] == pessoa[3]):
                    alugado = True

    if(alugado == True):
        for pessoa in pessoas:
            if(pessoa[1] == login):
                numero_de_livros = 0
                for livro in livros_alugados:
                    numero_de_livros = numero_de_livros + 1
                    if(livro[-1] == pessoa[3]):
                        print('Digite',numero_de_livros,'para devolver',livro[0])
    
        devolver = int(input('\nDigite o número a qual deseja efetuar a ação:   '))
        total = devolver - 1
        if(devolver > 0 and devolver <= len(livros_disponiveis)):
            for pessoa in pessoas:
                if(pessoa[1] == login):
                    if(livros_alugados[total][-1] == pessoa[3]):
                        livros_alugados[total][-1] = 0
                        livros_disponiveis.append(livros_alugados[total])
                        livros_alugados.pop(total)
                        time.sleep(1)
                        menu_user(login)

        else:
            print('O número',devolver,'está inválido')
            time.sleep(1)
            menu_user(login)

    else:
        print('Você não tem livros alugados.')
        time.sleep(1)
        menu_user(login)

menu()