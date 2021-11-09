from random import shuffle


def boneco(cont):
    if cont == 5:
        print(r'''
         ______            
        /     O
        |    
        |     
      __|__
        ''')
    elif cont == 4:
        print(r'''
         ______            
        /     O
        |     |
        |     
      __|__
                ''')
    elif cont == 3:
        print(r'''
         ______            
        /     O
        |    /|
        |     
      __|__
                ''')
    elif cont == 2:
        print(r'''
         ______            
        /     O
        |    /|\
        |     
      __|__
                ''')
    elif cont == 1:
        print(r'''
         ______            
        /     O
        |    /|\
        |    / 
      __|__
                ''')
    elif cont == 0:
        print(r'''
         ______            
        /     O
        |    /|\
        |    / \
      __|__
                ''')
    else:
        print(r'''
         ______            
        /     
        |    
        |     
      __|__
                ''')


palavras = ['cachorro', 'gato', 'cavalo', 'rinoceronte', 'dinossauro']
letras = []
escolha = []
vidas = 6
shuffle(palavras)
for c in range(0, len(palavras[0])):
    letras.append(palavras[0][c])
    escolha.append('[]')

while True:
    boneco(vidas)
    letra = str(input('Digite uma letra: ')).strip().lower()[0]
    if letra in palavras[0]:
        for t, i in enumerate(letras):
            if letra == i:
                escolha[t] = f'{i}'
                print(f'{escolha[t]}', end='')
            elif escolha[t] == '[]':
                print(f'_', end='')
            else:
                print(f'{escolha[t]}', end='')
        print('')
    if letra not in palavras[0]:
        vidas -= 1
        print(f'Não foi encontra a letra digitada. \033[1;31mVocê perdeu uma vida!\033[m')
        print(f'Vidas atuais: {vidas} de 6')

    if vidas == 0:
        print('-='*30)
        print('\033[1;31mVOCÊ PERDEU!')
        boneco(vidas)
        break
    if escolha == letras:
        print("\033[1;32mVocê venceu!")
        break
