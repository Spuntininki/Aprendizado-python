from random import randint

numero_secreto = randint(0, 10)
cont_dos_erros = 0
while True:
    numero_entrada = int(input('Qual é o número secreto? filho da puta'))
    if numero_entrada == numero_secreto:
        print(f'Parabens corno, você precisou de {cont_dos_erros} para ganhar!')
        break
    else:
        cont_dos_erros += 1
