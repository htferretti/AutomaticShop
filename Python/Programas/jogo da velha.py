import random
import time

tabu = ['.','.','.','.','.','.','.','.','.']

def vic():
    print("\nCongrats jogador X !!!\n")

    print(tabu[0], tabu[1], tabu[2], '\n', tabu[3], tabu[4], tabu[5], '\n', tabu[6], tabu[7], tabu[8])

    pervx = input("\nDigite 1 se desejar jogar novamente:   ")
    if(pervx == "1"):
        menu()
    else:
        print("\nFlw!")

def vicm():
    print("\nPerdeu !!!\n")

    print(tabu[0], tabu[1], tabu[2], '\n', tabu[3], tabu[4], tabu[5], '\n', tabu[6], tabu[7], tabu[8])

    perm = input("\nDigite 1 se desejar jogar novamente:   ")
    if(perm == "1"):
        menu()
    else:
        print("\nFlw!")

print("\nBem-vindo ao jogo da velha ! :D \n")
def menu():
    print("Siga esse tabuleiro:\n")
    print("1 / 2 / 3")
    print("4 / 5 / 6")
    print("7 / 8 / 9\n")

    gamex()

def gamex(): 
    perg = int(input("X: Faça sua jogada:   "))
    if(perg == 1, 2, 3, 4, 5, 6, 7, 8, 9):
        result = perg - 1
        if(tabu[result] == '.'):
            tabu[result] = "X"
            print(tabu[0], tabu[1], tabu[2], '\n', tabu[3], tabu[4], tabu[5], '\n', tabu[6], tabu[7], tabu[8])

            if((tabu[0] == 'X') and (tabu[1] == 'X') and (tabu[2] == 'X')):
                vic()
            elif((tabu[3] == 'X') and (tabu[4] == 'X') and (tabu[5] == 'X')):
                vic()
            elif((tabu[6] == 'X') and (tabu[7] == 'X') and (tabu[8] == 'X')):
                vic()

            elif((tabu[0] == 'X') and (tabu[3] == 'X') and (tabu[6] == 'X')):
                vic()
            elif((tabu[1] == 'X') and (tabu[4] == 'X') and (tabu[7] == 'X')):
                vic()
            elif((tabu[2] == 'X') and (tabu[5] == 'X') and (tabu[8] == 'X')):
                vic()

            elif((tabu[0] == 'X') and (tabu[4] == 'X') and (tabu[5] == 'X')):
                vic()
            elif((tabu[2] == 'X') and (tabu[4] == 'X') and (tabu[6] == 'X')):
                vic()
            else:
                print('\nO está jogando...\n')
                time.sleep(1)
                machine()
                gamex()
            
        else:
            print("\nA casa já está ocupada")
            gamex()

    else:
        print("\nErro. Digite novamente.")
        gamex()

def machine():
    randc = random.randint(0,8)
    if(tabu[randc] == '.'):
        tabu[randc] = "O"

        print(tabu[0], tabu[1], tabu[2], '\n', tabu[3], tabu[4], tabu[5], '\n', tabu[6], tabu[7], tabu[8])
        
        if((tabu[0] == 'O') and (tabu[1] == 'O') and (tabu[2] == 'O')):
            vicm()
        if((tabu[3] == 'O') and (tabu[4] == 'O') and (tabu[5] == 'O')):
            vicm()
        if((tabu[6] == 'O') and (tabu[7] == 'O') and (tabu[8] == 'O')):
            vicm()

        if((tabu[0] == 'O') and (tabu[3] == 'O') and (tabu[6] == 'O')):
            vicm()
        if((tabu[1] == 'O') and (tabu[4] == 'O') and (tabu[7] == 'O')):
            vicm()
        if((tabu[2] == 'O') and (tabu[5] == 'O') and (tabu[8] == 'O')):
            vicm()

        if((tabu[0] == 'O') and (tabu[4] == 'O') and (tabu[5] == 'O')):
            vicm()
        if((tabu[2] == 'O') and (tabu[4] == 'O') and (tabu[6] == 'O')):
            vicm()

    else:
        machine()

menu()