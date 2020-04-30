import calculadora
import maquina_de_vendas
import verificar_arq

#função do menu, onde fica todas as opções centrais
def menu():
    print("****Bem vindo usuário!!******")
    print("Seguinte, Você tem 4 Opções:\n(1)Calculadora\n(2)Maquina de vendas\n(3)Verificar Arquivos\n(4)Sair do sistema")
    opcao = int(input("Qual vai ser? "))
    if opcao == 1:
        calculadora()
    elif opcao == 2:
        maquina_de_vendas()
    elif opcao == 3:
        verificar_arq()
    elif opcao == 4:
        print('Obrigado pela visita')
        exit()
    else:
        print("pelo visto vc não quer nenhuma dessas opções ou vc nao saber ler")
