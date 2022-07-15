import time
import pygame
import random

album1 = open('Kendrick\DAMN..txt')
album2 = open('Kendrick\good kid, m.A.A.d city.txt')
songs = []

for song in album1:
    song = song.rstrip('\n')
    songs.append(song)

for song in album2:
    song = song.rstrip('\n')
    songs.append(song)

def menu():

    print('1 - Listar todas as músicas em ordem alfabética\n2 - Buscar pelo nome de uma música\n3 - Ouvir trechos de todas as músicas')
    menu1 = int(input('\nDigite o número a qual deseja efetuar a ação:   '))

    if(menu1 == 1):

        for s in sorted(songs):
            print(s)
            time.sleep(1)

        menu()

    if(menu1 == 2):
        menu3 = input('\nDigite o nome da música:   ')
        for s in songs:
            if(s == menu3):
                if(s[-1] == '.'):
                    print('\n',s,'é do albúm DAMN.\n')
                    menu()

                else:
                    print('\n',s,'é do albúm good kid, m.A.A.d city.\n')
                    menu()

        else:
            print('Música não encontrada.')
            menu()

    if(menu1 == 3):
        print('\n1 - Ouvir os 2 albuns\n2 - Ouvir em ordem alfabética\n3 - DAMN.\n4 - good kid, m.A.A.d city')
        menu4 = int(input('\nDigite o número a qual deseja efetuar a ação:   '))
        if(menu4 == 1):
            for s in songs:
                print(s)
                pygame.mixer.init()
                pygame.init()
                pygame.mixer.music.load(s)
                pygame.mixer_music.play()
                time.sleep(5.5)

            menu()

        if(menu4 == 2):
            for s in sorted(songs):
                print(s)
                pygame.mixer.init()
                pygame.init()
                pygame.mixer.music.load(s)
                pygame.mixer_music.play()
                time.sleep(5.5)

            menu()

        if(menu4 == 3):
            for s in album1:
                s = s.rstrip('\n')
                print(s)
                pygame.mixer.init()
                pygame.init()
                pygame.mixer.music.load(s)
                pygame.mixer_music.play()
                time.sleep(5.5)

            menu()

        if(menu4 == 4):
            for s in album2:
                s = s.rstrip('\n')
                print(s)
                pygame.mixer.init()
                pygame.init()
                pygame.mixer.music.load(s)
                pygame.mixer_music.play()
                time.sleep(5.5)

            menu()
    else:
        print('Volte sempre! ╰(￣ω￣ｏ)')

menu()