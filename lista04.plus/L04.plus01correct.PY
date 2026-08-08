from time import sleep
cores = {
    # Reseta a cor para o padrão do sistema (OBRIGATÓRIO usar no final)
    'limpa': '\033[m',
    
    # Estilos de Texto
    'negrito': '\033[1m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'magenta': '\033[35m'}

print (f'==================================== lista de exercício plus ====================================')
print(f'------------------------------------------- Questão 1 -------------------------------------------\n')
print ("Nossa necessidade é utilizar o recurso de liberação de portas dos Laboratórios de\nInformática utilizando os dispositivos instalados em cada porta com fechadura eletrônica.\nPara tal, desenvolveremos um sistema que identifique e autorize a entrada dos\nprofessores já cadastrados no sistema de uso dos laboratórios.\nO sistema deve possuir:")
print ("\n\n\t• Um cadastro completo de professores (adicionar, alterar, excluir e listar) que\n\tassocie o código do professor ao seu nome, alguns professores já devem ser précadastrados, veja a lista abaixo;\n\n\t• Um cadastro completo dos acessos dos professores aos laboratórios (adicionar,\n\talterar, excluir e listar), serão utilizados 6 laboratórios com as nomenclaturas\n\tLab102, Lab103, Lab104, Lab105, Lab106, Lab107 – os laboratórios são fixos no\n\tsistema, o que pode ser alterado são os acessos, alguns professores já devem\n\tser pré-cadastrados nos laboratórios, veja a outra lista abaixo (para facilitar a\n\timplementação, sugere-se que os laboratórios sejam associados ao código do\n\tprofessor e não ao seu nome);\n\n\t• Teste de acesso ao laboratório: deve ser possível informar o nome de um\n\tlaboratório e um código de professor para verificar se o acesso é permitido ou não\n\t(por exemplo, nesse teste deveria ser possível escolher o Lab103 e informar o\n\tcódigo de professor 002, nesse caso, o sistema deve negar o acesso).")
print(f'\n------------------------------------------------------------------------------------------------\n')
print (f'\n\nPré-cadastro de Professores (códigos x nomes)\n001 – Prof Thiago Paes\n002 – Prof Schalata\n003 – Prof Ignácio\n004 – Prof Ryan\n005 – Prof André\n006 – Profª Fabiana\n007 – Prof Alberto\n008 – Prof Juliano\n009 – Prof Thiago Waltrik\n010 – Prof João Eduardo\n\nPré-cadastro de Acessos (laboratório x professor)\n• Lab102 – Prof Ignácio, Prof Thiago Paes, Profª Ryan, Prof André, Profª\nFabiana;\n• Lab103 – Prof Alberto;\n• Lab104 – Prof Ryan, Prof Juliano, Prof Schalata, Prof André;\n• Lab105 – Prof Ignácio, Prof Alberto, Prof Thiago Waltrik, Prof Thiago Paes.\n• Lab106 – Prof Schalata, Prof Ignácio, Prof Thiago Waltrik, Prof Thiago Paes;\n• Lab107 – Prof André, Prof Schalata, Prof Thiago Waltrik, Prof Thiago Paes, Prof\nJoão Eduardo.')
print(f'\n------------------------------------------------------------------------------------------------\n')

professors = {'001' : 'Prof Thiago Paes',
            '002' : 'Prof Schalata',
            '003' : 'Prof Ignácio',
            '004' : 'Prof Ryan',
            '005' : 'Prof André',
            '006' : 'Profª Fabiana',
            '007' : 'Prof Alberto',
            '008' : 'Prof Juliano',
            '009' : 'Prof Thiago Waltrik',
            '010' : 'Prof João Eduardo'}

lab102 = ['001','003','004','005','006']
lab103 = ['007']
lab104 = ['002', '004', '005', '008']
lab105 = ['001', '003','007', '009']
lab106 = ['001', '002', '003','009']
lab107 = ['001', '002', '005','009', '010']


while True:
    options = int(input(f'\t\t{cores["negrito"]}Selecione a baixo, o que você deseja fazer:\n\t\t------------------------------------------------------------------{cores["limpa"]}\n\t\t {cores["magenta"]}{cores["negrito"]}1{cores["limpa"]} - Professores (Listar, Alterar, Remover e Adicionar) {cores["limpa"]}\n\t\t {cores["magenta"]}{cores["negrito"]}2{cores["limpa"]} - Laboratórios (Remover e Adicionar professores, Visualizar permissões...)\n\t\t {cores["magenta"]}{cores["negrito"]}0{cores["limpa"]} - Sair \n ⤷ '))

#Professores
    if options == 1:
        answer = int(input(f'\t\t{cores["negrito"]}PROFESSORES{cores["limpa"]}\n\t\t------------------------------------------------------------------\n\t\t {cores["magenta"]}{cores["negrito"]}1{cores["limpa"]} - Listar Professores\n\t\t {cores["magenta"]}{cores["negrito"]}2{cores["limpa"]} - Adicionar Professores\n\t\t {cores["magenta"]}{cores["negrito"]}3{cores["limpa"]} - Remover Professores\n\t\t {cores["magenta"]}{cores["negrito"]}4{cores["limpa"]} - Alterar Professores\n\t\t {cores["magenta"]}{cores["negrito"]}0{cores["limpa"]} - Voltar\n ⤷ '))

        print(f'\n')

        if answer == 0:
            break

        elif answer == 1:
            for k, v in professors.items():
                print(f'{k} - {v}')

        # CADASTRO
        elif answer == 2:
            adittion_code = input('\nDigite o código: ')

            if adittion_code in professors:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código já cadastrado!{cores["limpa"]}')

            else:
                adittion_name = input('\nDigite o nome do(a) professor(a): ')
                professors[adittion_code] = adittion_name
                print(f'{cores["verde"]}Adicionado com sucesso! {cores["limpa"]}')

        # EXCLUIR
        elif answer == 3:
            delete = input('Coloque o código do professor a ser excluido.')

            if delete in 'lab102' or 'lab103' or 'lab104' or 'lab105' or 'lab106' or 'lab107':
                print(f'{cores["negrito"]}{cores["magenta"]}ALERTA:{cores["limpa"]} O professor {delete} - {professors[delete]} esta cadastrado em algum(ns) laboratorio(s)')

                yes_or_no = int(input(f'Digite {cores["negrito"]} 1{cores["limpa"]} para prosseguir com a exclusao e{cores["negrito"]} 2{cores["limpa"]} para deixar pra la.'))

                if yes_or_no == 1:
                    if delete in professors:
                        del professors[delete]

                        print(f'{cores["verde"]}{cores["negrito"]}Exclusão bem sucedida!{cores["limpa"]}')

                        if delete in lab102:
                            lab102.pop(delete)

                        if delete in lab103:
                            lab103.pop(delete)

                        if delete in lab104:
                            lab104.pop(delete)

                        if delete in lab105:
                            lab105.pop(delete)

                        if delete in lab106:
                            lab106.pop(delete)

                        if delete in lab107:
                            lab107.pop(delete)

                else:
                    sleep(0.5)
                    print(f'{cores["negrito"]}ERRO: {cores["magenta"]}Voltando as opcoes...{cores["limpa"]}')

        # ALTERAR
        elif answer == 4:
            change = input('Qual nome deve ser alterado? Digite o código: ')

            if change in professors:
                print(f'{cores["negrito"]}Código encontrado.{cores["limpa"]}')

                new_name = input('\nColoque o novo nome: ')
                professors[change] = new_name

                print(f'\n{cores["magenta"]}Alterando...{cores["limpa"]}')
                sleep(0.9)

                print(f'{cores["verde"]}Alterado com sucesso! {cores["limpa"]}')
#Laboratório
    if options == 2:
        answer = int(input(f'\t\t{cores["negrito"]}LABORATÓRIOS{cores["limpa"]}\n\t\t------------------------------------------------------------------\n\t\t {cores["magenta"]}{cores["negrito"]}5{cores["limpa"]} - Adicionar Professor ao Laboratório\n\t\t {cores["magenta"]}{cores["negrito"]}6{cores["limpa"]} - Remover Professor do Laboratório\n\t\t {cores["magenta"]}{cores["negrito"]}7{cores["limpa"]} - Verificar se pode entrar\n\t\t {cores["magenta"]}{cores["negrito"]}8{cores["limpa"]} - Listar Professores Permitidos\n\t\t {cores["magenta"]}{cores["negrito"]}0{cores["limpa"]} - Voltar\n ⤷ '))

        print(f'\n')

        # ADICIONAR NO LABORATÓRIO
        if answer == 5:
            lab = input('Laboratório na qual você adicionará o professor (ex: lab000): ')
            lab = lab.strip().lower()

            if lab == 'lab102' or lab == 'lab103' or lab == 'lab104' or lab == 'lab105' or lab == 'lab106' or lab == 'lab107':
                prof_code = input('\nProfessor à ser adicionado: ')
                prof_code = prof_code.strip().lower()

                # lab102
                if lab == 'lab102':
                    if prof_code in lab102:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código já cadastrado!{cores["limpa"]}')
                    else:
                        lab102 = lab102.append(prof_code)

                # lab103
                elif lab == 'lab103':
                    if prof_code in lab103:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código já cadastrado!{cores["limpa"]}')
                    else:
                        lab103 = lab103.append(prof_code)

                # lab104
                elif lab == 'lab104':
                    if prof_code in lab104:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código já cadastrado!{cores["limpa"]}')
                    else:
                        lab104 = lab104.append(prof_code)

                # lab105
                elif lab == 'lab105':
                    if prof_code in lab105:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código já cadastrado!{cores["limpa"]}')
                    else:
                        lab105 = lab105.append(prof_code)

                # lab106
                elif lab == 'lab106':
                    if prof_code in lab106:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código já cadastrado!{cores["limpa"]}')
                    else:
                        lab106 = lab106.append(prof_code)

                # lab107
                elif lab == 'lab107':
                    if prof_code in lab107:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código já cadastrado!{cores["limpa"]}')
                    else:
                        lab107 = lab107.append(prof_code)

            else:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}Laboratório não encontrado!{cores["limpa"]}')

        # REMOVER DO LABORATÓRIO
        elif answer == 6:
            lab_delete = input('Laboratório na qual você removerá o professor (EX: lab000): ')
            lab_delete = lab_delete.strip().lower()

            if lab_delete == 'lab102' or lab_delete == 'lab103' or lab_delete == 'lab104' or lab_delete == 'lab105' or lab_delete == 'lab106' or lab_delete == 'lab107':
                prof_delete = input('Código do professor: ')
                prof_delete = prof_delete.strip().lower()

                # lab102
                if lab_delete == 'lab102':
                    if prof_delete not in lab102:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado em {lab_delete}!{cores["limpa"]}')
                    else:
                        lab102.pop(prof_delete)

                # lab103
                elif lab_delete == 'lab103':
                    if prof_delete not in lab103:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado em {lab_delete}!{cores["limpa"]}')
                    else:
                        lab103.pop(prof_delete)

                # lab104
                elif lab_delete == 'lab104':
                    if prof_delete not in lab104:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado em {lab_delete}!{cores["limpa"]}')
                    else:
                        lab104.pop(prof_delete)

                # lab105
                elif lab_delete == 'lab105':
                    if prof_delete not in lab105:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado em {lab_delete}!{cores["limpa"]}')
                    else:
                        lab105.pop(prof_delete)

                # lab106
                elif lab_delete == 'lab106':
                    if prof_delete not in lab106:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado em {lab_delete}!{cores["limpa"]}')
                    else:
                        lab106.pop(prof_delete)

                # lab107
                elif lab_delete == 'lab107':
                    if prof_delete not in lab107:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado em {lab_delete}!{cores["limpa"]}')
                    else:
                        lab107.pop(prof_delete)

            else:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}Laboratório não encontrado!{cores["limpa"]}')

        # VER SE PODE ENTRAR
        elif answer == 7:
            lab_test = input('Laboratório (EX: lab000): ')
            lab_test = lab_test.strip().lower()

            if lab_test == 'lab102' or lab_test == 'lab103' or lab_test == 'lab104' or lab_test == 'lab105' or lab_test == 'lab106' or lab_test == 'lab107':
                prof_test = input('\nCódigo do professor (EX: 000): ')

                # lab102
                if lab_test == 'lab102':
                    if prof_test in lab102:
                        print(f'{cores["verde"]}Professor {prof_test} - {professors[prof_test]} pode entrar no {lab_test}!{cores["limpa"]}')
                    else:
                        print(f'{cores["vermelho"]}Professor {prof_test} - {professors[prof_test]} não pode entrar no {lab_test}!{cores["limpa"]}')

                # lab103
                elif lab_test == 'lab103':
                    if prof_test in lab103:
                        print(f'{cores["verde"]}Professor {prof_test} - {professors[prof_test]} pode entrar no {lab_test}!{cores["limpa"]}')
                    else:
                        print(f'{cores["vermelho"]}Professor {prof_test} - {professors[prof_test]} não pode entrar no {lab_test}!{cores["limpa"]}')

                # lab104
                elif lab_test == 'lab104':
                    if prof_test in lab104:
                        print(f'{cores["verde"]}Professor {prof_test} - {professors[prof_test]} pode entrar no {lab_test}!{cores["limpa"]}')
                    else:
                        print(f'{cores["vermelho"]}Professor {prof_test} - {professors[prof_test]} não pode entrar no {lab_test}!{cores["limpa"]}')

                # lab105
                elif lab_test == 'lab105':
                    if prof_test in lab105:
                        print(f'{cores["verde"]}Professor {prof_test} - {professors[prof_test]} pode entrar no {lab_test}!{cores["limpa"]}')
                    else:
                        print(f'{cores["vermelho"]}Professor {prof_test} - {professors[prof_test]} não pode entrar no {lab_test}!{cores["limpa"]}')

                # lab106
                elif lab_test == 'lab106':
                    if prof_test in lab106:
                        print(f'{cores["verde"]}Professor {prof_test} - {professors[prof_test]} pode entrar no {lab_test}!{cores["limpa"]}')
                    else:
                        print(f'{cores["vermelho"]}Professor {prof_test} - {professors[prof_test]} não pode entrar no {lab_test}!{cores["limpa"]}')

                # lab107
                elif lab_test == 'lab107':
                    if prof_test in lab107:
                        print(f'{cores["verde"]}Professor {prof_test} - {professors[prof_test]} pode entrar no {lab_test}!{cores["limpa"]}')
                    else:
                        print(f'{cores["vermelho"]}Professor {prof_test} - {professors[prof_test]} não pode entrar no {lab_test}!{cores["limpa"]}')

            else:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}Laboratório não encontrado!{cores["limpa"]}')

        # PROFESSORES PERMITIDOS
        elif answer == 8:
            lab_permission=input('Laboratório (EX: lab000): ')
            lab_permission=lab_permission.strip().lower()

            #lab102
            if lab_permission == lab102:
                for code in lab102:
                    print (f'{code} - {professors[code]}')

            #lab103
            if lab_permission == lab103:
                for code in lab103:
                    print (f'{code} - {professors[code]}')

            #lab104
            if lab_permission == lab104:
                for code in lab104:
                    print (f'{code} - {professors[code]}')

            #lab105
            if lab_permission == lab105:
                for code in lab105:
                    print (f'{code} - {professors[code]}')

            #lab106
            if lab_permission == lab106:
                for code in lab106:
                    print (f'{code} - {professors[code]}')


           #lab107
            if lab_permission == lab107:
                for code in lab107:
                    print (f'{code} - {professors[code]}')
