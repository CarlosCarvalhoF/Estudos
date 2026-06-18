class Pet:
    def __init__(self,nome,especie,cidade,porte,):
        self.nome=nome
        self.especie=especie
        self.cidade=cidade
        self.porte=porte
        self.status='disponivel'

    def adota_pets(self):
        self.status='Adotado'


lista_de_pets=[]



def fazer_busca_por_cidade(gaveta_de_pets,cidade_desejada):
    print(f'procurando pets em: {cidade_desejada}')
    
    for ficha in gaveta_de_pets:
        if ficha.cidade==  cidade_desejada:
            print(f' encontrei o nome dele é {ficha.nome}')
            

while True:
    print('''=== MENU PRINCIPAL===
          
1 = CADASTRAR PET
2 = ADOTAR PET
3 = SOLICITAÇOES 
4 = RANKING
5 = RELATÓRIOS
0 = SAIR''')

    opcao=int(input('Escolha uma opcao: '))  

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

    elif opcao==3:
        print('Abrindo a tela Solicitações pet...')

    elif opcao==4:
        print('Abrindo a tela de Ranking pet...')

    elif opcao==5:
        print('Abrindo a tela de Relatórios pet...')

    elif opcao==0:
        print('Saindo do sistema... Até logo!')
        break

    else:
        print('Opcão inválida!, escolha de 0 a 5: ')    
           
            
            
        

    
    



