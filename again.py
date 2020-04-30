import calculadora
import menu

#função para refazer outro calculo ou retornar para o menu principal
def again():
    teste = input('Deseja fazer outro calculo? (y) para sim e (n) para nao \n')
    #teste.upper para que a letra digitada seja tanto minuscula quanto maiuscula
    if teste.upper() == 'Y':
        calculadora()
    elif teste.upper() == 'N':
        print('retornando para o menu principal\n\n')
        menu()