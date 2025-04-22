import random
import string

def gerar_senha():
    print('GERADOR DE SENHAS ALEATÓRIAS')

    while True:
        try:
            tamanho = int(input('Digite o tamanho da senha (4, 6, 8. 10 ou 12): '))
            if tamanho in [4, 6, 8, 10, 12]:
                break
            else:
                print('Você digitou um tamanho errado para a sua senha. Tente de novo!')
        except ValueError:
            print('Digite um número válido!')

    if tamanho == 4:
        senha = ''.join(random.choice(string.digits) for _ in range(4))
        print(senha)
    


gerar_senha()