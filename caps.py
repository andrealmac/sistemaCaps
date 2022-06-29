def salvarUsuario(lista):
    arquivo = open('prontuario.txt', 'w')

    for usuario in lista:
        arquivo.write('{},{},{},{},{},{},{},{},{}\n'.format(usuario['nome'],usuario['prontuario'],usuario['telefone'],
        usuario['data_de_nascimento'],usuario['segunda'],usuario['terca'],usuario['quarta'],
        usuario['quinta'],usuario['injetavel']))
    arquivo.close()

def carregarUsuario():
    lista = []
    arquivo = open('prontuario.txt', 'r')

    for linha in arquivo.readlines():
        coluna = linha.split(',')
        usuario = {
        'prontuario': coluna[1],
        'nome': coluna[0],
        'telefone': coluna[2],
        'data_de_nascimento': coluna[3],
        'segunda': coluna[4],
        'terca': coluna[5],
        'quarta': coluna[6],
        'quinta': coluna[7],
        'injetavel': coluna[8],
        }
        lista.append(usuario)#adicinar na lista
    arquivo.close()
    return lista

def existe_prontuario(lista, prontuario):
    #percorrer a lista para verificar se existe aque prontuario
    if len(lista) > 0:
        for usuario in lista:
            if usuario['prontuario'] == prontuario:
                return True
    return False


def adicionar(lista):
    #id
    while True:
        prontuario  = input('Digite o numero do prontuario: ')
        
        if not existe_prontuario(lista, prontuario):
            break
        else:
            print('Prontuario sendo usado, tente de novo outro prontuário.')

    #id unico 
    usuario = {
        'prontuario': prontuario,
        'nome': input('Digite o nome: ').upper(),
        'telefone': input('Digite o telefone: '),
        'data_de_nascimento': input('Digite a data de nascimento do usuário: '),
        'segunda': input('Digite [s]sim ou [n]nao se o usuário vem na segunda: ').upper(),
        'terca': input('Digite [s]sim ou [n]nao se o usuário vem na terça: ').upper(),
        'quarta': input('Digite [s]sim ou [n]nao se o usuário vem na quarta: ').upper(),
        'quinta': input('Digite [s]sim ou [n]nao se o usuário vem na quinta: ').upper(),
        'injetavel': input('Digite [s]sim ou [n]nao sem tem injetável: ').upper()
        }
    lista.append(usuario)#adicinar na lista

    print('O usuário {} foi cadastrdo com sucesso!\n'.format(usuario['nome']))

def alterar():
    pass
def excluir():
    pass
def buscar():
    pass
def listar(lista):
    print('== Listar Usuários == ')
    if len(lista) > 0:
        for i, usuario in enumerate(lista):
            print('Usuário {}: '.format(i+1))
            print('\tNome: {}'.format(usuario['nome']))
            print('\tTelefone: {}'.format(usuario['telefone']))
            print('\tdata_de_nascimento: {}'.format(usuario['data_de_nascimento']))
            print('\tSegunda: {}'.format(usuario['segunda']))
            print('\tTerça: {}'.format(usuario['terca']))
            print('\tQuarta: {}'.format(usuario['quarta']))
            print('\tQuinta: {}'.format(usuario['quinta']))
            print('\tInjetável: {}'.format(usuario['injetavel']))
            print('======================================')

        print('Quantidade de contatos: {}\n'.format(len(lista)))
    else:
        print('Nao existe nenhum usuario cadastrado')

def principal():

    lista = carregarUsuario()#iniciar lista de onde parou 

    while True:
        print('Agenda Caps')
        print('1 - Adicionar Usuário')
        print('2 - Alterar Usuário')
        print('3 - Excluir Usuário')
        print('4 - Buscar Usuário')
        print('5 - Listar Usuário')
        print('6 - Sair')
        opcao = int(input('>> '))

        if opcao == 1:
            adicionar(lista)
            salvarUsuario(lista)
        elif opcao == 2:
            alterar()
            salvarUsuario(lista)
        elif opcao == 3:
            excluir()
            salvarUsuario(lista)
        elif opcao == 4:
            buscar()
        elif opcao == 5:
            listar(lista)
        elif opcao == 6:
            print('Sair do programa')
            break
        else:
            print('Opçao inválida')

principal()


