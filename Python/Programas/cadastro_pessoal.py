import time

pessoas = [["Henrique Tammenhain Ferretti", "15", "14044174946"]]

print(pessoas[0])

def menu():

    print('\nSistema de cadastro pessoal.')
    print('\n 1 - Cadastro de Pessoa\n 2 - Editar Pessoa\n 3 - Excluir Pessoa\n 4 - Listar Todas as Pessoas')
    menu1 = int(input('\nDigite o número a qual deseja efetuar a ação:   '))
    if(menu1 == 1):
        cadastro()

    if(menu1 == 2):
        editor()

    if(menu1 == 3):
        dele()

    if(menu1 == 4):
        lista()

def cadastro():

    cadastro1 = input('\nDigite seu nome completo:   ')
    cadastro2 = input('Informe sua Idade:   ')
    cadastro3 = input('Informe seu CPF:   ')

    pessoas.append([cadastro1, cadastro2, cadastro3])

    menu()

def editor():

    for i in range(len(pessoas)):
        print('\nDigite',(i + 1),'para editar o cadastro de',pessoas[i][0])

    editor1 = int(input(''))
    cadastro1 = input('\nDigite seu nome completo:   ')
    cadastro2 = input('Informe sua Idade:   ')
    cadastro3 = input('Informe seu CPF:   ')

    n = editor1 - 1
    r = pessoas[n]

    pessoas.remove(r)
    pessoas.insert(n, [cadastro1, cadastro2, cadastro3])

    menu()

def dele():

    for i in range(len(pessoas)):
        print('\nDigite',(i + 1),'para excluir o cadastro de',pessoas[i][0])

    dele1 = int(input(''))

    e = dele1 - 1
    d = pessoas[e]

    pessoas.remove(d)

    menu()

def lista():

    if(len(pessoas) == 0):
        print("\nAinda não existem pessoas cadastradas.")
        menu()

    else:
        for i in range(len(pessoas)):
            print('\n',pessoas[i][0],'\n   Idade:',pessoas[i][1],'\n   CPF:  ',pessoas[i][2])

        time.sleep(3)
        menu()

menu()