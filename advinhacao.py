from random import randint


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    opc = int(0)
    total_de_tentativas = 0
    pontos = 1000
    numero_secreto = randint(1, 100)
    while True:
        print('''ESCOLHA SUA DIFICULDADE:
        [1]= Modo facil
        [2]= Modo médio
        [3]= Modo dificil''')
        opc = int(input('Digite a sua opção: '))
        if opc == 1:
            total_de_tentativas = 20
            break
        elif opc == 2:
            total_de_tentativas = 10
            break
        elif opc == 3:
            total_de_tentativas = 5
            break
        else:
            print("Por favor escolha uma opção valida!")
            continue

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)
        if chute < 1 or chute > 100:
            print("Você precisa digitar um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Parabéns! Você acertou! o número secreto é de fato {numero_secreto}, "
                  f"você precisou de {rodada} tentativa(s) e fez {pontos} pontos")
            break
        else:
            if maior:
                print("O seu chute foi maior do que o número secreto!")
            elif menor:
                print("O seu chute foi menor do que o número secreto!")
        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos
        print('-' * 40)
    if not acertou:
        print(f'O número correto era {numero_secreto}')

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
