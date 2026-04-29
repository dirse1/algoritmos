estacionamento = 0

while True:
    opcao = int(input('=== CONTROLE DE ESTACIONAMENTO ===\n[1] Registrar entrada de veículo\n[2] Registrar saída de veículo\n[3] Exibir vagas ocupadas e disponíveis\n[4] Encerrar programa\n'))
    if opcao == 1:
        if estacionamento < 10:
            veiculosAdd = int(input('Quantos veículos entraram?: '))
            if estacionamento+veiculosAdd <= 10:
                estacionamento += veiculosAdd
                print(f'{veiculosAdd} unidades adicionadas com sucesso!')
            else:
                print('O número máximo de veículos é 10')
        else:
            print('O estacionamento está cheio.')
    elif opcao == 2:
            veiculosRem = int(input('Quantos veiculos sairam?: '))
            if estacionamento > 0:
                if estacionamento-veiculosRem >= 0:
                    estacionamento -= veiculosRem
                    print(f'{veiculosRem} Veiculos removidos com sucesso!')
                else:
                    print('Não há mais veículos no estacionamento.')
            else:
                print('O estacionamento já está vazio')
    elif opcao == 3:
        print(f'O estacionamento tem {estacionamento} vagas ocupadas')
        print(f'O estacionamento tem {10-estacionamento} vagas disponíveis')
    elif opcao == 4:
        break
