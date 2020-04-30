import menu

#essa função serve para mostrar todos os dados que foram salvo no arquivo
def verificar_arq():
#abrindo arquivo
    arq = open("C:\\Users\\jrgcl\\PycharmProjects\\CursoPython - Seção 2\\registro3.txt", "r")
#salvando o arquivona variavel linhas
    linhas = arq.readlines()
#mostrando o arquivos em linhas
    print('LISTA DO ARQUIVO')
    print(linhas)
    print('\n')
    menu()
#essa seria a parte do código que exclui somente uma linha, mas não deu muito certo
    #excluir = input('Para excluir uma linha digite (y) para voltar ao menu (n)')
    #excluir.upper para que a letra digitada seja tanto minuscula quanto maiuscula
    #if excluir.upper() == 'Y':
     #   ide = input('Digite o Id: ')
      #  arq = open("C:\\Users\\jrgcl\\PycharmProjects\\CursoPython - Seção 2\\registro3.txt", "w")
       # for linha in linhas:
        #    if linha == ide+'.':
         #       print('salvou')
          #      arq.write(linha)
           #     print(linha)
            #    arq.close()
             #   menu()
            #else:
             #   print(linha)
              #  print('excluiu')
               # menu()
    #else:
     #   menu()