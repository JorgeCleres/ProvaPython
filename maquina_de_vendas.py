import menu

#função de máquina de vendas
    #o usuário insere um ID no lista e insere os produtos
    #caso não queira inserir mais produtos, basta digitar n quando for perguntado que retorna para o menu inicial
def maquina_de_vendas():
    arq = open("C:\\Users\\jrgcl\\PycharmProjects\\CursoPython - Seção 2\\registro3.txt", "a+")
    print("*****Maquina de Vendas ******")
    vx = 'y'
    id = input('DIGITE O ID DA LISTA: ')
    arq.write('%s.' %id)
    while vx != 'n':
        produto = input('ID: %s - Digite o produto: ' %id)
        arq.write('%s \n' %produto)
        vx = input('se deseja continuar digite (y) se quiser sair (n): ')
        arq.close()
    menu()