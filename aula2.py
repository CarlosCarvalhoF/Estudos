def cadastrar_produto(nome, preco, qtd_inicial):
    # O estoque inicial e o atual começam iguais, e a venda começa em 0
    produtos = {
        'nome': nome,
        'preco': float(preco),
        'estoque': int(qtd_inicial),
        'qtd_inicial': int(qtd_inicial),
        'qtd_ven': 0  
    }
    return produtos


def exibir_produtos(produtos):
    print('\n==== DADOS DO PRODUTO ====')
    print(f"Nome: {produtos['nome']}")
    print(f"Preço: R$ {produtos['preco']:.2f}")
    print(f"Estoque Atual: {produtos['qtd_inicial']}")
    print(f"Quantidade Vendida: {produtos['qtd_ven']}")

def menu():
    print('''1.CADASTRAR PRODUTOS
2.VENDER PRODUTOS
3.EXIBIR PRODUTOS
4.SAIR''')
