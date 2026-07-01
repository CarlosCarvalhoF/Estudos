class Pet:
    def __init__(self,nome,especie,cidade,porte,):
        self.nome=nome
        self.especie=especie
        self.cidade=cidade
        self.porte=porte
        self.status='Disponivel'

    def adota_pets(self):
        self.status='Adotado'


lista_de_pets=[]
solicitacoes_pet = []


def fazer_busca_por_cidade(gaveta_de_pets, cidade_desejada):
    print(f'\nProcurando pets em: {cidade_desejada}')
    encontrou = False
    
    for ficha in gaveta_de_pets:
        if ficha.cidade.lower() == cidade_desejada.lower():
            print(f'- Encontrei! O nome dele é {ficha.nome} ({ficha.especie}) | Status: {ficha.status}')
            encontrou = True
            
    if not encontrou:
        print('Nenhum pet encontrado nesta cidade.')

while True:
    print('''=== MENU PRINCIPAL===
          
1 = CADASTRAR PET
2 = ADOTAR PET
3 = SOLICITAÇOES 
4 = RANKING
5 = RELATÓRIOS
6 = BUSCA PET POR CIDADE          
0 = SAIR''')

    opcao=int(input('Escolha uma opção: '))  

    if opcao==1:

        nome=input('qual nome do pet: ')
        especie=input('qual é a espécie: ')     
        cidade=input('qual cidade do pet: ')
        porte=input('qual porte pet: ')  

        novo_pet = Pet(nome, especie, cidade, porte)
        lista_de_pets.append(novo_pet)

        print("Pet cadastrado com sucesso!")

    
    elif opcao==2:
        print(' ===== Pets no Abrigo =====')

        for ficha in lista_de_pets:
            print(f"Nome: {ficha.nome} | Espécie: {ficha.especie} | Status: {ficha.status}")
            
        nome_buscado=input('Qual nome do pet deseja adotar: ')
        for ficha in lista_de_pets:
            if ficha.nome==nome_buscado:
                ficha.adota_pets()
                print('Parabens, adoção realizada')

    elif opcao == 3:
        print('Abrindo a tela Solicitações pet...')
        print('1 = CRIAR NOVA SOLICITAÇÃO')
        print('2 = VER SOLICITAÇÕES')
        print('0 = VOLTAR AO MENU PRINCIPAL')

        sub_menu_soli = int(input('Escolha uma das opções: '))

        if sub_menu_soli == 1:
            nome_solicitante = input('Informe seu nome: ')
            idade_solicitante = int(input('Informe sua idade: '))
            
            if idade_solicitante < 18:
                print('Erro: Adoção permitida apenas para maiores de 18 anos.')

            else:
                telefone_solicitante = input('Informe seu numero de telefone: ')
                animal_solicitante = input('Nome do pet de interesse: ')

                pet_existe = False

                # Busca o pet na lista
                for ficha in lista_de_pets:
                    if ficha.nome.lower() == animal_solicitante.lower():
                        pet_existe = True
                        break

                # Valida se encontrou o pet
                if pet_existe == True:
                    nova_solicitacao = {
                        'solicitante': nome_solicitante, 
                        'telefone': telefone_solicitante, 
                        'pet_desejado': animal_solicitante
                    }
                    solicitacoes_pet.append(nova_solicitacao)
                    print('Sucesso! Solicitação registrada no sistema.')
                
                else:
                    # Este é o bloco que faltava no seu código!
                    print('Erro: Pet não encontrado no banco de dados.')

    elif opcao==4:
        print('Abrindo a tela de Ranking pet...')

    elif opcao==5:
        
        total_disponivel=0
        total_Adotado=0
        for ficha in lista_de_pets:
            if ficha.status== 'Disponivel':
               
                total_disponivel=total_disponivel+1
    
            elif ficha.status=='Adotado' :   

                total_adotado=total_adotado+1
        print(f'Total de Pest Disponivel: {total_disponivel}')
        print(f'Total de Pest Adotado: {total_adotado}')        

    elif opcao == 6:
        cidade_busca = input('Digite a cidade que deseja pesquisar: ')
        fazer_busca_por_cidade(lista_de_pets, cidade_busca)

    elif opcao==0:
        print('Saindo do sistema... Até logo!')
        break

    else:
        print('Opcão inválida!, escolha de 0 a 5: ')    
           
            
            
        

    
    



