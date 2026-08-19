from time import sleep
from datetime import datetime

cores = {
    # Reseta a cor para o padrão do sistema (OBRIGATÓRIO usar no final)
    'limpa': '\033[m',
    
    # Estilos de Texto
    'negrito': '\033[1m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'magenta': '\033[35m'}

print (f'==================================== lista de exercício plus ====================================')
print(f'------------------------------------------- Questão 2 -------------------------------------------\n')
print ("A situação de logística da Empresa Alpha Entregas está necessitando de melhorias no controle das\nsaídas e retornos dos caminhões. O sistema deve possuir:\n")
print ("\n\n\t• Cadastro dos caminhões e dos condutores;\n\n\t• Cadastro com uma lista de todos os caminhões que saem diariamente;\n\n\t• Registro da data e hora de saída de cada veículo, bem como o condutor responsável;\n\n\t• Registro da data e hora de chegada de cada caminhão;\n\n\t• Verificação se determinado caminhão retornou da rota ou não;\n\n\t• Listagem do cadastro de caminhões;\n\n\t• Listagem dos condutores;\n\n\t• Listagem, por data, dos veículos que retornaram;\n\n\t• Verificação se todas as entregas do dia foram realizadas.")
print(f'\n------------------------------------------------------------------------------------------------\n')

drivers = {'001' : 'Roberto Souza',
           '002' : 'João Graciano',
           '003' : 'Karine Silva',
           '004' : 'Pedro Luiz',
           '005' : 'Maria Catarina',
           '006' : 'Júlio Cardoso',
           '007' : 'Altivo Antônio',
           '008' : 'Jorge Gonçalves',
           '009' : 'Marcos Vinícius',
           '010' : 'Heleno Nunes',
           '011' : 'Mara Cristina',
           '012' : 'Otávio Rocha'}

trucks = {'001' : 'Monobloco',
          '002' : 'Scania 112 HW',
          '003' : 'Volkswagen Express 4150',
          '004' : 'Volkswagen Express 6160',
          '005' : 'Volkswagen VW 17230 Worker',
          '006' : 'Volkswagen Express 9170',
          '007' : 'Iveco Daily 40s14',
          '008' : 'Iveco Tectro 310E28'}

daily_routes = []

while True:
    options = int(input(f'\t\t{cores["negrito"]}Selecione a baixo, o que você deseja fazer:\n\t\t------------------------------------------------------------------{cores["limpa"]}\n\t\t {cores["magenta"]}{cores["negrito"]}1{cores["limpa"]} - Caminhões (Listar, Alterar, Remover e Adicionar)\n\t\t {cores["magenta"]}{cores["negrito"]}2{cores["limpa"]} - Condutores (Listar, Alterar, Remover e Adicionar)\n\t\t {cores["magenta"]}{cores["negrito"]}3{cores["limpa"]} - Saídas e retornos dos caminhões\n\t\t {cores["magenta"]}{cores["negrito"]}4{cores["limpa"]} - Verificar retorno de caminhão\n\t\t {cores["magenta"]}{cores["negrito"]}5{cores["limpa"]} - Listar veículos que retornaram por data\n\t\t {cores["magenta"]}{cores["negrito"]}6{cores["limpa"]} - Verificar entregas do dia\n\t\t {cores["magenta"]}{cores["negrito"]}0{cores["limpa"]} - Sair\n ⤷ '))

    # Caminhões
    if options == 1:
        answer = int(input(f'\t\t{cores["negrito"]}CAMINHÕES{cores["limpa"]}\n\t\t------------------------------------------------------------------\n\t\t {cores["magenta"]}{cores["negrito"]}1{cores["limpa"]} - Listar Caminhões\n\t\t {cores["magenta"]}{cores["negrito"]}2{cores["limpa"]} - Adicionar Caminhão\n\t\t {cores["magenta"]}{cores["negrito"]}3{cores["limpa"]} - Remover Caminhão\n\t\t {cores["magenta"]}{cores["negrito"]}4{cores["limpa"]} - Alterar Caminhão\n\t\t {cores["magenta"]}{cores["negrito"]}0{cores["limpa"]} - Voltar\n ⤷ '))

        print(f'\n')

        if answer == 0:
            break

        # LISTAR
        elif answer == 1:
            for k, v in trucks.items():
                print(f'{k} - {v}')

        # CADASTRO
        elif answer == 2:
            adittion_code = input('\nDigite o código: ')

            if adittion_code in trucks:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código já cadastrado!{cores["limpa"]}')

            else:
                adittion_name = input('\nDigite o modelo do caminhão: ')
                trucks[adittion_code] = adittion_name
                print(f'{cores["verde"]}Adicionado com sucesso! {cores["limpa"]}')

        # EXCLUIR
        elif answer == 3:
            delete = input('Coloque o código do caminhão a ser excluido: ')

            if delete in trucks:
                del trucks[delete]
                print(f'{cores["verde"]}{cores["negrito"]}Exclusão bem sucedida!{cores["limpa"]}')

            else:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado!{cores["limpa"]}')

        # ALTERAR
        elif answer == 4:
            change = input('Qual caminhão deve ser alterado? Digite o código: ')

            if change in trucks:
                print(f'{cores["negrito"]}Código encontrado.{cores["limpa"]}')

                new_name = input('\nColoque o novo modelo: ')
                trucks[change] = new_name

                print(f'\n{cores["magenta"]}Alterando...{cores["limpa"]}')
                sleep(0.9)

                print(f'{cores["verde"]}Alterado com sucesso! {cores["limpa"]}')

            else:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado!{cores["limpa"]}')

    # Condutores
    if options == 2:
        answer = int(input(f'\t\t{cores["negrito"]}CONDUTORES{cores["limpa"]}\n\t\t------------------------------------------------------------------\n\t\t {cores["magenta"]}{cores["negrito"]}1{cores["limpa"]} - Listar Condutores\n\t\t {cores["magenta"]}{cores["negrito"]}2{cores["limpa"]} - Adicionar Condutor\n\t\t {cores["magenta"]}{cores["negrito"]}3{cores["limpa"]} - Remover Condutor\n\t\t {cores["magenta"]}{cores["negrito"]}4{cores["limpa"]} - Alterar Condutor\n\t\t {cores["magenta"]}{cores["negrito"]}0{cores["limpa"]} - Voltar\n ⤷ '))

        print(f'\n')

        if answer == 0:
            break

        # LISTAR
        elif answer == 1:
            for k, v in drivers.items():
                print(f'{k} - {v}')

        # CADASTRO
        elif answer == 2:
            adittion_code = input('\nDigite o código: ')

            if adittion_code in drivers:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código já cadastrado!{cores["limpa"]}')

            else:
                adittion_name = input('\nDigite o nome do(a) condutor(a): ')
                drivers[adittion_code] = adittion_name
                print(f'{cores["verde"]}Adicionado com sucesso! {cores["limpa"]}')

        # EXCLUIR
        elif answer == 3:
            delete = input('Coloque o código do condutor a ser excluido: ')

            if delete in drivers:
                del drivers[delete]
                print(f'{cores["verde"]}{cores["negrito"]}Exclusão bem sucedida!{cores["limpa"]}')

            else:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado!{cores["limpa"]}')

        # ALTERAR
        elif answer == 4:
            change = input('Qual condutor deve ser alterado? Digite o código: ')

            if change in drivers:
                print(f'{cores["negrito"]}Código encontrado.{cores["limpa"]}')

                new_name = input('\nColoque o novo nome: ')
                drivers[change] = new_name

                print(f'\n{cores["magenta"]}Alterando...{cores["limpa"]}')
                sleep(0.9)

                print(f'{cores["verde"]}Alterado com sucesso! {cores["limpa"]}')

            else:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}código não encontrado!{cores["limpa"]}')

    # Saídas e retornos
    if options == 3:
        answer = int(input(f'\t\t{cores["negrito"]}SAÍDAS E RETORNOS{cores["limpa"]}\n\t\t------------------------------------------------------------------\n\t\t {cores["magenta"]}{cores["negrito"]}1{cores["limpa"]} - Registrar saída de caminhão\n\t\t {cores["magenta"]}{cores["negrito"]}2{cores["limpa"]} - Registrar retorno de caminhão\n\t\t {cores["magenta"]}{cores["negrito"]}3{cores["limpa"]} - Listar caminhões que saíram\n\t\t {cores["magenta"]}{cores["negrito"]}0{cores["limpa"]} - Voltar\n ⤷ '))

        print(f'\n')

        if answer == 0:
            break

        # REGISTRAR SAÍDA
        elif answer == 1:
            truck_code = input('Código do caminhão: ')

            if truck_code not in trucks:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}caminhão não encontrado!{cores["limpa"]}')

            else:
                driver_code = input('Código do condutor: ')

                if driver_code not in drivers:
                    print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}condutor não encontrado!{cores["limpa"]}')

                else:
                    route_date = input('Data da saída (DD/MM/AAAA): ')
                    route_time = input('Hora da saída (HH:MM): ')

                    route = {
                        'truck_code': truck_code,
                        'driver_code': driver_code,
                        'departure_date': route_date,
                        'departure_time': route_time,
                        'arrival_date': '',
                        'arrival_time': ''
                    }

                    daily_routes.append(route)

                    print(f'{cores["verde"]}Saída registrada com sucesso! {cores["limpa"]}')

        # REGISTRAR RETORNO
        elif answer == 2:
            truck_code = input('Código do caminhão: ')

            if truck_code not in trucks:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}caminhão não encontrado!{cores["limpa"]}')

            else:
                driver_code = input('Código do condutor: ')

                if driver_code not in drivers:
                    print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}condutor não encontrado!{cores["limpa"]}')

                else:
                    route_found = False

                    for route in daily_routes:
                        if route['truck_code'] == truck_code and route['driver_code'] == driver_code and route['arrival_date'] == '':
                            arrival_date = input('Data da chegada (DD/MM/AAAA): ')
                            arrival_time = input('Hora da chegada (HH:MM): ')

                            route['arrival_date'] = arrival_date
                            route['arrival_time'] = arrival_time

                            route_found = True

                            print(f'{cores["verde"]}Retorno registrado com sucesso! {cores["limpa"]}')
                            break

                    if route_found == False:
                        print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}saída não encontrada ou caminhão já retornou!{cores["limpa"]}')

        # LISTAR SAÍDAS
        elif answer == 3:
            for route in daily_routes:
                print(f'{route["truck_code"]} - {trucks[route["truck_code"]]} - {route["departure_date"]} {route["departure_time"]} - {drivers[route["driver_code"]]}')

    # VERIFICAR RETORNO
    if options == 4:
        truck_code = input('Código do caminhão: ')

        if truck_code not in trucks:
            print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}caminhão não encontrado!{cores["limpa"]}')

        else:
            route_found = False

            for route in daily_routes:
                if route['truck_code'] == truck_code:
                    route_found = True

                    if route['arrival_date'] != '':
                        print(f'{cores["verde"]}Caminhão {truck_code} - {trucks[truck_code]} retornou da rota!{cores["limpa"]}')
                        print(f'Data de chegada: {route["arrival_date"]}')
                        print(f'Hora de chegada: {route["arrival_time"]}')
                        print(f'Condutor: {drivers[route["driver_code"]]}')
                    else:
                        print(f'{cores["vermelho"]}Caminhão {truck_code} - {trucks[truck_code]} ainda não retornou da rota!{cores["limpa"]}')
                        print(f'Data de saída: {route["departure_date"]}')
                        print(f'Hora de saída: {route["departure_time"]}')
                        print(f'Condutor: {drivers[route["driver_code"]]}')

                    break

            if route_found == False:
                print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}nenhuma saída encontrada para este caminhão!{cores["limpa"]}')

    # LISTAR RETORNOS POR DATA
    if options == 5:
        search_date = input('Digite a data que deseja consultar (DD/MM/AAAA): ')

        route_found = False

        for route in daily_routes:
            if route['arrival_date'] == search_date:
                print(f'{route["truck_code"]} - {trucks[route["truck_code"]]} - {route["arrival_date"]} {route["arrival_time"]} - {drivers[route["driver_code"]]}')
                route_found = True

        if route_found == False:
            print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}nenhum caminhão retornou nesta data!{cores["limpa"]}')

    # VERIFICAR ENTREGAS
    if options == 6:
        search_date = input('Digite a data que deseja consultar (DD/MM/AAAA): ')

        total_routes = 0
        completed_routes = 0

        for route in daily_routes:
            if route['departure_date'] == search_date:
                total_routes += 1

                if route['arrival_date'] != '':
                    completed_routes += 1

        if total_routes == 0:
            print(f'{cores["negrito"]}ERRO: {cores["vermelho"]}nenhuma saída encontrada nesta data!{cores["limpa"]}')

        elif total_routes == completed_routes:
            print(f'{cores["verde"]}{cores["negrito"]}Todas as entregas do dia foram realizadas!{cores["limpa"]}')
            print(f'Entregas realizadas: {completed_routes}/{total_routes}')

        else:
            print(f'{cores["vermelho"]}{cores["negrito"]}Ainda existem entregas pendentes!{cores["limpa"]}')
            print(f'Entregas realizadas: {completed_routes}/{total_routes}')