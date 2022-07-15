import time
import math
from fractions import Fraction

def menu():
    print('\n1 - Calcular hipotenusa com vetores Y e X.\n2 - Calcular Velocidade de vetores com velocidade e ângulo')
    menu1 = int(input('\nDigite o número a qual deseja efetuar a ação:   '))
    if(menu1 == 1):
        c1()

    if(menu1 == 2):
        c2()

def c1():
    y = int(input('Y:   '))
    x = int(input('X:   '))

    rx = x * x 
    ry = y * y 
    rt = (rx + ry)
    result = math.sqrt(rt)

    print('Resultado =',result)

    time.sleep(3)
    menu()

def c2():

    v = int(input('Velocidade:   '))
    a = int(input('Ângulo:   '))

    sen = format(math.sin(math.radians(a)))
    cos = format(math.cos(math.radians(a)))
    tng = format(math.tan(math.radians(a)))

    vx = v * cos
    vy = v * sen
    vh = v * tng

    print('Resultado vetor X =',vx,'\nResultado vetor Y =',vy,'\nResultado hipotenusa =',vh)

    time.sleep(3)
    menu()

menu()