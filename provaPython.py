arq = open("C:\\Users\\jrgcl\\PycharmProjects\\CursoPython - Seção 2\\registro3.txt", "a+")


def calculadora():
    arq = open("C:\\Users\\jrgcl\\PycharmProjects\\CursoPython - Seção 2\\registro3.txt", "a+")
    print ('\n\n*******calculadora********\n')
    operador = input('(+) soma\n(-) subtração\n(/) divisão\n(*) multiplicação\nEscolha uma operação:  ')
    num1 = int(input('digite um numero: '))
    num2 = int(input('digite um numero: '))
    if operador == '+':
        total = num1 + num2
        print ("o resultado é: %d " %total)
        if total % 2 == 0:
            arq.write('%d + %d = %d \n' %(num1, num2, total))
            arq.close()
        again()
    elif operador == '-':
        total = num1 - num2
        print ("o resultado é: %d " %total)
        if total % 2 == 0:
            arq.write('%d - %d = %d \n' %(num1, num2, total))
            arq.close()
        again()
    elif operador == '/':
        if num1 == 0 or num2 == 0:
            print ('não é possível dividor por 0')
            calculadora()
        total = num1 / num2
        print ("o resultado é: %d " %total)
        if total % 2 == 0:
            arq.write('%d / %d = %d \n' %(num1, num2, total))
            arq.close()
        again()
    elif operador == '*':
        total = num1 * num2
        print ("o resultado é: %d " %total)
        if total % 2 == 0:
            arq.write('%d * %d = %d \n' %(num1, num2, total))
            arq.close()
        again()
    else:
        print ('operação inválida')
        calculadora()


def again():
    teste = input('Deseja fazer outro calculo? (y) para sim e (n) para nao \n')
    if teste.upper() == 'Y':
        calculadora()
    elif teste.upper() == 'N':
        print ('retornando para o menu principal\n\n')
        menu()


def menu():
    print ("****Bem vindo usuário!!******")
    print ("Seguinte, Você tem 4 Opções:\n(1)Calculadora\n(2)Maquina de vendas\n(3)Verificar Arquivos\n(4)Sair do sistema")
    opcao = int(input("Qual vai ser? "))
    if opcao == 1:
        calculadora()
    elif opcao == 2:
        maquina_de_vendas()
    elif opcao == 3:
        verificar_arq()
    elif opcao == 4:
        print ('Obrigado pela visita')
        exit()
    else:
        print ("pelo visto vc não quer nenhuma dessas opções ou vc nao saber ler")


def maquina_de_vendas():
    arq = open("C:\\Users\\jrgcl\\PycharmProjects\\CursoPython - Seção 2\\registro3.txt", "a+")
    print ("*****Maquina de Vendas ******")
    vx = 'y'
    id = input('DIGITE O ID DA LISTA: ')
    arq.write('%s.' %id)
    while vx != 'n':
        produto = input('ID: %s - Digite o produto: ' %id)
        arq.write('%s \n' %produto)
        vx = input('se deseja continuar digite (y) se quiser sair (n): ')
        arq.close()
    menu()


def verificar_arq():
    arq = open("C:\\Users\\jrgcl\\PycharmProjects\\CursoPython - Seção 2\\registro3.txt", "r")
    linhas = arq.readlines()
    print ('LISTA DO ARQUIVO')
    print (linhas)
    print ('\n')
    menu()

#iniciado o código
menu()
#fechando o arquivo para salva-lo
arq.close()
