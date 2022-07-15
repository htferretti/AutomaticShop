def numero_perfeito(num):
    result = 1

    for n in range(num):
        for d in range(num):
            if((n * d) == num):
                result = result + n

    if(result == num):
        print(num, 'é perfeito.')
    else:
        print(num, 'não é perfeito.') 

numero_perfeito(92)