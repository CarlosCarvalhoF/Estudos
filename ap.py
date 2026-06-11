acao = 0
participantes = []
 
 
while acao != 6:
    print('''=================================
TECHCONNECT EVENTOS
=================================
 
1 - Cadastrar participante
2 - Listar participantes
3 - Buscar participante
4 - Exibir estatísticas
5 - Exibir ranking
6 - Sair
====================================================================================''')
    acao = int(input('O que você quer fazer agora? '))
 
    if acao == 1: #Cadastrar
        #Validação Nome
        nome = input('Digite o nome do participante: ').strip().lower()
        while nome.strip() == '':
            nome = input('Nome invalido\nDigite o nome do participante: ').strip().lower()
        #Validação curso
        curso = input('Digite o curso do participante: ').strip().lower()
        while curso.strip() == '':
            curso = input('Curso inválido\ndigite o curso do participante: ').strip().lower()
        #Validação presença
        presenca = int(input('Digite a presenção do participante: '))
        while presenca <0 or presenca >100:
            presenca = int(input('Presença inválida\nDigite a presenção do participante: '))
        #Validação notas
        n1 = float(input("Digite a 1ª nota:  "))
        while n1 <0 or n1 > 10:
            n1 = float(input("Nota inválida, digite a 1ª nota: "))
 
        n2 = float(input("Digite a 2ª nota:  "))
        while n2 <0 or n2 > 10:
            n2 = float(input("Nota inválida, digite a 2ª nota: "))
 
        n3 = float(input("Digite a 3ª nota:  "))
        while n3 <0 or n3 > 10:
            n3 = float(input("Nota inválida, digite a 3ª nota: "))
        media = (n1 + n2 + n3) / 3
        #Armazenar informações
        participante = [nome, curso, presenca, n1, n2, n3, (media)]
        participantes.append(participante)
        print('Participante cadastrado com sucesso!')
 
    elif acao == 2:
      #Listar
      # Verifica se existem participantes cadastrados
        if len(participantes) == 0:
          print('lista vazia')
        else:
          #Percorre a lista para buscar as informações
          for participante in participantes:
            print(30*'=')
            print(f'''
    Nome: {participante[0]}
    Curso: {participante[1]}
    Presença: {participante[2]}
    Notas: {participante[3], participante[4], participante[5]}
    Media: {participante[6]:.2f}''')
            print(30*'=')
 
 
 
    elif acao == 3:
 
        encontrou = False
        busca = input('Digite o nome do participante: ').strip().lower()
 
        for participante in participantes:
                if busca in participante[0]:
                    print(30*'=')
                    print(f'''
Nome: {participante[0]}
Curso: {participante[1]}
Presença: {participante[2]}
Notas: {participante[3], participante[4], participante[5]}
Media: {participante[6]:.2f}''')
                    print(30*'=')
                    encontrou = True
        if encontrou == False:
            print('Participante não encontrado')
 
 
 
    elif acao == 4:
    # Estatísticas
 
    # Verifica se existem participantes cadastrados
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
======== ESTATÍSTICAS ========
 
Maior média: {maiorMedia}
Menor média: {menorMedia}
 
Número de aprovados: {aprovados}
Número de recuperação: {recuperacao}
Número de reprovados: {reprovados}
 
Média geral da turma: {mediaTurma:.2f}
Média de presença: {mediaPresenca:.2f}%
 
==============================
    ''')
 
 
    elif acao == 5:
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
 