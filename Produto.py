import csv

class Produto:
    def __init__(self, nome, preco, descricao, marca, quantidade):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.marca = marca
        self.quantidade = quantidade
    
    def __cadastrarProduto__(self):
        with open('produtos.csv', 'a', newline='', encoding='utf-8') as csvfile:
            produtos = csv.writer(csvfile, delimiter=',',quotechar='|')
            produtos.writerow([self.nome, self.preco, self.descricao, self.marca, self.quantidade])
        return

    @staticmethod
    def __listaProdutos__():
        print(f"{"NOME":<30} {"PREÇO":<10} {"DESCRIÇÃO":<70} {"MARCA":<30} {"QUANTIDADE":<30}")

        with open('produtos.csv', newline='', encoding='utf-8') as csvfile:
            produtos = csv.reader(csvfile, delimiter=',', quotechar='|')
            for linha in produtos:
                print(f"{linha[0]:<30} {linha[1]:<10} {linha[2]:<70} {linha[3]:<30} {linha[4]:<30}")
        return
    
    @staticmethod
    def __removerProduto__(nomeProduto):
        linhas = []

        with open('produtos.csv', 'r', newline='', encoding='utf-8') as csvfile:
            leitor = csv.reader(csvfile, delimiter=',', quotechar='|')
            for linha in leitor:
                if linha[0].upper() != nomeProduto.upper():
                    linhas.append(linha)
        
        with open('produtos.csv', 'w', newline='', encoding='utf-8') as csvfile:
            produtos = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            produtos.writerows(linhas)
        
        return
    
    @staticmethod
    def __buscarProdutosPorPreco__(precoInicial, precoFinal):
        linhas = []

        print("\n=======================================")
        print(f"{"NOME":<30} {"PREÇO":<10} {"DESCRIÇÃO":<70} {"MARCA":<30} {"QUANTIDADE":<30}")

        with open('produtos.csv', 'r', newline='', encoding='utf-8') as csvfile:
            leitor = csv.reader(csvfile, delimiter=',', quotechar='|')
            for linha in leitor:
                if float(linha[1]) >= precoInicial and float(linha[1]) <= precoFinal:
                    linhas.append(linha)

        for linha in linhas:
            print(f"{linha[0]:<30} {linha[1]:<10} {linha[2]:<70} {linha[3]:<30} {linha[4]:<30}")
        
        return