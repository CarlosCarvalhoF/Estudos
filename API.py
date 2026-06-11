opcao = 0
participantes = []

while opcao != 6:

    print('=========================')
    print('TECHCONNECT EVENTOS')
    print('=========================')

    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Buscar')
    print('4 - Estatísticas')
    print('5 - Ranking')
    print('6 - Sair')

    opcao = int(input('Escolha uma das opções: '))

    if opcao < 1 or opcao > 6:
        print('Opção inválida!')

    
    elif opcao == 1:

        print('=== Cadastro de Participante ===')

        nome = input('Digite o nome: ')
        curso = input('Digite o curso: ')

        print('Nome:', nome)
        print('Curso:', curso)
        presenca = float(input('Digite a presença: '))
        nota1 = float(input('Digite a nota 1: '))
        nota2 = float(input('Digite a nota 2: '))
        nota3 = float(input('Digite a nota 3: '))
        media=(nota1+nota2+nota3)/3
        
        participante=[nome,curso,presenca,nota1,nota2,nota3,media]
        participantes.append(participante)
        print(nome)
        print(curso)
        print(presenca)
        print(nota1)
        print(nota2)
        print(nota3)
        print(media)
        print('Cadastrado com sucesso!')

    elif opcao== 2:
        for parcipante in participantes:
            print('=====Lista de Participantes=====')
            print('nome:',participante[0])
            print('curso:',participante[1])
            print('presenca:',participante[2])
            print('nota 1:',participante[3])
            print('nota 2:',participante[4])
            print('nota 3:',participante[5])
            print('media:',participante[6])

            print('SISTEMA ENCERRADO')        
    
    elif opcao== 3:
        nome_busca = input("Digite o nome do participante: ").strip()

        encontrou = False

        for participante in participantes:

            if participante[0] == nome_busca:

                print("\nParticipante encontrado!")
                print("Nome:", participante[0])
                print("Curso:", participante[1])
                print("Presença:", participante[2])
                print("Nota 1:", participante[3])
                print("Nota 2:", participante[4])
                print("Nota 3:", participante[5])

                encontrou = True
                break

        if encontrou == False:
            print("Participante não encontrado")

    elif opcao==4:

        if len(participantes) == 0:
            print('Nenhum participante cadastrado.')
 
        else:
 
            aprovados = 0
            recuperacao = 0
            reprovados = 0
 
            somaMedia = 0
            somaPresenca = 0
 
            maiorMedia = participantes[0][6]
            menorMedia = participantes[0][6]
 
            for participante in participantes:
 
                if participante[6] > maiorMedia:
                    maiorMedia = participante[6]
 
                if participante[6] < menorMedia:
                    menorMedia = participante[6]
 
                if participante[6] >= 7 and participante[2] >= 75:
                    aprovados += 1
 
                elif participante[6] >= 5 and participante[2] >= 75:
                    recuperacao += 1
 
                else:
                    reprovados += 1
 
                somaMedia += participante[6]
 
                somaPresenca += participante[2]
 
            mediaTurma = somaMedia / len(participantes)
 
            mediaPresenca = somaPresenca / len(participantes)
 
            print(f'''
======== ESTATÍSTICAS ========''')    
    elif opcao == 5:
      #Ranking
      # Verifica se existem participantes cadastrados
        if len(participantes) == 0:
            print('Nenhum participante cadastrado.')
        else:
          participantes.sort(key=lambda x: x[6], reverse=True)
          posicao = 1
          print(10*'=','RANKING', 10*'=')
          for participante in participantes:
            print(f'{posicao}ª-{participante[0]}')
            print(f'Média: {participante[6]}')
            posicao +=1
    else:
        print('Opção inválida')
 
print('Programa finalizado')    
               

        

