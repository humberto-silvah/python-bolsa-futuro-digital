class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Estoque:

    def __init__(self):
        self.produtos = []
        self.quantidade_de_produtos = 0

    def quantidade_de_itens(self):
        self.quantidade_de_produtos = len(self.produtos)
        return self.quantidade_de_produtos  

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")

    def valor_total_estoque(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco * produto.quantidade
        return total

produto1 = Produto("Caneta", 1.50, 100)
produto2 = Produto("Caderno", 15.00, 50)
produto3 = Produto("Mochila", 120.00, 20)
estoque = Estoque()
estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)
estoque.adicionar_produto(produto3)
estoque.listar_produtos()
print(f"Quantidade de produtos no estoque: {estoque.quantidade_de_itens()}")
print(f"Valor total do estoque: R$ {estoque.valor_total_estoque():.2f}")