from random import randint

while True:
    print("""O jogo de adivinhação irá começar, você está preparado?
    [1] - SIM
    [2] - NÂO 
    """)

    opcao = input('Jogador: ')

    if opcao == '1' or opcao == '2':
        if opcao == '2':
            print(""Tudo bem, quando quiser começar pressione a tecla 'enter'"")
            print()
            comecar = input('Pressione a tecla "enter" para começar')
            print()

        user1 = int(input('Escolha um número: '))
        user2 = int(input('Escolha outro número: '))

        if user1 > user2:
            pc = randint(user2, user1)
        else:
            pc = randint(user1, user2)

        print('Número aleatório escolhido, agora chegou a sua vez. Tentativas(10)')
        for i in range(1, 11):
            usuario = int(input('>> '))
            if usuario == pc:
                print('Parabéns, você acertou.')
                break
            elif usuario > pc:
                print(f'Errou, o número é menor. Tentativas restantes({10 - i})')
            elif usuario < pc:
                print(f'Errou, o número é maior. Tentativas restantes({10 - i})')

        print()
        print(20 * '=')
        print()
        
        print("""Deseja jogar novamente?
        [1] - SIM
        [2] - NÂO              
                       """)
        
        resposta = input('Qual opção você deseja? ')
        
        if resposta == '1':
            print()
            print(20 * '=')
            print()
        elif resposta == '2':
            print('Foi um prazer tê-lo aqui, espero que tenha gostado. Até mais!')
            break
        else:
            print('\nOPS, alguma coisa deu errado. Tente novamente\n')

    else:
        print()
        print('OPS, alguma coisa deu errado. Tente novamente')
        print()
