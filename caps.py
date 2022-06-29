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

    lista = []#iniciar lista vazia que ira incrementando 

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
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            excluir()
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


