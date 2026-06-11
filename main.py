from aula2 import cadastrar_produto
from aula2 import exibir_produtos
from aula2 import menu

lista_de_produtos=[]
while True:
    menu()
    opcao=int(input('Digite uma opcão ou [4] pra sair: '))    
    print(f'Opção escolhida foi: {opcao}')   
    if opcao==1:
        print('===CADASTRO DE PRODUTOS===')

        nome=input('Nome do produto: ')
        preco=float(input('Preço:R$ '))
        qtd_inicial= int(input('Quantidade em estoque: '))

        novo_produto=cadastrar_produto(nome,preco,qtd_inicial)

        lista_de_produtos.append(novo_produto)
    
        print('\n[Sucesso]\n Produto adicionado à lista!')
   
    elif opcao == 2:
        print('===VENDA===')
        print('-'*30)
        for prod in lista_de_produtos:
            print(f"- {prod['nome']} (Estoque: {prod['qtd_inicial']})")
        print("-" * 30)
        busca_nome = input('Digite o nome do produto para venda: ')
        produto_encontrado=False

        for novo_produto in lista_de_produtos:
            if novo_produto['nome'] == busca_nome.lower().strip():
                qtd_ven = int(input('Quantidade vendida: '))
                produto_encontrado=True
                
                if qtd_ven <= novo_produto['qtd_inicial']:
                    print('Venda realizada!')
                    novo_produto['qtd_inicial'] = novo_produto['qtd_inicial'] - qtd_ven
                    novo_produto['qtd_ven'] = novo_produto['qtd_ven'] + qtd_ven
                else:
                    print('[ERRO] Estoque insuficiente! Não é possivel realizar a venda ')
                
                break  
        if produto_encontrado == False:
            print('[ERRO] Produto não cadastrado ou nome incorreto!')            

    elif opcao == 3:
        print('===RELATÓRIO GERAL DE ESTOQUE E VENDAS===')  
            
        if len(lista_de_produtos) == 0:
            print("[Aviso] Nenhum produto cadastrado para exibir.")
            
        else:
            for produto in lista_de_produtos:
                
                exibir_produtos(produto)
                
                
                total_vendido = produto['preco'] * produto['qtd_ven']
                print(f"Valor total faturado: R$ {total_vendido:.2f}")
                print("-" * 30)

    elif opcao == 4:
        print('Saindo do sistema... Até logo!')
        break            
