from random import choice
import cores

def abre_o_jogo():
    print(f'*' * 30)
    print(f'*', end='')
    print(f'Jogo da Forca - Times'.center(28), end='')
    print('*')
    print(f'*' * 30)

def escolhe_a_palavra():
    lista = ['ATHLETICO',
             'ATLETICO',
             'BAHIA',
             'BOTAFOGO',
             'CEARA',
             'CORINTHIANS',
             'CRUZEIRO',
             'CURITIBA',
             'FLAMENGO',
             'FLUMINENSE',
             'FORTALEZA',
             'PALMEIRAS',
             'GOIAS',
             'BRAGANTINO',
             'SANTOS',
             'SAOPAULO',
             'SPORT',
             'VASCO',
             'AMERICA',
             'CHAPECOENSE',
             'VITORIA',
             'NAUTICO']
    sorteio = choice(lista)
    return sorteio


def vencedor():
    print(cores.Fazulclaro + '*' * 30 + cores.limpa)
    print(cores.Fazulclaro + '*' + cores.limpa, end='')
    print(cores.Lverde + 'Você Ganhou!'.center(28) + cores.limpa, end='')
    print(cores.Fazulclaro + '*' + cores.limpa)
    print(cores.Fazulclaro + '*' + cores.limpa, end='')
    print(palavra.center(28), end='')
    print(cores.Fazulclaro + '*' + cores.limpa)
    print(cores.Fazulclaro + '*' * 30 + cores.limpa)


def perdeu():
    print(cores.Fvermelho + '*' * 30 + cores.limpa)
    print(cores.Fvermelho + '*' + cores.limpa, end='')
    print(cores.Lvermelho + 'Você Perdeu!'.center(28), end='' + cores.limpa)
    print(cores.Fvermelho + '*' + cores.limpa)
    print(cores.Fvermelho + '*' + cores.limpa, end='')
    print(palavra.center(28), end='')
    print(cores.Fvermelho + '*' + cores.limpa)
    print(cores.Fvermelho + '*' * 30 + cores.limpa)


palavra = escolhe_a_palavra()
abre_o_jogo()
tamanho = len(palavra)
x = 0
vida=5
jogo=[]
while x < tamanho:
    jogo.append('-')
    x+=1
while True:
    print(jogo)
    chute = str(input('Digite uma letra: ')).upper().strip()[0]

    if chute in palavra:
        for i, c in enumerate(palavra):
            if c == chute:
                jogo[i] = chute
    else:
        vida-=1
    resultado = ''.join(jogo)
    if resultado == palavra:
        vencedor()
        break

    elif vida == 0:
        perdeu()
        break
