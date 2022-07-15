num = int(input('Número:   '))
numl = []

for a in range(num):
    for b in range(num):
        if(a * b == num):
            numl.append('')

if(len(numl) ==0):
    print(num,'é primo')
else:
    print(num,'não é primo')