from random import randint
from time import sleep


def jogar():
    mensagem_abertura('Bem vindo ao jogo da forca!')

    palavra_secreta = escolhe_palavra()

    letras_acertadas = ['_' for _ in palavra_secreta]
    print(letras_acertadas)

    enforcou = venceu = False
    erros = 0

    while not enforcou and not venceu:
        chute = input('Qual é a letra?').strip().upper()[0]
        if chute in palavra_secreta.upper():
            verifica_letra(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
        print(letras_acertadas)
        enforcou = erros == 7
        venceu = '_' not in letras_acertadas
    if venceu:
        sleep(0.5)
        imprime_mensagem_vencedor()
    else:
        sleep(0.5)
        imprime_mensagem_perdedor(palavra_secreta)


def mensagem_abertura(mensagem, cor = '\033[1;32m'):
    print(f"{cor}~"*len(mensagem))
    print(f"{mensagem}")
    print(f"~"*len(mensagem), "\033[m")


def escolhe_palavra(nome_arquivo ='arquivo.txt'):
    arquivo = open(nome_arquivo, 'r')

    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha.strip())

    arquivo.close()

    sorteio = randint(0, len(palavras))
    palavra_secreta = palavras[sorteio]

    return palavra_secreta


def verifica_letra(chute, palavra_secreta, letras_acertadas):

        index = 0
        for letra in palavra_secreta:
            if chute == letra.upper():
                letras_acertadas[index] = letra
            index += 1


def imprime_mensagem_perdedor(palavra_secreta):
    print("\033[1;31mPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           \033[m")


def imprime_mensagem_vencedor():
    print("\033[1;32mParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \033[m")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()