import again

#usamos uma função para a calculado para facilitar a repetição da mesma
#para usar a calculadora deve usar o simbolos corretos para cada operação
def calculadora():
    #criando um arquivo com o tipo "a+" para inserir novas linhas caso o resultado de alguma operação seja PAR
    #e é usado o arq.close() nos finais de alguns "if" para quer o arquivo seja salvo
    arq = open("C:\\Users\\jrgcl\\PycharmProjects\\CursoPython - Seção 2\\registro3.txt", "a+")
    print('\n\n*******calculadora********\n')
    operador = input('(+) soma\n(-) subtração\n(/) divisão\n(*) multiplicação\nEscolha uma operação:  ')
    num1 = int(input('digite um numero: '))
    num2 = int(input('digite um numero: '))
    if operador == '+':
        total = num1 + num2
        print("o resultado é: %d " %total)
        if total % 2 == 0:
            arq.write('%d + %d = %d \n' %(num1, num2, total))
            arq.close()
        again()
    elif operador == '-':
        total = num1 - num2
        print("o resultado é: %d " %total)
        if total % 2 == 0:
            arq.write('%d - %d = %d \n' %(num1, num2, total))
            arq.close()
        again()
    elif operador == '/':
        if num1 == 0 or num2 == 0:
            print('não é possível dividor por 0')
            calculadora()
        total = num1 / num2
        print("o resultado é: %d " %total)
        if total % 2 == 0:
            arq.write('%d / %d = %d \n' %(num1, num2, total))
            arq.close()
        again()
    elif operador == '*':
        total = num1 * num2
        print("o resultado é: %d " %total)
        if total % 2 == 0:
            arq.write('%d * %d = %d \n' %(num1, num2, total))
            arq.close()
        again()
    else:
        print('operação inválida')
        calculadora()
