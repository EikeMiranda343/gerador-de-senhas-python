import random
import string

def gerar_senha():
    print('GERADOR DE SENHAS ALEATÓRIAS')

    while True:
        try:
            tamanho = int(input('Digite o tamanho da senha (4, 6, 8, 10 ou 12): '))
            if tamanho in [4, 6, 8, 10, 12]:
                break
            else:
                print('Você digitou um tamanho errado para a sua senha. Tente de novo!')
        except ValueError:
            print('Digite um número válido!')

    if tamanho == 4:
        senha = ''.join(random.choice(string.digits) for _ in range(4))
        print(senha)

    print('Escolha os tipos de caracteres que você quer usar na sua senha. Digite S para sim e N para não')
    usar_numeros = input('Usar números (S/N): ').strip().upper() == 'S'
    usar_minusculas = input('Usar letras minúsculas (S/N): ').strip().upper() == 'S'
    usar_maiusculas = input('Usar letras maiúsculas (S/N): ').strip().upper() == 'S'
    usar_especiais = input('Usar caracteres especiais (S/N): ').strip().upper() == 'S'

    caracteres = ''
    if usar_numeros:
        caracteres += string.digits
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print('Nenhum tipo de caractere foi selecionado... Por favor, selecione pelo menos um para prosseguir com a criação da senha.')
        gerar_senha()
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(senha)
    
gerar_senha()