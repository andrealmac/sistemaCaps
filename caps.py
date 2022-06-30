def salvarUsuario(lista):
    arquivo = open('prontuario.txt', 'w')

    for usuario in lista:
        arquivo.write('{},{},{},{},{},{},{},{},{}\n'.format(usuario['nome'],usuario['prontuario'],usuario['telefone'],
        usuario['data_de_nascimento'],usuario['segunda'],usuario['terca'],usuario['quarta'],
        usuario['quinta'],usuario['injetavel']))
    arquivo.close()

def carregarUsuario():
    lista = []
    try:
        arquivo = open('prontuario.txt', 'r')

        for linha in arquivo.readlines():
            coluna = linha.strip().split(',')
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
    except FileNotFoundError:
        print('Erro em abrir o arquivo')
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

def alterar(lista):
    print('== Alterar Usuário == ')
    if len(lista) > 0:
        prontuario = input("Digite o numero do prontuario a ser alterado: ")
        if existe_prontuario(lista, prontuario):
            for usuario in lista:
                if usuario['prontuario'] == prontuario:
                    print('Nome: {}'.format(usuario['nome']))
                    print('Telefone: {}'.format(usuario['telefone']))
                    print('data_de_nascimento: {}'.format(usuario['data_de_nascimento']))
                    print('Segunda: {}'.format(usuario['segunda']))
                    print('Terça: {}'.format(usuario['terca']))
                    print('Quarta: {}'.format(usuario['quarta']))
                    print('Quinta: {}'.format(usuario['quinta']))
                    print('Injetável: {}'.format(usuario['injetavel']))
                    print('======================================\n')

                    #Alterar o usuario
                    usuario['nome'] = input('Digite o novo nome: ') 
                    usuario['telefone'] = input('Digite o novo telefone: ')   
                    usuario['data_de_nascimento'] = input('Digite a nova data de nascimento: ')   
                    usuario['segunda'] = input('Digite se [s]sim e [n]não se o dia do usuário é segunda: ')   
                    usuario['terca'] = input('Digite se [s]sim e [n]não se o dia do usuário é terça: ') 
                    usuario['quarta'] = input('Digite se [s]sim e [n]não se o dia do usuário é quarta: ') 
                    usuario['quinta'] = input('Digite se [s]sim e [n]não se o dia do usuário é quinta: ') 
                    usuario['injetavel'] = input('Digite se [s]sim e [n]não se o usuário toma injetável: ')
                    print('Os dados do usuário {}, foram alteradas com sucesso!.'.format(usuario['prontuario']))
                    break 
        else:
            print('Nao existe nenhum usuario com este número de prontuario {}\n'.format(prontuario))
    else:
        print("Não existe nenhum usuário cadastrado!!.\n")

def excluir(lista):
    print('== Excluir Usuário == ')
    if len(lista) > 0:
        prontuario = input("Digite o numero do prontuario a ser excluído: ")
        if existe_prontuario(lista, prontuario):
            for i, usuario in enumerate(lista):
                if usuario['prontuario'] == prontuario:
                    print('Nome: {}'.format(usuario['nome']))
                    print('Telefone: {}'.format(usuario['telefone']))
                    print('data_de_nascimento: {}'.format(usuario['data_de_nascimento']))
                    print('Segunda: {}'.format(usuario['segunda']))
                    print('Terça: {}'.format(usuario['terca']))
                    print('Quarta: {}'.format(usuario['quarta']))
                    print('Quinta: {}'.format(usuario['quinta']))
                    print('Injetável: {}'.format(usuario['injetavel']))
                    print('======================================\n')

                    # Excluido o contato precisa esta enumerado
                    del lista[i]
                    print('O usuário foi apagado com sucesso!!!')
                    break
        else:
            print('Nao existe nenhum usuario com este número de prontuario {}\n'.format(prontuario))
    else:
        print("Não existe nenhum usuário cadastrado!!.\n")

def buscar(lista):
    print('== Buscar Usuário == ')
    if len(lista) > 0:
        prontuario = input("Digite o numero do prontuario a ser procurado: ")
        if existe_prontuario(lista, prontuario):
            for usuario in lista:
                if usuario['prontuario'] == prontuario:
                    print('Nome: {}'.format(usuario['nome']))
                    print('Telefone: {}'.format(usuario['telefone']))
                    print('data_de_nascimento: {}'.format(usuario['data_de_nascimento']))
                    print('Segunda: {}'.format(usuario['segunda']))
                    print('Terça: {}'.format(usuario['terca']))
                    print('Quarta: {}'.format(usuario['quarta']))
                    print('Quinta: {}'.format(usuario['quinta']))
                    print('Injetável: {}'.format(usuario['injetavel']))
                    print('======================================\n')
                    break
        else:
            print('Nao existe nenhum usuario com este número de prontuario {}\n'.format(prontuario))
    else:
        print("Não existe nenhum usuário cadastrado!!.\n")

def listar(lista):
    print('== Listar Usuários == ')
    if len(lista) > 0:
        for i, usuario in enumerate(lista):
            print('Usuário {}: '.format(i+1))
            print('\tProntuario: {}'.format(usuario['prontuario']))
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
            alterar(lista)
            salvarUsuario(lista)
        elif opcao == 3:
            excluir(lista)
            salvarUsuario(lista)
        elif opcao == 4:
            buscar(lista)
        elif opcao == 5:
            listar(lista)
        elif opcao == 6:
            print('Sair do programa')
            break
        else:
            print('Opçao inválida')

principal()


